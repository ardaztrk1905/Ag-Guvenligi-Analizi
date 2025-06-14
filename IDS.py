import logging
import re
import time
from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import atexit

# Log ayarları
logging.basicConfig(
    filename="ids_alerts.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# İmza desenleri
signature_patterns = {
    "Nmap Scan": re.compile(r"^.*nmap.*$", re.IGNORECASE),
    "SQL Injection": re.compile(r"^.*(select|drop|union|insert|or 1=1).*", re.IGNORECASE),
}

packet_counter = defaultdict(int)
scan_detected = set()
blacklist = set()

# Saldırı tespiti fonksiyonları
def detect_signature(payload):
    for attack, pattern in signature_patterns.items():
        if pattern.search(payload):
            print(f"[!!] İmza Tespiti: {attack} | İçerik: {payload}")
            logging.warning(f"İmza Tespiti: {attack} | İçerik: {payload}")
            return True
    return False

def analyze_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if TCP in packet or UDP in packet:
            port = packet[TCP].dport if TCP in packet else packet[UDP].dport
            packet_counter[(ip_src, port)] += 1
            if packet_counter[(ip_src, port)] > 10 and ip_src not in scan_detected:
                print(f"[!] Port Taraması Tespit Edildi: {ip_src} => {port}")
                logging.warning(f"Port Taraması Tespit Edildi: {ip_src} => {port}")
                scan_detected.add(ip_src)
                blacklist.add(ip_src)
                with open("blacklist.txt", "a") as f:
                    f.write(f"{ip_src}\n")

        if packet.haslayer(TCP) and hasattr(packet[TCP], 'payload'):
            payload = str(bytes(packet[TCP].payload))
            detect_signature(payload)

        if packet_counter[ip_src] > 100:
            print(f"[!] Olası DoS Saldırısı: {ip_src}")
            logging.warning(f"Olası DoS Saldırısı: {ip_src}")
            blacklist.add(ip_src)
            with open("blacklist.txt", "a") as f:
                f.write(f"{ip_src}\n")

def show_summary():
    print("\n📊 Özet:")
    print(f"- Tespit edilen port tarayıcı IP'ler: {len(scan_detected)}")
    print(f"- Kara listeye alınan IP'ler: {len(blacklist)}")

atexit.register(show_summary)

def start_sniffing():
    iface = input("🔧 İzlemek istediğiniz ağ arayüzü (örnek: eth0, wlan0): ")
    print(f"📡 {iface} arayüzü üzerinden trafik izleniyor... (Ctrl+C ile durdur)")
    sniff(filter="ip", prn=analyze_packet, store=0, iface=iface)

if __name__ == "__main__":
    start_sniffing()
