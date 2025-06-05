<div align="center">
  <img src="https://img.shields.io/github/languages/count/ardaztrk1905/Ag-Guvenligi-Analizi?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/ardaztrk1905/Ag-Guvenligi-Analizi?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/ardaztrk1905/Ag-Guvenligi-Analizi?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/ardaztrk1905/Ag-Guvenligi-Analizi?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

Network security analysis
Ağ Güvenliği Analizi

Analyze the operation of network security detectors (IDS/IPS) used to detect malicious activities (attacks, malware, unauthorized access, etc.) by monitoring traffic within the network. Reveal the weaknesses and strengths of these systems and offer suggestions to create a secure network environment.

Ağın içinde gerçekleşen trafiği izleyerek, kötü niyetli aktiviteleri (saldırılar, kötü amaçlı yazılımlar, yetkisiz erişimler vs.) tespit etmek amacıyla kullanılan ağ güvenliği dedektörlerinin (IDS/IPS) işleyişini analiz etmek. Bu sistemlerin zayıf ve güçlü yönlerini ortaya koymak ve güvenli bir ağ ortamı oluşturmak için öneriler sunmak.

---

## Features / *Özellikler*

- "Port Scanning": Detects common attack types such as port scanning (Nmap), brute force, DoS.
  ""Port Tarama": Port tarama (Nmap), brute force, DoS gibi yaygın saldırı türlerini tespit eder.
  **Traffic Analysis:** Can distinguish between normal and abnormal traffic behavior.
- **Trafik Analizi:** Normal ve anormal trafik davranışlarını ayırt edebilir.  

--

## Team / *Ekip*

- 2320191086 - Arda Öztürk: *Tüm projeyi geliştiren*  

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Makale   |  https://arxiv.org/abs/2004.08967 | IDS ve IPS sistemlerinin genel bir değerlendirmesini sunar, avantajları ve sınırlamaları üzerine odaklanır.
🔗 arXiv:2004.08967 |
| Zeek | https://en.wikipedia.org/wiki/Zeek | Zeek, ağ trafiğini derinlemesine analiz eden ve olayları mantıksal olarak raporlayan güçlü bir araçtır. |
| Snort , Suricata , Zeek ..     |           |

---


1.  https://github.com/ardaztrk1905/Ag-Guvenligi-Analizi

2. /home/kali/ag-guvenligi-projesi/venv/bin/python


3. home/kali/ag-guvenligi-projesi/venv/bin/python
Package         Version
--------------- -----------
appdirs         1.4.4
lxml            5.4.0
numpy           2.2.6
packaging       25.0
pandas          2.3.0
pip             25.1.1
pyshark         0.6
python-dateutil 2.9.0.post0
pytz            2025.2
scapy           2.6.1
six             1.17.0
termcolor       3.1.0
tzdata          2025.2


---

## Usage / *Kullanım*

python aggüvenliği.py --input ornek.pcap --output sonuc.txt


**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1.Bu dosyalar TCP, UDP, ICMP gibi ağ paketlerini içerir
Gerçek ya da test ortamında kaydedilmiş saldırı içeren veya normal trafik verileri olabilir
 sudo tcpdump -i eth0 -w verı.pcap

3. input  veri.pcap	Analiz edilecek ağ verisi (giriş dosyası)
   output sonuc.txt	Tespit edilen tehditlerin ya da analiz özetinin yazılacağı çıktı dosyası
  Çıktıyı kontrol edin 

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
