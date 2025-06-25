import subprocess
from ipwhois import IPWhois
from geopy.geocoders import Nominatim

def run_traceroute(domain):
    try:
        result = subprocess.run(["tracert", "-d", domain], capture_output=True, text=True, timeout=30)
        hops = []
        for line in result.stdout.splitlines():
            if "ms" in line:
                parts = line.strip().split()
                for part in parts:
                    if part.count('.') == 3:
                        hops.append(part)
                        break
        return hops
    except:
        return []

def geoip_lookup(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        loc = res['network'].get('country', 'Unknown')
        return loc
    except:
        return "Unknown"
