# === HYDRA (BRUTE-FORCE TOOL - ETHICAL USE ONLY) ===

---

## 🛠️ MUST HAVE:
- Hydra εγκατεστημένο:  
  ```bash
  sudo apt install hydra
Wordlists (π.χ. rockyou.txt)

⚖️ LEGAL USE: Μόνο για συστήματα που σου ανήκουν ή έχεις άδεια να ελέγξεις.

1. 🚀 BASIC USAGE
Brute-force SSH:


hydra -l <username> -P <wordlist.txt> <target_IP> ssh
Brute-force FTP:


hydra -l <username> -P <wordlist.txt> <target_IP> ftp
2. ⚙️ COMMON FLAGS
Flag	Περιγραφή
-s <port>	Καθορισμός port
-f	Σταματάει όταν βρει το πρώτο valid password
-v	Verbose mode – δείχνει προσπάθειες

3. 🎯 ATTACK MODES
Username list + password list:


hydra -L <userlist.txt> -P <wordlist.txt> <target_IP> <protocol>
Single username + password list (π.χ. για web login):

hydra -l admin -P <wordlist.txt> <target_IP> http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
4. 🛡️ DEFENSIVE COUNTERMEASURES
Πώς να προστατευτείς από Hydra:

🔐 Κλείδωμα λογαριασμού μετά από Χ αποτυχημένες προσπάθειες.

🤖 Ενεργοποίηση CAPTCHA ή 2FA.

📈 Παρακολούθηση logs για επαναλαμβανόμενα login attempts.

⚠️ WARNING
❌ Η μη εξουσιοδοτημένη χρήση είναι παράνομη.

✅ Επιτρέπεται μόνο σε εργαστήρια/δοκιμές με άδεια: HTB, TryHackMe, προσωπικά VMs κ.λπ.