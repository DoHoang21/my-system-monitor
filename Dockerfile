# Sử dụng Python bản nhẹ
FROM python:3.9-slim

# Tạo thư mục app trong container
WORKDIR /app

# Copy code vào trong container
COPY . .

# Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng 5000
EXPOSE 5000

# Lệnh khởi chạy
CMD ["python", "app.py"]