from flask import Flask, render_template, jsonify
import psutil
import platform
import time
import os

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def index():
    # 1. Thông tin cấu hình hệ thống
    sys_info = {
        "node": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "cpu_count": psutil.cpu_count(logical=True),
        "total_ram": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    }
    
    # 2. Thư viện lệnh Docker (Nội dung "To" hơn cho web)
    docker_lib = {
        "Container": [
            {"cmd": "docker ps -a", "desc": "Liệt kê tất cả container"},
            {"cmd": "docker exec -it [id] /bin/bash", "desc": "Truy cập terminal của container"}
        ],
        "Images": [
            {"cmd": "docker build -t [tag] .", "desc": "Build image từ Dockerfile"},
            {"cmd": "docker images", "desc": "Xem danh sách các image"}
        ],
        "Network/Volume": [
            {"cmd": "docker network ls", "desc": "Xem các mạng Docker"},
            {"cmd": "docker volume prune", "desc": "Xóa toàn bộ volume dư thừa"}
        ]
    }
    return render_template('index.html', info=sys_info, library=docker_lib)

@app.route('/api/stats')
def stats():
    net = psutil.net_io_counters()
    uptime = int(time.time() - START_TIME)
    return jsonify(
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory().percent,
        net_in=f"{round(net.bytes_recv / (1024**2), 2)} MB",
        net_out=f"{round(net.bytes_sent / (1024**2), 2)} MB",
        uptime=f"{uptime // 60}m {uptime % 60}s"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)