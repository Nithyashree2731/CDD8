"""
Experiment 08: Simple Python Web Application
A basic Flask web server that displays system information
"""

from flask import Flask
import platform
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    info = {
        'application': 'DevOps Lab - Experiment 08',
        'student': 'Nithyashree D S',
        'university': 'The National Institute of Engineering, Mysuru',
        'hostname': platform.node(),
        'platform': platform.platform(),
        'python_version': platform.python_version(),
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Lab - Experiment 08</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f9; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
            h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            table { width: 100%; border-collapse: collapse; margin-top: 15px; }
            td { padding: 10px; border-bottom: 1px solid #eee; }
            td:first-child { font-weight: bold; color: #555; width: 40%; }
            .footer { margin-top: 20px; text-align: center; color: #888; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Experiment 08: Docker Container Application</h1>
            <table>
    """

    for key, value in info.items():
        html += f"<tr><td>{key.replace('_', ' ').title()}</td><td>{value}</td></tr>"

    html += """
            </table>
            <div class="footer">
                <p>Running inside a Docker Container</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
