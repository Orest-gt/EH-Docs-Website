# === JOHN THE RIPPER (PASSWORD CRACKING TOOL - ETHICAL USE ONLY) ===

---

## 🧠 ΤΡΟΠΟΙ ΕΠΙΘΕΣΗΣ (MODES)

- `--single`  
  ➤ "Single crack" mode: κάνει educated guesses από shadow/passwd info.

- `--wordlist=FILE`  
  ➤ Dictionary attack με λέξεις από αρχείο.

- `--stdin`  
  ➤ Διαβάζει τις λέξεις από την είσοδο (όχι από αρχείο).

- `--rules`  
  ➤ Εφαρμόζει κανόνες μετατροπής λέξεων (π.χ. password → P@ssw0rd).

---

## 🧪 ΠΡΟΗΓΜΕΝΕΣ ΜΕΘΟΔΟΙ

- `--incremental[=MODE]`  
  ➤ Brute-force με όλους τους συνδυασμούς. MODE = All, Digits, Alpha, κ.ά.

- `--external=MODE`  
  ➤ Custom cracking λογική μέσω scripts.

---

## 📤 ΕΞΑΓΩΓΗ / ΠΡΟΒΟΛΗ

- `--stdout[=LENGTH]`  
  ➤ Εμφανίζει δοκιμαζόμενες λέξεις χωρίς cracking.

- `--show`  
  ➤ Δείχνει τους ήδη βρεθέντες (cracked) κωδικούς.

---

## 🔁 ΔΙΑΧΕΙΡΙΣΗ ΣΥΝΕΔΡΙΩΝ

- `--session=NAME`  
  ➤ Ορίζει νέα cracking συνεδρία.

- `--restore[=NAME]`  
  ➤ Επαναφέρει συνεδρία από checkpoint.

- `--status[=NAME]`  
  ➤ Προβολή προόδου συνεδρίας.

---

## 🧪 BENCHMARK / ΔΟΚΙΜΗ

- `--test[=SECONDS]`  
  ➤ Εκτελεί benchmark για τον καθορισμένο χρόνο.

---

## 🎯 ΦΙΛΤΡΑΡΙΣΜΑ ΣΤΟΧΩΝ

- `--users=LOGIN` ή `--users=UID`  
  ➤ Επιλογή/αποκλεισμός συγκεκριμένων χρηστών.

- `--groups=GID`  
  ➤ Επιλογή συγκεκριμένων ομάδων.

- `--shells=SHELL`  
  ➤ Επιλογή χρηστών με συγκεκριμένο shell (π.χ. /bin/bash).

- `--salts=N`  
  ➤ Hashes με τουλάχιστον (ή λιγότερους με `-`) N users.

---

## 💾 ΡΥΘΜΙΣΕΙΣ ΠΟΡΩΝ

- `--save-memory=1|2|3`  
  ➤ Εξοικονόμηση RAM με μικρότερο performance.

- `--fork=N`  
  ➤ Τρέχει N παράλληλες διεργασίες (για πολυπύρηνα CPUs).

- `--node=MIN[-MAX]/TOTAL`  
  ➤ Κατανομή cracking σε πολλά συστήματα (distributed).

---

## 🔧 ΔΙΑΦΟΡΑ

- `--make-charset=FILE`  
  ➤ Δημιουργία custom charset (αντικαθιστά το FILE).

- `--format=NAME`  
  ➤ Ορίζει hash format (π.χ. md5crypt, bcrypt, NT, sha512crypt, κ.λπ.).

---

## ⚠️ WARNING
- ❌ Παράνομο αν χρησιμοποιηθεί χωρίς άδεια.
- ✅ Χρήση ΜΟΝΟ σε περιβάλλοντα που σου ανήκουν ή με ρητή άδεια (π.χ. TryHackMe, HTB, lab VMs).

---
