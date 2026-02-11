from flask import Flask, render_template, jsonify
import psutil
import platform
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Thư viện lệnh Docker được phân loại chuyên nghiệp
    docker_library = {
        "Cơ bản": [
            {"cmd": "docker --version", "desc": "Kiểm tra phiên bản Docker đã cài đặt"},
            {"cmd": "docker pull [image]", "desc": "Tải một Image từ Docker Hub về máy chủ Cloud"}
        ],
        "Vận hành": [
            {"cmd": "docker run -d -p 80:5000 [img]", "desc": "Chạy Container ở chế độ nền và ánh xạ cổng"},
            {"cmd": "docker ps -a", "desc": "Liệt kê tất cả Container (đang chạy và đã dừng)"},
            {"cmd": "docker logs --tail 50 [id]", "desc": "Xem 50 dòng nhật ký mới nhất của Container"}
        ],
        "Dọn dẹp": [
            {"cmd": "docker system prune", "desc": "Xóa toàn bộ tài nguyên thừa (Image, Container rác)"},
            {"cmd": "docker stop $(docker ps -q)", "desc": "Dừng tất cả các Container đang hoạt động"}
        ]
    }
    return render_template('index.html', library=docker_library)

@app.route('/api/stats')
def stats():
    return jsonify(
        cpu=psutil.cpu_percent(interval=None),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage('/').percent
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)