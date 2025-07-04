# 🛡️ Nikto (Web Server Scanner - ETHICAL USE ONLY)

> **MUST HAVE:**  
> - Installed: `sudo apt install nikto`  
> - **LEGAL USE:** Only scan servers you own or have permission to test.

---

## 📦 1. Basic Usage

### 🔍 Scan a target web server:
```bash
nikto -h <target_IP>
📌 Scan with specific port:

nikto -h <target_IP> -p <port>
⚙️ 2. Common Flags
💾 Save results to a file:

nikto -h <target_IP> -o <report.txt>
🔐 Scan for SSL vulnerabilities:

nikto -h <target_IP> -ssl
🗂️ Scan multiple hosts from file:

nikto -h <hosts.txt>
🧪 3. Tuning Options
🚫 Skip false positives:

nikto -h <target_IP> -no404
🕵️‍♂️ Evasion techniques (IDS bypass):

nikto -h <target_IP> -evasion 1
🛡️ 4. Defensive Countermeasures
Protect against Nikto-type vulnerabilities:

🩹 Patch outdated software (e.g., Apache, PHP).

🔒 Disable unnecessary HTTP methods (OPTIONS, TRACE).

🙈 Hide server banners (ServerTokens Prod in Apache).

⚠️ WARNING:

Unauthorized scanning is illegal.

Always obtain written permission before testing.