import telebot
import requests
import json
import os
import time
import re
from datetime import datetime, timedelta

TOKEN = "6761241273:AAF0Lfahp98O_FHCGr3q1A94ueziB7rm26c"
bot = telebot.TeleBot(TOKEN)

def send_long_message(chat_id, text, parse_mode=None):
    max_len = 4096
    for i in range(0, len(text), max_len):
        bot.send_message(chat_id, text[i:i + max_len], parse_mode=parse_mode)

# Start & Komutlar Menüsü
@bot.message_handler(commands=['start', 'komutlar'])
def start(message):
    komutlar = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
➤ /sorgu - Ad soyad ile bilgi verir
➤ /tc - T.C. numarasından kişi bilgisi verir
➤ /aile - T.C.'den aile bilgisi verir
➤ /sulale - T.C.'den sülale bilgisi verir
➤ /es - T.C.'den eş sorgu
➤ /cocuk - T.C.'den çocuk sorgu
➤ /adres - T.C.'den adres (kısa)
➤ /tcpro - T.C.'den detaylı bilgi
➤ /medeni - Medeni hal sorgu
➤ /iban - IBAN'dan kişi
➤ /gsmtc - GSM’den TC
➤ /tcgsm - TC’den GSM
➤ /operator - GSM’den operatör
➤ /sms - GSM’ye SMS gönder
➤ /arama - Telefona arama gönder
➤ /ip - IP’den konum
➤ /ig - Instagram bilgi
➤ /ses - Metni sese çevir
➤ /index - Site indexi alır
➤ /yaz - Fotoğraf üzerine yazı
"""
    bot.send_message(message.chat.id, komutlar)

# /tc
@bot.message_handler(commands=['tc'])
def tc_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ *TC Kimlik Numarası girin:*\nÖrnek: /tc 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://api.hexnox.pro/sowixapi/tc.php?tc={tc}'
    try:
        resp = requests.get(url)
        result = resp.json()
        if result.get("success") and "data" in result:
            member = result["data"]
            msg = (
                f"TC: {member.get('TC', '-')}\n"
                f"AD: {member.get('AD', '-')}\n"
                f"SOYAD: {member.get('SOYAD', '-')}\n"
                f"BABA ADI: {member.get('BABAADI', '-')}\n"
                f"ANNE ADI: {member.get('ANNEADI', '-')}\n"
                f"DOĞUM YERİ: {member.get('MEMLEKETIL', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "Geçersiz TC numarası veya veri yok.")
    except Exception:
        bot.send_message(chat_id, "API veya bağlantı hatası.")

# /aile
@bot.message_handler(commands=['aile'])
def aile_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ *TC Kimlik Numarası girin:*\nÖrnek: /aile 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://api.hexnox.pro/sowixapi/aile.php?tc={tc}'
    try:
        resp = requests.get(url, timeout=10)
        result = resp.json()
        if not result.get("success") or "data" not in result or not isinstance(result["data"], list):
            bot.send_message(chat_id, "❌ Aile bilgisi bulunamadı.")
            return
        members = result["data"]
        msg = f"👨‍👩‍👧‍👦 Toplam Aile Üyesi: {len(members)}\n"
        for i, m in enumerate(members, 1):
            msg += (
                f"\n{i}. Üye: {m.get('Yakınlık', '-')}\n"
                f"TC: {m.get('TC', '-')}\n"
                f"Ad Soyad: {m.get('AD', '')} {m.get('SOYAD', '')}\n"
                f"Doğum Tarihi: {m.get('DOGUMTARIHI', '-')}\n"
            )
        send_long_message(chat_id, msg)
    except Exception as e:
        bot.send_message(chat_id, f"API bağlantı hatası: {e}")

# /sulale
@bot.message_handler(commands=['sulale'])
def sulale_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ *TC Kimlik Numarası girin:*\nÖrnek: /sulale 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'https://api.hexnox.pro/sowixapi/sulale.php?tc={tc}'
    try:
        resp = requests.get(url, timeout=20)
        result = resp.json()
        # Hem doğrudan liste hem dict-data desteklenir
        if isinstance(result, list) and len(result) > 0:
            members = result
        elif isinstance(result, dict) and "data" in result and isinstance(result["data"], list) and len(result["data"]) > 0:
            members = result["data"]
        else:
            bot.send_message(chat_id, "❌ Sülale bilgisi bulunamadı.")
            return

        # TXT dosyasını oluştur
        txt_content = f"Toplam sülale üyesi: {len(members)}\n\n"
        for m in members:
            txt_content += (
                f"YAKINLIK: {m.get('YAKINLIK', '-')}\n"
                f"TC: {m.get('TC', '-')}\n"
                f"AD: {m.get('AD', '-')}\n"
                f"SOYAD: {m.get('SOYAD', '-')}\n\n"
            )

        # Dosyaya yaz
        file_path = "sulale.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(txt_content)

        # Dosyayı Telegram ile gönder
        with open(file_path, "rb") as f:
            bot.send_document(chat_id, f, caption="Sülale sorgu sonucu")

        # Dosyayı sil
        os.remove(file_path)
    except Exception as e:
        bot.send_message(chat_id, f"Hata oluştu: {e}")
        
# /tcpro
@bot.message_handler(commands=['tcpro'])
def tcpro_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ TC Kimlik Numarası girin:\n/tcpro 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://jessyapiservices.duckdns.org/apiservices/jessytcpro.php?tc={tc}'
    try:
        resp = requests.get(url)
        result = resp.json()
        if result.get("success") and isinstance(result.get("data"), list):
            person = result["data"][0]
            msg = (
                f"TC: {person.get('TC', '-')}\n"
                f"AD: {person.get('AD', '-')}\n"
                f"SOYAD: {person.get('SOYAD', '-')}\n"
                f"GSM: {person.get('GSM', '-')}\n"
                f"BABA ADI: {person.get('BABAADI', '-')}\n"
                f"BABA TC: {person.get('BABATC', '-')}\n"
                f"ANNE ADI: {person.get('ANNEADI', '-')}\n"
                f"ANNE TC: {person.get('ANNETC', '-')}\n"
                f"DOĞUM TARİHİ: {person.get('DOGUMTARIHI', '-')}\n"
                f"ÖLÜM TARİHİ: {person.get('OLUMTARIHI', '-')}\n"
                f"DOĞUM YERİ: {person.get('DOGUMYERI', '-')}\n"
                f"MEMLEKET İL: {person.get('MEMLEKETIL', '-')}\n"
                f"MEMLEKET İLÇE: {person.get('MEMLEKETILCE', '-')}\n"
                f"AİLE SIRA NO: {person.get('AILESIRANO', '-')}\n"
                f"BİREY SIRA NO: {person.get('BIREYSIRANO', '-')}\n"
                f"MEDENİ HAL: {person.get('MEDENIHAL', '-')}\n"
                f"CİNSİYET: {person.get('CINSIYET', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "TC Pro bilgisi bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"API hatası: {e}")

# /medeni
@bot.message_handler(commands=['medeni'])
def medeni_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ TC Kimlik Numarası girin:\n/medeni 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://api.hexnox.pro/sowixapi/medeni.php?tc={tc}'
    try:
        resp = requests.get(url)
        result = resp.json()
        if result.get("success") and "data" in result:
            member = result["data"]
            msg = (
                f"TC: {member.get('TC', '-')}\n"
                f"AD: {member.get('AD', '-')}\n"
                f"SOYAD: {member.get('SOYAD', '-')}\n"
                f"MEDENİ HAL: {member.get('MEDENIHAL', '-')}\n"
                f"EŞİ: {member.get('ESI', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "Medeni hali bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"API hatası: {e}")

# --- /gsmtc --- #
@bot.message_handler(commands=['gsmtc'])
def gsmtc_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir GSM numarası girin.*\nÖrnek: /gsmtc 5553723339", parse_mode="Markdown")
        return
    gsm = args[1]
    url = f'http://api.hexnox.pro/sowixapi/gsmdetay.php?gsm={gsm}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get('success') and data.get('data'):
            m = data['data'][0]
            msg = (
                f"GSM: {m.get('GSM','-')}\n"
                f"TC: {m.get('TC','-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "GSM numarasına ait veri bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"API bağlantı hatası: {e}")

@bot.message_handler(commands=['tcpro'])
def tcpro_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Lütfen bir TC Kimlik Numarası girin!\nÖrnek: /tcpro 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://jessyapiservices.duckdns.org/apiservices/jessytcpro.php?tc={tc}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        result = resp.json()
        if result.get("success") and isinstance(result.get("data"), list):
            person = result["data"][0]
            msg = (
                f"TC: {person.get('TC', '-')}\n"
                f"AD: {person.get('AD', '-')}\n"
                f"SOYAD: {person.get('SOYAD', '-')}\n"
                f"GSM: {person.get('GSM', '-')}\n"
                f"BABA ADI: {person.get('BABAADI', '-')}\n"
                f"BABA TC: {person.get('BABATC', '-')}\n"
                f"ANNE ADI: {person.get('ANNEADI', '-')}\n"
                f"ANNE TC: {person.get('ANNETC', '-')}\n"
                f"DOĞUM TARİHİ: {person.get('DOGUMTARIHI', '-')}\n"
                f"ÖLÜM TARİHİ: {person.get('OLUMTARIHI', '-')}\n"
                f"DOĞUM YERİ: {person.get('DOGUMYERI', '-')}\n"
                f"MEMLEKET İL: {person.get('MEMLEKETIL', '-')}\n"
                f"MEMLEKET İLÇE: {person.get('MEMLEKETILCE', '-')}\n"
                f"AİLE SIRA NO: {person.get('AILESIRANO', '-')}\n"
                f"BİREY SIRA NO: {person.get('BIREYSIRANO', '-')}\n"
                f"MEDENİ HAL: {person.get('MEDENIHAL', '-')}\n"
                f"CİNSİYET: {person.get('CINSIYET', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "TC Pro bilgisi bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"API hatası: {e}")

# --- /tcgsm --- #
@bot.message_handler(commands=['tcgsm'])
def tcgsm_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ *Lütfen Geçerli Bir TC Kimlik Numarası Girin!*\nÖrnek: /tcgsm 11111111110", parse_mode="Markdown")
        return
    tc = args[1]
    url = f'http://api.hexnox.pro/sowixapi/tcgsm.php?tc={tc}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        raw = resp.content.decode('utf-8-sig')
        result = json.loads(raw)
        if isinstance(result, dict) and result.get("success") and isinstance(result.get("data"), list):
            data = result['data']
            msg = f"TC: {tc}\n"
            for entry in data:
                gsm = entry.get('GSM', '-')
                msg += f"GSM: {gsm}\n"
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "TC numarasına ait GSM bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"API hatası: {e}")

# --- /iban --- #
@bot.message_handler(commands=['iban'])
def iban_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "*⚠️ Lütfen Geçerli Bir IBAN Numarası girin!\nÖrnek: /iban TR560001002247786851675002*", parse_mode='Markdown')
        return
    iban = args[1]
    url = f'http://api.hexnox.pro/sowixapi/iban.php?iban={iban}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        result = resp.content.decode('utf-8-sig')
        data = json.loads(result)
        if data:
            banka = data.get('BANKA', {})
            sube = data.get('ŞUBE', {})
            msg = (
                f"Banka: {banka.get('Adı', '-')}\n"
                f"Şube: {sube.get('Ad', '-')}\n"
                f"Adres: {sube.get('Adres', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "IBAN numarası bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"Hata oluştu: {e}")

# --- /adres --- #
@bot.message_handler(commands=['adres'])
def adres_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "*⚠️ Lütfen Geçerli Bir TC Kimlik Numarası Girin!*\nÖrnek: /adres 11111111110", parse_mode='Markdown')
        return
    tc = args[1]
    url = f'http://api.hexnox.pro/sowixapi/adres.php?tc={tc}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        data = resp.content.decode('utf-8-sig')
        member = json.loads(data)
        if member.get("success") and "data" in member:
            m = member["data"]
            msg = (
                f"TC: {m.get('KimlikNo', '-')}\n"
                f"Ad Soyad: {m.get('AdSoyad', '-')}\n"
                f"Adres: {m.get('Ikametgah', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "Veri bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"Hata: {e}")

# --- /arama (spam arama) --- #
last_usage = {}
@bot.message_handler(commands=['arama'])
def handle_arama(message):
    user_id = message.from_user.id
    current_time = datetime.now()
    if user_id in last_usage and current_time < last_usage[user_id] + timedelta(minutes=1):
        bot.send_message(message.chat.id, "⚠️ Bu komutu 1 dakikada bir kullanabilirsin.", parse_mode="Markdown")
        return
    try:
        phone_number = message.text.split(' ')[1]
        if not phone_number.startswith('+'):
            raise ValueError
        # Basit bir fake call örneği, kendi servisini buraya ekle!
        bot.send_message(message.chat.id, f"*{phone_number}* numarasına arama isteği gönderildi. (fake)", parse_mode="Markdown")
        last_usage[user_id] = datetime.now()
    except Exception:
        bot.send_message(message.chat.id, "⚠️ Lütfen geçerli bir telefon numarası girin. Örnek: /arama +905555555555", parse_mode="Markdown")



def send_long_message(chat_id, text, parse_mode=None):
    max_len = 4096
    for i in range(0, len(text), max_len):
        bot.send_message(chat_id, text[i:i + max_len], parse_mode=parse_mode)




@bot.message_handler(commands=['sorgu'])
def kimlik_sorgu(message):
    try:
        chat_id = message.chat.id
        # Parametreleri ayrıştır
        text = message.text
        parameters = {}
        for part in text.split('-')[1:]:
            key_value = part.strip().split(maxsplit=1)
            if len(key_value) == 2:
                key, value = key_value
                parameters[key.lower()] = value.strip()

        # Zorunlu parametre kontrolü
        if not ('ad' in parameters and 'soyad' in parameters):
            bot.reply_to(
                message,
                "*⚠️ Geçersiz kullanım!* \nÖrnek: `/sorgu -ad ali -soyad veli -il istanbul -ilce kadıköy`\nÇift isim için: -ad azat+can",
                parse_mode="Markdown"
            )
            return

        # URL seçimi
        if 'ilce' in parameters:
            url = f"http://api.hexnox.pro/sowixapi/adsoyadilice.php?ad={parameters['ad']}&soyad={parameters['soyad']}&il={parameters.get('il', '')}&ilce={parameters['ilce']}"
        elif 'il' in parameters:
            url = f"http://api.hexnox.pro/sowixapi/adsoyadilce.php?ad={parameters['ad']}&soyad={parameters['soyad']}&il={parameters['il']}"
        else:
            url = f"http://api.hexnox.pro/sowixapi/adsoyadilce.php?ad={parameters['ad']}&soyad={parameters['soyad']}"

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        data = response.json()

        # Yanıtı güvenli al
        result_list = []
        if isinstance(data, dict) and 'data' in data and isinstance(data['data'], list):
            result_list = data['data']
        elif isinstance(data, list):
            result_list = data
        else:
            result_list = []

        if not result_list or len(result_list) == 0:
            bot.send_message(chat_id, "🔍 Hiç sonuç bulunamadı.")
            return

        formatted_message = f"🔍 Toplam: {len(result_list)} Kişi\n\n"
        for person in result_list:
            formatted_message += (
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                f"┃➥ AD: {person.get('ADI', 'Bilinmiyor')}\n"
                f"┃➥ SOYAD: {person.get('SOYADI', 'Bilinmiyor')}\n"
                f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                f"┃➥ İL: {person.get('NUFUSIL', 'Bilinmiyor')}\n"
                f"┃➥ İLÇE: {person.get('NUFUSILCE', 'Bilinmiyor')}\n"
                f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                f"┃➥ UYRUK: {person.get('UYRUK', 'Bilinmiyor')}\n"
                f"╰━━━━━━━━━━━━━━\n\n"
            )

        # Çok uzun mesajsa txt dosyası gönder
        if len(formatted_message) > 4000 or len(result_list) > 30:
            file_path = "adsoyadsorgu.txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted_message)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id, f, caption="Sonuçlar txt olarak gönderildi.")
            os.remove(file_path)
        else:
            send_long_message(chat_id, formatted_message)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Bir hata oluştu: {str(e)}")


# --- /ip --- #
IP_REGEX = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
@bot.message_handler(commands=['ip'])
def ip_sorgu(message):
    try:
        ip = message.text.split()[1]
        if not IP_REGEX.match(ip):
            bot.send_message(message.chat.id, "⚠️ Lütfen geçerli bir IP adresi girin!\nÖrnek: /ip 8.8.8.8", parse_mode="Markdown")
            return
        resp = requests.get(f"http://ip-api.com/json/{ip}").json()
        if resp["status"] == "success":
            msg = (
                f"IP: {resp['query']}\n"
                f"Ülke: {resp['country']} ({resp['countryCode']})\n"
                f"Şehir: {resp['regionName']} / {resp['city']}\n"
                f"Posta Kodu: {resp['zip']}\n"
                f"Operatör: {resp['isp']}\n"
            )
            bot.send_message(message.chat.id, msg)
        else:
            bot.send_message(message.chat.id, "Sorgu başarısız.")
    except Exception:
        bot.send_message(message.chat.id, "Kullanım: /ip 8.8.8.8")

# devamı aşağıda...# --- /operator --- #
@bot.message_handler(commands=['operator'])
def operator_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Lütfen bir GSM numarası girin!\nÖrnek: /operator 5553723339", parse_mode="Markdown")
        return
    gsm = args[1]
    url = f"http://api.hexnox.pro/sowixapi/operator.php?gsm={gsm}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        data = resp.json()
        if data and 'operator' in data:
            msg = (
                f"GSM: {data.get('gsm', '-')}\n"
                f"Operatör: {data.get('operator', '-')}\n"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "Operatör bilgisi bulunamadı.")
    except Exception as e:
        bot.send_message(chat_id, f"Hata: {e}")

# --- /sms --- #
@bot.message_handler(commands=['sms'])
def send_sms(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Lütfen bir telefon numarası girin!\nÖrnek: /sms 5555555555", parse_mode="Markdown")
        return
    gsm = args[1]
    url = f'https://sowixapi.online/api/sowixapi/sms.php?telno={gsm}'
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            bot.send_message(chat_id, "Sms gönderildi!")
        else:
            bot.send_message(chat_id, "SMS gönderirken bir hata oluştu.")
    except Exception:
        bot.send_message(chat_id, "API hatası.")

# --- /ig --- #
@bot.message_handler(commands=['ig'])
def ig_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Kullanıcı adı girin.\nÖrnek: /ig amedskofficial", parse_mode="Markdown")
        return
    username = args[1]
    url = f'http://api.hexnox.pro/sowixapi/instgram.php?search={username}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        result = resp.json()
        if isinstance(result, list) and len(result) > 0:
            user = result[0]
            pic_url = user.get('profile_pic_url', '')
            if pic_url:
                bot.send_photo(chat_id, pic_url)
            msg = (
                f"İSİM: {user.get('full_name', '-')}\n"
                f"USERNAME: {user.get('username', '-')}\n"
                f"GİZLİ HESAP: {'Evet' if user.get('is_private') else 'Hayır'}\n"
                f"MAVİ TİK: {'Evet' if user.get('is_verified') else 'Hayır'}"
            )
            bot.send_message(chat_id, msg)
        else:
            bot.send_message(chat_id, "Veri bulunamadı.")
    except Exception:
        bot.send_message(chat_id, "Bir hata oluştu.")

# --- /ses --- #
@bot.message_handler(commands=['ses'])
def ses_cevir(message):
    chat_id = message.chat.id
    text = " ".join(message.text.split()[1:])
    if not text:
        bot.send_message(chat_id, "⚠️ Lütfen bir mesaj girin!\nÖrnek: /ses Merhaba dünya", parse_mode='Markdown')
        return
    url = f'https://tilki.dev/api/yaziyi-ses-yapma?text={text}'
    try:
        response = requests.get(url)
        with open('mesaj_sesi.mp3', 'wb') as f:
            f.write(response.content)
        with open('mesaj_sesi.mp3', 'rb') as audio_file:
            bot.send_voice(chat_id, audio_file)
        os.remove('mesaj_sesi.mp3')
    except Exception:
        bot.send_message(chat_id, "Ses oluşturma sırasında hata oluştu.")

# --- /index --- #
@bot.message_handler(commands=['index'])
def index_cek(message):
    chat_id = message.chat.id
    args = message.text.split(maxsplit=1)
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Lütfen bir URL girin!\nÖrnek: /index https://google.com", parse_mode='Markdown')
        return
    url = args[1]
    if not url.startswith("http"):
        bot.send_message(chat_id, "⚠️ Geçersiz URL.", parse_mode='Markdown')
        return
    try:
        resp = requests.get(url)
        file_name = "site_index.html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(resp.text)
        with open(file_name, 'rb') as file:
            bot.send_document(chat_id, file)
        os.remove(file_name)
    except Exception:
        bot.send_message(chat_id, "Index çekilemedi.")

# --- /yaz --- #
API_ENDPOINT = 'https://apis.xditya.me/write?text={}'
@bot.message_handler(commands=['yaz'])
def yaz(message):
    chat_id = message.chat.id
    args = message.text.split(maxsplit=1)
    if len(args) != 2:
        bot.send_message(chat_id, "⚠️ Bir yazı girin!\nÖrnek: /yaz Selam millet", parse_mode="Markdown")
        return
    text = args[1]
    try:
        api_url = API_ENDPOINT.format(text)
        resp = requests.get(api_url)
        if resp.status_code == 200:
            bot.send_photo(chat_id, resp.content)
        else:
            bot.send_message(chat_id, "API'de sorun var.")
    except Exception:
        bot.send_message(chat_id, "Bir hata oluştu.")

# --- Bot'u başlat --- #
if __name__ == '__main__':
    print("Bot başlatılıyor...")
    bot.infinity_polling()
