# NoobSecToolkit v3

> "All day, every day."

A Python 3 penetration testing framework designed to make security tools accessible to students and beginners. Bundles together widely-used open-source security tools with simplified interfaces and predefined configurations.

> **Successor:** [Silent Strike Arsenal (SSA)](https://www.intercuba.net/silent-strike-arsenal-1) by Intercuba.net is the next-generation successor to this toolkit, rebuilt from the ground up in Python 3 with additional capabilities.

---

## Requirements

- **Python 3.8+**
- Perl (for Nikto, Admin Page Finder)
- Standard Linux/macOS system utilities (`nslookup`, `nmap`, `steghide`, etc.)

### Python Dependencies

```bash
pip3 install requests tweepy feedparser shodan beautifulsoup4 colorama pillow mechanize
```

---

## Installation

```bash
git clone https://github.com/krintoxi/NoobSec-Toolkit.git
cd NoobSec-Toolkit/NoobSecToolkit\ -\ MAC\ OSX/
python3 NSToolkit.py
```

---

## Usage

Launch the main menu:

```bash
python3 NSToolkit.py
```

---

## Toolkit Commands

| Command | Description |
|---|---|
| `sqli` | SQL Injector (SQLMap wrapper) |
| `vulscan` | Web Vulnerability Scanner (Nikto wrapper) |
| `dinfo` | DNS / Domain Information Gathering |
| `apf` | Admin Page Finder (Perl script) |
| `hashtype` | Identify Hash Algorithm Type |
| `hexconv` | Hex Encoder and Decoder |
| `numconv` | Number Base Converter (Decimal ↔ Binary) |
| `dping` | HTTP Stress Test / Flood (authorized use only) |
| `osint` | OSINT Framework (OSCARF) |
| `steghide` | Steghide GUI Launcher |
| `stegattack` | Steghide Dictionary Attack |
| `toolbox` | Extended Toolkit (Web Hacking, Exploitation, etc.) |
| `backdoorssh` | SSH Backdoor Deployment Framework |

### Security / Anonymity (Linux)

| Command | Description |
|---|---|
| `macspoof` | Spoof MAC Address |
| `itor` | Install Tor |
| `stor` | Start Tor |
| `tors` | Check Tor Status |
| `vpn` | Download and Launch Bitmask VPN |
| `encdns` | Encrypt DNS with DNSCrypt |

### General

| Command | Description |
|---|---|
| `clear` | Clear terminal |
| `home` | Reload toolkit |
| `update` | System package update (Linux) |
| `quit` / `exit` | Exit |

---

## OSCARF (OSINT Framework)

The OSINT module provides:

- **Social Networking** — Instagram username checker
- **Shodan** — Search by subnet, hostname, organization, ports (requires API key)
- **Network Info** — IP lookup, port lookup, domain-to-IP resolution
- **Pastebin Scraper** — Keyword-based paste monitoring
- **RSS News Feed** — Keyword-filtered news aggregation

### OSCARF Setup

```bash
pip3 install tweepy twitter feedparser shodan beautifulsoup4 requests
```

For Twitter integration, create `scripts/OSCAR/auth/twitter_app.dat` with your API credentials.

---

## Toolbox

Extended tools launched via the `toolbox` command:

**Information Gathering:**
- nmap, Setoolkit, Port Scanner, Host-to-IP, WordPress User Enumeration, CMS Scanner, XSSTracer, Doork (Google Dorks)

**Password Attacks:**
- Cupp (Password List Generator), Ncrack

**Wireless Testing:**
- Reaver (WPS attack), Pixiewps (Pixie Dust attack), Bluetooth Honeypot (BluePot)

**Exploitation:**
- Venom (Shellcode Generator), SQLMap, ShellNoob, Commix, jboss-autopwn, bsqlbf (Blind SQL)

**Web Hacking:**
- Drupal exploitation, WordPress/Joomla scanners, Gravity Forms scanner, File Upload checker, WordPress exploit scanner, plugin scanner, shell/directory finder, Joomla RCE, BruteX, Arachni scanner

**Sniffing & Spoofing:**
- Setoolkit, SSLstrip, pyPISHER, SMTP Mailer

**Post Exploitation:**
- POET (Post-Exploitation Tool), Weeman (Phishing Framework)

**Smartphones:**
- Smartphone Pentest Framework (SPF), Drozer, Android PIN Cracker

---

## Bundled Tools

| Tool | Purpose | Source |
|---|---|---|
| SQLMap | SQL Injection Testing | `tools/inject/` |
| Nikto | Web Vulnerability Scanner | `tools/vscan/` |

---

## Legal Disclaimer

This toolkit is intended for **authorized penetration testing, CTF competitions, and educational use only**.

**Do not use against systems you do not own or have explicit written permission to test.** Unauthorized use is illegal and unethical. The authors assume no liability for misuse.

---

## Credits

- **SQLMap** — sqlmapproject
- **Nikto** — sullo
- **OSCARF** — NinjaSl0th (@ninjasl0th)
- **BackdoorMe SSH Framework** — Original contributors
- **Krintoxi** — Original NSToolkit author
- **Intercuba.Net** — Spanish translation and Silent Strike Arsenal
- **ZenOokami** — NumberConverter
- **Zion3R / Blackploit** — Hash Identifier
- **4sec / PTT** — Hex Converter

---

## Links

- GitHub: https://github.com/krintoxi/NoobSec-Toolkit
- Successor (SSA): https://www.intercuba.net/silent-strike-arsenal-1
- Original Author: https://www.cybrary.it/members/leoedge

---

## License

GNU General Public License v2 — see [LICENSE](LICENSE)
