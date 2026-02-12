# Bước 1: Sử dụng hình ảnh Python siêu nhẹ
FROM python:3.9-slim

# Bước 2: Thiết lập thư mục làm việc trong Container
WORKDIR /app

# Bước 3: Copy file danh sách thư viện và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bước 4: Copy toàn bộ mã nguồn vào Container
COPY . .

# Bước 5: Khai báo cổng ứng dụng
EXPOSE 5000

# Bước 6: Lệnh chạy ứng dụng
CMD ["python", "app.py"]