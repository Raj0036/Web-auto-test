
from flask import Flask, render_template_string, send_from_directory
import glob, os
app = Flask(__name__)
TEMPLATE = """
<!doctype html>
<title>AAS Dashboard</title>
<h1>Adaptive Attack Simulator - Reports</h1>
<ul>
{% for f in files %}
<li><a href="/reports/{{f}}">{{f}}</a></li>
{% endfor %}
</ul>
"""
@app.route('/')
def index():
    files = [os.path.basename(f) for f in glob.glob('reports/*.md')]
    return render_template_string(TEMPLATE, files=files)
@app.route('/reports/<path:n>')
def rfile(n):
    return send_from_directory('reports', n)
if __name__ == '__main__':
    app.run(debug=True)
