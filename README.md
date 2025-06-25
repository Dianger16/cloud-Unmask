# 🕵️‍♂️ CloudUnmask

> Reveal the **real IP address** behind cloud-protected servers using **AI + OSINT**.

CloudUnmask is a cybersecurity tool that combines **DNS analysis**, **WHOIS data**,
"SSL subdomain leaks", "traceroute", and "AI-based classification" to unmask origin
 IPs hidden behind CDNs like "Cloudfare"


## ⚙️ Features

- 🌐 Domain-to-IP reconnaissance
- 🔐 SSL subdomain extraction
- 🛰️ Traceroute + Geo-location mapping
- 📄 WHOIS + DNS record lookup
- 🤖 AI model to predict real IP
- 🖥️ Flask web app with clean UI



## 🚀 Run Locally

```bash
git clone https://github.com/Dianger16/CloudUnmask.git
cd CloudUnmask
pip install -r requirements.txt
python app/ui.py
