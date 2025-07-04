# 🔎 Nmap Cheat Sheet (Pentesting/CTF Edition)

> **⚠️ Reminder:**  
> Χρησιμοποίησε το Nmap **μόνο σε εξουσιοδοτημένα δίκτυα** (CTF, labs, HTB, TryHackMe, κ.λπ.).

---

## 🚀 Βασική Σύνταξη

```bash
nmap <target>
nmap 10.10.10.10
nmap 10.10.10.0/24
⚙️ Συχνές Επιλογές
Επιλογή	Περιγραφή
-sS	SYN (stealth) scan (default ως root)
-sT	TCP connect scan (για μη root)
-sU	UDP scan
-sV	Version detection
-sC	Εκτέλεση default scripts
-A	All-in-one: OS detection, scripts, κλπ
-O	OS detection
-Pn	Χωρίς ping (scan ακόμη και αν δεν απαντάει σε ping)
-p	Καθορισμός ports (π.χ. -p 22,80,443)
-p-	Όλοι οι 65535 TCP ports
-T<0-5>	Ταχύτητα scan (T4 = γρήγορο, T5 = επιθετικό)

🧪 Χρήσιμα Παραδείγματα
🎯 Basic Scan

nmap -sS -p 22,80 10.10.10.10
🎯 Full TCP Port Scan

nmap -sS -p- 10.10.10.10
🎯 Aggressive Scan (γρήγορο recon)

nmap -A -T4 10.10.10.10
🎯 Version & Default Scripts

nmap -sC -sV 10.10.10.10
🎯 UDP Scan (προσοχή: αργό!)

nmap -sU -p 53,161 10.10.10.10
🎯 Χωρίς Ping

nmap -Pn 10.10.10.10
📄 Εξαγωγή Αποτελεσμάτων
Format	Παράδειγμα
Normal	-oN result.txt
XML	-oX result.xml
Grepable	-oG result.grep
All	-oA scan → scan.nmap, scan.xml, scan.gnmap

nmap -sC -sV -oN myscan.txt 10.10.10.10
🔬 Script Engine (NSE)
Χρήση συγκεκριμένου NSE script:

nmap --script http-title -p 80 10.10.10.10
Αναζήτηση script:

ls /usr/share/nmap/scripts | grep ftp
Run category of scripts:

nmap --script vuln 10.10.10.10
💡 Pro Tips
Χρησιμοποίησε το -oA για εύκολη μελλοντική αναφορά.

-sC -sV είναι το απόλυτο recon combo για TryHackMe & HTB.

Πάντα κάνε -p- σε άγνωστα μηχανήματα (πολλά flags σε μη default ports).

Μπορείς να κάνεις UDP+TCP scan μαζί:

nmap -sS -sU -p T:1-1000,U:53,161 10.10.10.10
🔥 Για ακόμα καλύτερη αυτοματοποίηση, δες τα εργαλεία: rustscan, masscan, autorecon, nmapAutomator.