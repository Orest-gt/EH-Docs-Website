# BETTERCAP USAGE (ETHICAL HACKING / PENTESTING)

---

## MUST HAVE:
- bettercap installed:  
  ```bash
  sudo apt install bettercap
Run as root:

sudo bettercap
Only use on networks you own/have permission to test!

1. BASIC STARTUP
Launch interactive mode:

sudo bettercap
Start with a specific network interface (e.g., eth0, wlan0):

sudo bettercap --iface <interface>
# or
sudo bettercap -I <interface>
2. NETWORK DISCOVERY
Scan the network for hosts:

net.probe on
net.show
3. MITM (Man-in-the-Middle)
ARP Spoofing
(Redirect traffic through your machine)

set arp.spoof.targets <target_IP>
arp.spoof on
DNS Spoofing
(Redirect DNS queries)

set dns.spoof.domains <domain_to_spoof>
set dns.spoof.address <fake_IP>
dns.spoof on
4. TRAFFIC SNIFFING
Monitor HTTP traffic (plaintext passwords, cookies):

net.sniff on
Filter sniffed traffic (e.g., for credentials):

set net.sniff.local true
set net.sniff.filter "tcp port 80 or tcp port 443"
5. CREDENTIAL HARVESTING
Enable HTTP/HTTPS sniffing for logins:

net.sniff on
6. DEFENSIVE COUNTERMEASURES
Stop all attacks:

arp.spoof off
dns.spoof off
net.sniff off
7. MODULES
Load modules (e.g., WiFi, HID attacks):

Αντιγραφή κώδικα
wifi.recon on
hid.probe
WARNING
Use ONLY on authorized networks.

ARP/DNS spoofing is ILLEGAL without permission.

Bettercap logs all actions; maintain ethical transparency.