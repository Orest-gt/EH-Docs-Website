# Gobuster Cheat Sheet

---

## ΒΑΣΙΚΗ ΣΥΝΤΑΞΗ:
```bash
gobuster dir -u URL -w WORDLIST
ΠΑΡΑΔΕΙΓΜΑ:

gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt
ΧΡΗΣΙΜΕΣ ΣΗΜΑΙΕΣ:
Σημαία	Περιγραφή
-u	URL στόχου
-w	Wordlist που χρησιμοποιείται
-k	Αγνόησε SSL Certificate Errors
-x php,txt,bak	Επεκτάσεις αρχείων
-t 50	Threads (για ταχύτητα)
-s 200,204,301,302	Συγκεκριμένα status codes
-e	Βάζει / στο τέλος για directories
-r	Αγνοεί redirects
-o results.txt	Αποθηκεύει τα αποτελέσματα
--no-error	Κρύβει errors

FULL ΠΑΡΑΔΕΙΓΜΑ:

gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt -x php,txt,bak -t 50 -e -o gobuster_results.txt
VHOST ENUMERATION:


gobuster vhost -u http://TARGET_IP -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt
DNS SUBDOMAIN ENUM:

gobuster dns -d domain.com -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt
EXTRA:
Proxy μέσω Burp:


gobuster dir -u http://target -w wordlist --proxy http://127.0.0.1:8080
Wordlists:
/usr/share/wordlists/dirb/common.txt

/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

/usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt

TIP:
Αν βλέπεις μόνο 403/404, δοκίμασε άλλη wordlist ή άλλη επέκταση (-x).