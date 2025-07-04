# 🧠 AMASS CHEAT SHEET για Ethical Hacking

## 1. Παθητικό Enumeration (Stealth Recon)
```bash
amass enum -passive -d target.com
Χρήση public sources, χωρίς επαφή με τον στόχο.

2. Ενεργό Enumeration

amass enum -active -d target.com
Παθητικό + brute-force + DNS resolving.

3. Brute-force Subdomains

amass enum -brute -d target.com
Χρήση ενσωματωμένου wordlist για εύρεση subdomains.

4. Custom Wordlist

amass enum -brute -d target.com -w wordlist.txt
Χρήση δικού σου wordlist.

5. Χρήση Συγκεκριμένου DNS Resolver

amass enum -d target.com -r 1.1.1.1,8.8.8.8
Αλλάζει DNS resolver για καλύτερη ή stealth πρόσβαση.

6. Έξοδος σε Αρχεία (JSON + TXT)

amass enum -passive -d target.com -oA output
Δημιουργεί αρχεία: output.txt, output.json, output.gnmap.

7. WHOIS & Domains με intel

amass intel -d target.com
Βρίσκει domains, WHOIS, ASN, κ.ά.

8. Από ASN

amass intel -asn 15169
Βρίσκει domains και IPs από ASN (π.χ. Google).

9. Με Configuration File

amass enum -d target.com -config config.ini
Βάζεις API keys, έξτρα ρυθμίσεις.

10. Συνδυασμός με httpx (ζωντανοί hosts)

amass enum -passive -d target.com | httpx -silent | tee alive.txt
Παθητική ανακάλυψη → Ζωντανοί hosts → Αποθήκευση.

11. Silent Mode (μόνο τα domains)

amass enum -passive -d target.com -silent
Καθαρή έξοδος με μόνο τα subdomains.

12. WHOIS Reverse Lookups

amass intel -whois -d target.com
Επιστρέφει σχετικά domains από WHOIS βάσεις.

13. Μαζικό Recon σε Πολλά Domains

for d in $(cat domains.txt); do amass enum -passive -d $d -o $d.txt; done
Loop για πολλά domains με passive mode.