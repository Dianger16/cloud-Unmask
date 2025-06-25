import socket
import requests
import dns.resolver
import whois
from app.utils import run_traceroute, geoip_lookup

def get_dns_records(domain):
    records = {}
    try:
        records['A'] = [r.address for r in dns.resolver.resolve(domain, 'A')]
    except:
        records['A'] = []
    try:
        records['CNAME'] = [r.to_text() for r in dns.resolver.resolve(domain, 'CNAME')]
    except:
        records['CNAME'] = []
    try:
        records['NS'] = [r.to_text() for r in dns.resolver.resolve(domain, 'NS')]
    except:
        records['NS'] = []
    return records

def get_crtsh_certificates(domain):
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            certs = list(set([entry['name_value'] for entry in data]))
            return certs
    except:
        pass
    return []

def get_ip_from_socket(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            'registrar': w.registrar,
            'creation_date': str(w.creation_date),
            'expiration_date': str(w.expiration_date),
            'name_servers': w.name_servers
        }
    except:
        return {}

def detect_cdn_provider(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=10)
        headers = response.headers
        server = headers.get("Server", "").lower()
        cdn_keywords = {
            "cloudflare": "Cloudflare",
            "akamai": "Akamai",
            "fastly": "Fastly",
            "sucuri": "Sucuri",
            "cloudfront": "AWS CloudFront"
        }

        for keyword in cdn_keywords:
            if keyword in server:
                return cdn_keywords[keyword]

        if "cf-ray" in headers or "cf-cache-status" in headers:
            return "Cloudflare"

        return "None Detected"
    except:
        return "Detection Failed"

def gather_osint(domain):
    traceroute_hops = run_traceroute(domain)
    geo_info = {ip: geoip_lookup(ip) for ip in traceroute_hops}
    return {
        'ip_from_socket': get_ip_from_socket(domain),
        'dns_records': get_dns_records(domain),
        'ssl_cert_domains': get_crtsh_certificates(domain),
        'whois': get_whois_info(domain),
        'cdn_provider': detect_cdn_provider(domain),
        'traceroute': traceroute_hops,
        'geo_trace': geo_info
    }
