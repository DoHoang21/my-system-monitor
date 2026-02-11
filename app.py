from flask import Flask, render_template, jsonify
import psutil
import platform
import time
import os

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def index():
    # 1. Thông tin cấu hình hệ thống Cloud (Static Info)
    sys_info = {
        "node": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "cpu_type": platform.processor() or "Cloud-optimized Processor",
        "cores": psutil.cpu_count(logical=True),
        "total_ram": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
    }
    
    # 2. Thư viện tri thức Docker & Cloud (Encyclopedia)
    docker_lib = {
        "Container Life Cycle": [
            {"cmd": "docker build -t app:v1 .", "desc": "Đóng gói ứng dụng từ Dockerfile thành Image."},
            {"cmd": "docker run -d --name myapp -p 80:5000 app:v1", "desc": "Khởi chạy Container với chế độ chạy ngầm và ánh xạ cổng."},
            {"cmd": "docker ps -as", "desc": "Liệt kê các container cùng dung lượng bộ nhớ chiếm dụng."}
        ],
        "Cloud Architecture": [
            {"term": "PaaS (Platform as a Service)", "desc": "Mô hình dịch vụ cho phép triển khai ứng dụng mà không cần quản lý hạ tầng phần cứng."},
            {"term": "Shared Responsibility Model", "desc": "Mô hình trách nhiệm chung giữa nhà cung cấp Cloud (Render/AWS) và người dùng (Sinh viên)."}
        ]
    }
    return render_template('index.html', info=sys_info, library=docker_lib)

@app.route('/api/stats')
def stats():
    # API cung cấp dữ liệu cho biểu đồ Real-time
    net = psutil.net_io_counters()
    uptime = time.time() - start_time
    return jsonify(
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage('/').percent,
        net_in=f"{round(net.bytes_recv / (1024**2), 2)} MB",
        net_out=f"{round(net.bytes_sent / (1024**2), 2)} MB",
        uptime=f"{int(uptime // 60)} phút {int(uptime % 60)} giây"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)