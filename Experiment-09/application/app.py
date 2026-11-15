from flask import Flask, jsonify, request
import os
import platform
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    uptime = round(time.time() - start_time, 2)
    return jsonify({
        "status": "success",
        "experiment": "Experiment 09 - Custom Dockerfile & Image Build",
        "student": "Nithyashree D S",
        "institution": "The National Institute of Engineering, Mysuru",
        "hostname": platform.node(),
        "os_platform": platform.platform(),
        "python_version": platform.python_version(),
        "uptime_seconds": uptime,
        "message": "Custom Docker container built and executed successfully!"
    })

@app.route('/health')
def health():
    return jsonify({"status": "UP", "timestamp": time.time()}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
