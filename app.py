from flask import Flask, render_template, jsonify
import psutil
import platform
import time
import os

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def index():
    # Thư viện kiến thức Docker & Cloud chuyên sâu
    knowledge_base = {
        "Docker Basic": [
            {"cmd": "docker build -t app .", "desc": "Khởi tạo Image từ Dockerfile"},
            {"cmd": "docker run -p 80:5000 app", "desc": "Chạy Container với ánh xạ cổng"},
            {"cmd": "docker ps", "desc": "Xem các Container đang hoạt động"}
        ],
        "Docker Advanced": [
            {"cmd": "docker-compose up -d", "desc": "Triển khai đa dịch vụ (Multi-container)"},
            {"cmd": "docker network inspect bridge", "desc": "Kiểm tra cấu hình mạng nội bộ"},
            {"cmd": "docker volume ls", "desc": "Quản lý dữ liệu bền vững (Persistence)"}
        ],
        "Cloud Knowledge": [
            {"term": "PaaS (Platform as a Service)", "desc": "Render cung cấp môi trường để chạy app mà không cần quản trị OS."},
            {"term": "Virtualization", "desc": "Công nghệ ảo hóa giúp chia sẻ tài nguyên vật lý thành các đơn vị cách ly (Container)."}
        ]
    }
    
    # Thông tin phần cứng máy chủ Cloud
    sys_info = {
        "os": f"{platform.system()} {platform.release()}",
        "cpu": platform.processor() or "Cloud-optimized CPU",
        "cores": psutil.cpu_count(logical=True),
        "ram_total": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
    }
    return render_template('index.html', library=knowledge_base, info=sys_info)

@app.route('/api/stats')
def stats():
    net = psutil.net_io_counters()
    uptime = time.time() - start_time
    return jsonify(
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage('/').percent,
        net_in=f"{round(net.bytes_recv / (1024**2), 2)} MB",
        net_out=f"{round(net.bytes_sent / (1024**2), 2)} MB",
        uptime=f"{int(uptime // 60)} phút"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)