# Telegram Sorgu Botu

Bu repo, çeşitli sorgu API'leriyle çalışan bir Telegram botu içerir.

## Kurulum

1. Bot tokenini `sorgubot.py` dosyasına ekle.
2. Gereksinimleri yükle:
    ```bash
    pip install -r requirements.txt
    ```

3. Botu çalıştır:
    ```bash
    python sorgubot.py
    ```

## Docker ile Çalıştırma

```bash
docker build -t sorgubot .
docker run -d --name sorgubot sorgubot
