from flask import Flask, render_template
import psutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Lấy thông số thực tế của server
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    return render_template('index.html', cpu=cpu_percent, ram=ram_percent)

if __name__ == "__main__":
    # Render cấp cổng (Port) tự động qua biến môi trường
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)