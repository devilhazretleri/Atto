FROM python:3.11-slim

# Sistem paketlerini güncelle ve pip'i güncelle
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizini oluştur
WORKDIR /app

# Gereksinim dosyalarını kopyala ve yükle
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Bot dosyasını kopyala
COPY sorgubot.py .

# Default olarak botu başlat
CMD ["python", "sorgubot.py"]
