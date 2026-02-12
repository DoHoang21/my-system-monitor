import os, psutil, platform, time
from flask import Flask, render_template_string

app = Flask(__name__)

# Giao diện HTML chuyên nghiệp tích hợp CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Cloud System Monitor - PTIT Lab</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #eef2f3; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 400px; }
        h1 { color: #d32f2f; font-size: 24px; text-align: center; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .stat-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f9f9f9; }
        .label { font-weight: 600; color: #555; }
        .value { color: #007bff; font-weight: bold; }
        .footer { font-size: 12px; color: #888; text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 System Monitor</h1>
        <div class="stat-item"><span class="label">Nền tảng Cloud:</span> <span class="value">Render (PaaS)</span></div>
        <div class="stat-item"><span class="label">Hệ điều hành:</span> <span class="value">{{ os_info }}</span></div>
        <div class="stat-item"><span class="label">CPU Usage:</span> <span class="value">{{ cpu }}%</span></div>
        <div class="stat-item"><span class="label">RAM Usage:</span> <span class="value">{{ ram }}%</span></div>
        <div class="stat-item"><span class="label">Container ID:</span> <span class="value">{{ node }}</span></div>
        <div class="footer">SV thực hiện: [Tên của bạn] - PTIT 2026</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    os_info = f"{platform.system()} {platform.release()}"
    node = platform.node()
    return render_template_string(HTML_TEMPLATE, cpu=cpu, ram=ram, os_info=os_info, node=node)

if __name__ == '__main__':
    # Render yêu cầu lấy port từ môi trường
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)