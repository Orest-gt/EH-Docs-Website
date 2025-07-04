# BURP SUITE CHEAT SHEET

---

## [❗] Ξεκίνα πάντα:
- Ρύθμισε τον browser να περνάει μέσω του Burp Proxy (`127.0.0.1:8080`)
- Ενεργοποίησε το Intercept ON μόνο όταν θες να "πιάσεις" requests

---

## [💥] MODULES OVERVIEW

1. **Proxy**  
   - Intercept requests/responses  
   - Modify live traffic  
   - Forward or drop requests  

2. **Repeater**  
   - Στέλνεις επαναλαμβανόμενα modified requests  
   - Ιδανικό για SQLi, XSS testing, logic flaws  

3. **Intruder**  
   - Brute force / fuzzing / injection automation  
   - Position markers: `§word§`  
   - Payloads: dictionary, numbers, chars, custom  

4. **Decoder**  
   - Encode/decode: Base64, URL, HTML, Hex, κλπ  

5. **Comparer**  
   - Σύγκριση responses ή request blobs  

6. **Scanner (Pro only)**  
   - Αυτόματο vulnerability scanner  

---

## [🔥] BURP INTRUDER EXAMPLES

- **Brute force login (password field):**  
  - Set `§username§` and `§password§`  
  - Payload list: `common-passwords.txt`  

- **Fuzzing params:**  
  - URL: `/search.php?q=§value§`  
  - Payloads: `'; --`, `<script>`, `../`, κλπ  

---

## [🎯] TRICKS & TIPS

- ✔ Intercept request → Send to Repeater (`Ctrl + R`)  
- ✔ Change User-Agent / Cookie headers για bypass  
- ✔ Χρήση Proxy history για παρακολούθηση όλων των αιτήσεων  
- ✔ Add match & replace rules για automation  

---

## [🧪] TESTING FOR VULNS

- **SQLi:**  
  `' OR '1'='1`, `' UNION SELECT`, `'--`  
- **XSS:**  
  `<script>alert(1)</script>`, `"><svg/onload=alert(1)>`  
- **LFI:**  
  `../../../../etc/passwd`, `%2e%2e%2f`  
- **Command Injection:**  
  `;id`, `|whoami`, `&& ls`  

---

## [⚙️] COMMON HEADERS

- User-Agent  
- Cookie  
- Host  
- Referer  
- X-Forwarded-For  

---

## [📦] EXPORT

- Save requests/responses to file  
- Export project for future analysis  

---
