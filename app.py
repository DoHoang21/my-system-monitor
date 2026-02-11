from flask import Flask, render_template, jsonify
import psutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# API này trả về dữ liệu dạng JSON để JavaScript xử lý
@app.route('/api/stats')
def stats():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return jsonify(cpu=cpu, ram=ram, disk=disk)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)