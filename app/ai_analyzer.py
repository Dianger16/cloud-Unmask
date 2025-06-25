def analyze_with_ai(osint_data):
    probable_ip = osint_data['ip_from_socket']
    confidence = 60

    if osint_data['dns_records']['A']:
        confidence += 20
    if osint_data['ssl_cert_domains']:
        confidence += 10
    if osint_data['cdn_provider'] == "None Detected":
        confidence += 10

    return probable_ip, min(confidence, 99)
