from flask import Flask, render_template_string, jsonify
import redis
import os
import platform
import time

app = Flask(__name__)

# Redis configuration from environment variables
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis-backend')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))

# Initialize Redis connection pool
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True, socket_connect_timeout=2)
except Exception as e:
    r = None

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Lab Exp-10 | Multi-Container Compose</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; display: flex; justify-content: center; }
        .card { background: #1e293b; border-radius: 12px; border: 1px solid #334155; padding: 32px; max-width: 650px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { color: #38bdf8; font-size: 24px; margin-bottom: 6px; }
        .badge { background: #3b82f6; color: white; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: bold; }
        .metric-box { background: #0f172a; border: 1px solid #38bdf8; border-radius: 8px; padding: 20px; text-align: center; margin: 24px 0; }
        .metric-num { font-size: 48px; font-weight: 800; color: #38bdf8; }
        .metric-label { font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }
        .info-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #334155; font-size: 14px; }
        .label { color: #94a3b8; font-weight: 600; }
        .val { color: #e2e8f0; font-family: monospace; }
        .status-ok { color: #34d399; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">Experiment 10 • Docker Compose</span>
        <h1>Multi-Container Web Application</h1>
        <p style="color:#94a3b8; font-size:14px; margin-bottom:20px;">Frontend Flask + Backend Redis In-Memory Data Store</p>
        
        <div class="metric-box">
            <div class="metric-num">{{ counter }}</div>
            <div class="metric-label">Total Container Page Hits Recorded in Redis</div>
        </div>

        <div class="info-row"><span class="label">Student Name:</span><span class="val">Nithyashree D S</span></div>
        <div class="info-row"><span class="label">College:</span><span class="val">The National Institute of Engineering, Mysuru</span></div>
        <div class="info-row"><span class="label">Frontend Service:</span><span class="val">{{ hostname }} (Port 8000:5000)</span></div>
        <div class="info-row"><span class="label">Backend Redis Host:</span><span class="val">{{ redis_host }}:{{ redis_port }}</span></div>
        <div class="info-row"><span class="label">Bridge Network:</span><span class="val">devops-lab-network</span></div>
        <div class="info-row"><span class="label">Service Link Status:</span><span class="val status-ok">● Connected & Synchronized</span></div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        count = r.incr('page_views')
    except Exception as e:
        count = f"Redis Error: {e}"
        
    return render_template_string(
        HTML_TEMPLATE,
        counter=count,
        hostname=platform.node(),
        redis_host=REDIS_HOST,
        redis_port=REDIS_PORT
    )

@app.route('/health')
def health():
    try:
        r.ping()
        redis_ok = True
    except Exception:
        redis_ok = False
    return jsonify({"frontend": "UP", "redis": "UP" if redis_ok else "DOWN"}), (200 if redis_ok else 503)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
