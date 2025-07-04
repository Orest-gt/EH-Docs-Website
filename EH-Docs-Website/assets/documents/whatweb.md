# 🕷️ WhatWeb (Website Fingerprinting Tool)

> **MUST HAVE:**  
> - Εγκατάσταση: `sudo apt install whatweb`  
> - Για **ethical hacking use only** (πάντα με άδεια)

---

## 🛠️ ΒΑΣΙΚΗ ΣΥΝΤΑΞΗ

```bash
whatweb [επιλογές] [URL ή αρχείο με URL]
🔍 ΒΑΣΙΚΗ ΧΡΗΣΗ

whatweb https://example.com               # Βασική σάρωση
whatweb -v https://example.com            # Λεπτομερής σάρωση
whatweb -i targets.txt                    # Μαζική σάρωση από αρχείο
⚙️ ΚΥΡΙΑ FLAGS
Flag	Περιγραφή
-v, --verbose	Εμφάνιση επιπλέον πληροφορίας
--color	Χρωματιστή έξοδος
--no-errors	Αγνόηση σφαλμάτων
--log-verbose=output.txt	Αποθήκευση λεπτομερούς αναφοράς
--user-agent=UA_STRING	Ορισμός custom User-Agent
--timeout=N	Timeout ανά αίτημα (default: 15 sec)
--follow-redirect=when-ok	Ακολουθεί redirects μόνο αν 200 OK
--max-threads=N	Αριθμός ταυτόχρονων νημάτων (default: 25)
--quiet	Σιωπηλή λειτουργία (χωρίς banners/logs)

🧠 ΣΥΝΗΘΗ ΠΑΡΑΔΕΙΓΜΑΤΑ

whatweb -v --color https://site.com
whatweb -i urls.txt --log-verbose=scan.txt
whatweb --no-errors -v --user-agent "Mozilla/5.0" https://target.gr
whatweb -v --max-threads=50 https://example.com
🧪 ADVANCED TRICKS

whatweb -v --aggression=3 https://target.com      # Full scan (1-3)
whatweb --list-plugins                            # Λίστα όλων των plugins
whatweb --plugin-dir=/custom/plugins              # Χρήση custom plugin directory
⚠️ ΠΡΟΣΟΧΗ:
Χρησιμοποίησε το εργαλείο ΜΟΝΟ σε servers που έχεις άδεια να σκανάρεις.
Η μη εξουσιοδοτημένη χρήση είναι παράνομη.