import os
import sys
from flask import Flask, render_template, request
from app.recon_gather import gather_osint
from app.ai_analyzer import analyze_with_ai

# ✅ Fix template path manually
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        domain = request.form['domain']
        osint_data = gather_osint(domain)
        real_ip, confidence = analyze_with_ai(osint_data)
        result = {
            'domain': domain,
            'real_ip': real_ip,
            'confidence': confidence,
            'details': osint_data
        }
    return render_template('index.html', result=result)
