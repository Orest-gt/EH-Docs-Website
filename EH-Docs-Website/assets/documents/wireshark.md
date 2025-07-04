# 🧪 WIRESHARK (Ethical Network Analysis Guide)

> ⚠️ **MUST HAVE:**  
> - Εγκατάσταση: `sudo apt install wireshark`  
> - Εκκίνηση με πλήρη δικαιώματα: `sudo wireshark`  
> - **Αναλύεις ΜΟΝΟ traffic που έχεις εξουσιοδότηση!**

---

## 1️⃣ ΒΑΣΙΚΗ ΧΡΗΣΗ

🔹 **Έναρξη καταγραφής:**
- Άνοιξε Wireshark → Επίλεξε διεπαφή → Πάτα "Start"
- CLI (tshark):

```bash
sudo tshark -i <interface>
🔹 Φίλτρα:


ip.addr == <target_IP>         # Φιλτράρισμα IP
http || dns                    # Πρωτόκολλα HTTP ή DNS
2️⃣ ΧΡΗΣΙΜΑ ΦΙΛΤΡΑ
Ενέργεια	Φίλτρο
HTTP αιτήματα (GET/POST)	http.request
Εύρεση credentials (σε POST)	http.request.method == "POST"
DNS αιτήματα	dns
TCP/UDP ανά port	tcp.port == <port> / udp.port == <port>

3️⃣ CAPTURE TRAFFIC ΣΕ HOST(S)
🔹 Απλό capture:

host <target_IP>
🔹 Ανάμεσα σε 2 hosts:


ip.src == <IP1> && ip.dst == <IP2>
4️⃣ ΕΞΑΓΩΓΗ ΔΕΔΟΜΕΝΩΝ
🔹 Αποθήκευση πακέτων:

GUI: File → Save As...

🔹 Εξαγωγή αντικειμένων (π.χ. HTTP):

File → Export Objects → HTTP

5️⃣ ΕΝΤΟΠΙΣΜΟΣ ΕΠΙΘΕΣΕΩΝ
Τύπος Επίθεσης	Φίλτρο
ARP spoofing	arp.duplicate-address-detected
TCP SYN flood	tcp.flags.syn == 1 && tcp.flags.ack == 0

6️⃣ ΑΜΥΝΑ & ΠΡΟΛΗΨΗ
✅ Τρόποι προστασίας από sniffer tools:

➤ Πάντα HTTPS, ποτέ απλό HTTP

➤ Χρήση SSH, TLS, VPNs για κρυπτογράφηση

➤ Παρακολούθηση ARP tables για ύποπτες εγγραφές

⚠️ ΝΟΜΙΚΗ ΠΡΟΕΙΔΟΠΟΙΗΣΗ
📛 Η ανάλυση πακέτων χωρίς εξουσιοδότηση μπορεί να είναι παράνομη.
✅ Ζήτα άδεια ΠΡΙΝ αναλύσεις οποιοδήποτε δίκτυο.