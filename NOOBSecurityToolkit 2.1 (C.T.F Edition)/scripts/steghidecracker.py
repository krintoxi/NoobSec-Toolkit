import os
import inspect
import sys
import commands
import threading


def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        wordlistname = sys.argv[2]

    else:
        print("Using => steghidecracker.py [file] [wordlist]")

        sys.exit()

    runningpath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    file = wordlistname;
    wordlist = open(file).readlines();
    length = len(wordlist)
    i = 1;
    for line in wordlist:
        remaining = length - i
        output = commands.getoutput("steghide extract -sf " + filename.strip() + " -p " + line.strip())
        if output.find("could not extract") == -1:
            print("FOUND!!!!!!=> " + line)
            print(output)
            break
        else:
            print("Remaining :" + str(remaining))

        i = i + 1


if __name__ == '__main__':
    main()
