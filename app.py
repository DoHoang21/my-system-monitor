from flask import Flask, render_template, jsonify
import psutil
import platform
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Thông tin cấu hình cố định của máy chủ Cloud
    sys_info = {
        "os": f"{platform.system()} {platform.release()}",
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=True),
        "total_ram": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
    }
    return render_template('index.html', info=sys_info)

@app.route('/api/stats')
def stats():
    # Thông tin thay đổi theo thời gian thực
    net_io = psutil.net_io_counters()
    return jsonify(
        cpu=psutil.cpu_percent(interval=None),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage('/').percent,
        boot_time=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        net_sent=f"{round(net_io.bytes_sent / (1024**2), 2)} MB",
        net_recv=f"{round(net_io.bytes_recv / (1024**2), 2)} MB",
        process_count=len(psutil.pids())
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)