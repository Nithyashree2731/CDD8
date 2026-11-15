from flask import Flask, render_template_string, jsonify, request
import os
import platform

app = Flask(__name__)

STUDENTS_DB = [
    {"usn": "4NI23CS001", "name": "Aditi Sharma", "sub1": 88, "sub2": 92, "sub3": 85, "gpa": 9.1, "grade": "S"},
    {"usn": "4NI23CS045", "name": "Nithyashree D S", "sub1": 95, "sub2": 98, "sub3": 94, "gpa": 9.8, "grade": "S+"},
    {"usn": "4NI23CS082", "name": "Rahul Verma", "sub1": 78, "sub2": 82, "sub3": 75, "gpa": 8.0, "grade": "A"},
    {"usn": "4NI23CS110", "name": "Sneha Patil", "sub1": 84, "sub2": 89, "sub3": 91, "gpa": 8.8, "grade": "A+"}
]

HTML_VIEW = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOps Lab Exp-11 | Python Academic Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 30px; }
        .container { max-width: 800px; margin: auto; background: #1e293b; padding: 30px; border-radius: 12px; border: 1px solid #334155; }
        h1 { color: #38bdf8; font-size: 24px; margin-bottom: 6px; }
        .sub { color: #94a3b8; font-size: 14px; margin-bottom: 24px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #334155; font-size: 14px; }
        th { background: #0f172a; color: #94a3b8; text-transform: uppercase; font-size: 12px; }
        .highlight { color: #34d399; font-weight: bold; }
        .badge { background: #38bdf8; color: #0f172a; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; }
        .meta { margin-top: 25px; padding: 15px; background: #0f172a; border-radius: 8px; border-left: 4px solid #38bdf8; font-size: 13px; color: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Academic Performance & Grade Analytics System</h1>
        <div class="sub">Experiment 11: Containerized Python Microservice | Department of CSE, NIE Mysuru</div>
        
        <table>
            <thead>
                <tr>
                    <th>USN</th>
                    <th>Student Name</th>
                    <th>DevOps</th>
                    <th>Cloud</th>
                    <th>AI/ML</th>
                    <th>CGPA</th>
                    <th>Grade</th>
                </tr>
            </thead>
            <tbody>
                {% for s in students %}
                <tr>
                    <td style="font-family:monospace;">{{ s.usn }}</td>
                    <td><strong>{{ s.name }}</strong></td>
                    <td>{{ s.sub1 }}</td>
                    <td>{{ s.sub2 }}</td>
                    <td>{{ s.sub3 }}</td>
                    <td class="highlight">{{ s.gpa }}</td>
                    <td><span class="badge">{{ s.grade }}</span></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <div class="meta">
            <div><strong>Host Container ID:</strong> {{ hostname }}</div>
            <div><strong>Runtime Engine:</strong> Python {{ py_ver }} on Alpine Linux (Containerized)</div>
            <div><strong>Port Mapping:</strong> Host 5050 &rarr; Container 5050</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        HTML_VIEW,
        students=STUDENTS_DB,
        hostname=platform.node(),
        py_ver=platform.python_version()
    )

@app.route('/api/students')
def get_students():
    return jsonify({
        "experiment": "Experiment 11",
        "records_count": len(STUDENTS_DB),
        "students": STUDENTS_DB
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
