import telebot
import requests
import urllib
import time
import random
from datetime import datetime
import hashlib, random
import sqlite3
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from telebot import types
from io import BytesIO
import telebot
import json
import requests
from telebot import types
import time
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from datetime import datetime
from pytz import timezone
from datetime import timedelta
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, request
import telegram
from datetime import datetime, timedelta
import re
import socket
import subprocess
import platform
import threading
import qrcode
from PIL import Image
import base64
import threading
import pytz
import re
import os

# Geçici log storage
temp_log_storage = {}
log_counter = 0

TOKEN = "7436117955:AAGI2XAmBGzkH0M0NztXPZZQmmtBfDqt9jc"
bot = telebot.TeleBot(TOKEN)

# Kanal ve grup kontrolünü devre dışı bırak - test amaçlı
kanal_kontrolu_aktif = False  # True yaparsan kontrol etmeye başlar

kanal_id = -1002646147395 
grup_id = -1002109722883

print("Bot Dişxwile")

from telebot import TeleBot, types

import telebot
import time

import telebot




@bot.message_handler(commands=['komutlar'])
def start(message):
    try:
        # Kanal kontrolü aktifse kontrol et
        if kanal_kontrolu_aktif:
            try:
                kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
            except:
                # Kanal kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                kanal_katildi = "left"
                
            try:
                grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
            except:
                # Grup kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                grup_katildi = "left"
            
            if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
                mesaj = "Komutları görmek için kanala ve gruba katılmanız gerekiyor. Katıldıktan sonra /komutlar yazarak komutları görebilirsiniz."
                
                kanala_katil = types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/ehliyetkimlikpasaport")
                gruba_katil = types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/dijvarhackchat")
                butonlar = types.InlineKeyboardMarkup()
                butonlar.row(kanala_katil, gruba_katil)
                bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
                return
        
        # Komutlar menüsünü göster
        mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • GSM den T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
        butonlar = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
    
    except Exception as e:
        # Chat bulunamadığında veya başka hata olduğunda komutları direkt göster
        print(f"Chat kontrolü hatası: {e}")
        mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • GSM den T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
        butonlar = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)







@bot.message_handler(commands=['start'])
def start(message):
    try:
        # Kanal kontrolü aktifse kontrol et
        if kanal_kontrolu_aktif:
            try:
                kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
            except:
                # Kanal kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                kanal_katildi = "left"
                
            try:
                grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
            except:
                # Grup kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                grup_katildi = "left"
            
            # Eğer kullanıcı kanala veya gruba katılmadıysa
            if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
                mesaj = (f"Merhaba 👋 {message.from_user.first_name},\n\n"
                         "Beni kullanabilmek için ana kanala ve chat grubuna katılmanız gerekiyor!\n"
                         "Kanala ve chate katılıp /start yazarak tekrar deneyin.")
                
                # Kanal ve grup katılım butonları
                kanala_katil = telebot.types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/ehliyetkimlikpasaport")
                gruba_katil = telebot.types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/dijvarhackchat")
                butonlar = telebot.types.InlineKeyboardMarkup()
                butonlar.row(kanala_katil, gruba_katil)
                
                bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
                return
        
        # Kullanıcı kontrolleri geçti veya kontrol deaktif
        mesaj = ("👋 Merhaba! Benim adım Polat Hack bot, sorgu yapmak için buradayım.\n"
                 "Beni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\n"
                 "En son güncellemeler hakkında bilgi almak için @ehliyetkimlikpasaport kanalıma katılın.\n\n"
                 "⛔ Not: Bot @polatalemdar330'a özel olarak yapılmıştır. "
                 "Botu kullanmak için Polat Hack'a katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız.")
        
        # Gruba ekleme ve diğer butonlar
        majeste_sohbet = telebot.types.InlineKeyboardButton("➕ Beni Grubuna Ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
        iletisim = telebot.types.InlineKeyboardButton("🙋 Owner", url="https://t.me/polatalemdar330")
        komutlar = telebot.types.InlineKeyboardButton("📜 Komutlar", callback_data="komutlar")
        
        butonlar = telebot.types.InlineKeyboardMarkup()
        butonlar.row(komutlar)
        butonlar.row(majeste_sohbet, iletisim)
        
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)

    except telebot.apihelper.ApiTelegramException as e:
        # Chat bulunamadı veya bot kanal/grupa erişim hataları
        if "chat not found" in str(e).lower() or e.error_code == 400:
            print(f"Chat bulunamadı hatası: {e}")
            # Chat kontrolü yapamıyorsak direkt hoş geldin mesajı göster
            mesaj = ("👋 Merhaba! Benim adım Polat Hack bot, sorgu yapmak için buradayım.\n"
                     "Beni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\n"
                     "⛔ Not: Bot @polatalemdar330'a özel olarak yapılmıştır.")
            
            majeste_sohbet = telebot.types.InlineKeyboardButton("➕ Beni Grubuna Ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
            iletisim = telebot.types.InlineKeyboardButton("🙋 Owner", url="https://t.me/polatalemdar330")
            komutlar = telebot.types.InlineKeyboardButton("📜 Komutlar", callback_data="komutlar")
            
            butonlar = telebot.types.InlineKeyboardMarkup()
            butonlar.row(komutlar)
            butonlar.row(majeste_sohbet, iletisim)
            
            bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
        # Eğer bot, kullanıcının engellediği bir mesajı gönderirse 403 hatasını yakala
        elif e.error_code == 403 and "bot was blocked by the user" in str(e):
            print(f"Bot {message.from_user.id} tarafından engellendi.")
        else:
            # Diğer hataları işlemeye devam et
            print(f"Bir hata oluştu: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")
        # Herhangi bir hata durumunda basit hoş geldin mesajı
        mesaj = "👋 Merhaba! Bot aktif. Komutlar için /komutlar yazın."
        bot.send_message(message.chat.id, mesaj)






        
def send_long_message(chat_id, text):
    MAX_MESSAGE_LENGTH = 4096  # Telegram mesaj karakter sınırı

    # Mesajı parçalara böl
    for i in range(0, len(text), MAX_MESSAGE_LENGTH):
        bot.send_message(chat_id, text[i:i + MAX_MESSAGE_LENGTH])

@bot.message_handler(commands=['adsoyad'])
def adsoyad_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 3:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad ve soyad girin!\n\nÖrnek:* `/adsoyad ahmet yılmaz`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyad.php?ad={ad}&soyad={soyad}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadsorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad ve soyad için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['adsoyadil'])
def adsoyadil_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 4:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad, soyad ve il girin!\n\nÖrnek:* `/adsoyadil ahmet yılmaz istanbul`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        il = args[3]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyadil.php?ad={ad}&soyad={soyad}&il={il}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad il bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad İl Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadilsorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} {il} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad, soyad ve il için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['adsoyadililce'])
def adsoyadililce_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 5:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad, soyad, il ve ilçe girin!\n\nÖrnek:* `/adsoyadililce ahmet yılmaz istanbul kadıköy`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        il = args[3]
        ilce = args[4]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyadililce.php?ad={ad}&soyad={soyad}&il={il}&ilce={ilce}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad il ilçe bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad İl İlçe Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadililcesorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} {il} {ilce} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad, soyad, il ve ilçe için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['tc'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tc.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            text = response.content.decode('utf-8-sig')
            result = json.loads(text)
            
            if result.get("success") and "data" in result:
                member = result["data"]
                
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                formatted_message += (
                    f"┃➥ TC: {member.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ AD: {member.get('AD', 'Bilinmiyor')}\n"
                    f"┃➥ SOYAD: {member.get('SOYAD', 'Bilinmiyor')}\n"
                    f"┃➥ BABA ADI: {member.get('BABAADI', 'Bilinmiyor')}\n"
                    f"┃➥ BABA TC: {member.get('BABATC', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE ADI: {member.get('ANNEADI', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE TC: {member.get('ANNETC', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İL: {member.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İLÇE: {member.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                )
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
                
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/tc 11111111110`", parse_mode="Markdown")

import os

def send_long_message_or_file(chat_id, text, file_name="output.txt"):
    MAX_MESSAGE_LENGTH = 4096  # Telegram mesaj karakter sınırı

    if len(text) > MAX_MESSAGE_LENGTH:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
        with open(file_name, 'rb') as f:
            bot.send_document(chat_id, f)
        os.remove(file_name)
    else:
        bot.send_message(chat_id, text)

@bot.message_handler(commands=['aile'])
def aile(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir TC kimlik numarası girin.*\n\n*Örnek:* `/aile 11111111110`", parse_mode="Markdown")
        return

    tc_number = parts[1]
    url = f'http://api.hexnox.pro/sowixapi/aile.php?tc={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *Aile bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)  # Timeout artırıldı
        response.raise_for_status()

        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)
        
        result = response.json()

        if not result.get("success") or "data" not in result:
            bot.send_message(chat_id, "❌ Aile bilgisi bulunamadı.")
            return

        members = result["data"]

        if not isinstance(members, list) or len(members) == 0:
            bot.send_message(chat_id, "❌ Aile üyesi bulunamadı.")
            return

        formatted_message = f"👨‍👩‍👧‍👦 *Toplam Aile Üyesi:* {len(members)}\n\n"

        for i, member in enumerate(members, start=1):
            formatted_message += (
                f"🔹 *{i}. Üye: {member.get('Yakınlık', 'Bilinmiyor')}*\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *ID:* {member.get('ID', '-')}\n"
                f"┃➥ *TC:* `{member.get('TC', '-')}`\n"
                f"┃➥ *Ad:* {member.get('AD', '-')}\n"
                f"┃➥ *Soyad:* {member.get('SOYAD', '-')}\n"
                f"┃➥ *GSM:* {member.get('GSM', '-')}\n"
                f"┃➥ *Baba Adı:* {member.get('BABAADI', '-')}\n"
                f"┃➥ *Baba TC:* {member.get('BABATC', '-')}\n"
                f"┃➥ *Anne Adı:* {member.get('ANNEADI', '-')}\n"
                f"┃➥ *Anne TC:* {member.get('ANNETC', '-')}\n"
                f"┃➥ *Doğum Tarihi:* {member.get('DOGUMTARIHI', '-')}\n"
                f"┃➥ *Ölüm Tarihi:* {member.get('OLUMTARIHI', 'YOK')}\n"
                f"┃➥ *Doğum Yeri:* {member.get('DOGUMYERI', '-')}\n"
                f"┃➥ *Memleket İl:* {member.get('MEMLEKETIL', '-')}\n"
                f"┃➥ *Memleket İlçe:* {member.get('MEMLEKETILCE', '-')}\n"
                f"┃➥ *Memleket Köy:* {member.get('MEMLEKETKOY', '-')}\n"
                f"┃➥ *Adres İl:* {member.get('ADRESIL', '-')}\n"
                f"┃➥ *Adres İlçe:* {member.get('ADRESILCE', '-')}\n"
                f"┃➥ *Ailesi Sıra No:* {member.get('AILESIRANO', '-')}\n"
                f"┃➥ *Birey Sıra No:* {member.get('BIREYSIRANO', '-')}\n"
                f"┃➥ *Medeni Hal:* {member.get('MEDENIHAL', '-')}\n"
                f"┃➥ *Cinsiyet:* {member.get('CINSIYET', '-')}\n"
                f"╰━━━━━━━━━━━━━━\n\n"
            )

        # Uzunsa dosya olarak gönder
        if len(formatted_message) > 4000:
            file_name = "aile_sorgu.txt"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(formatted_message)
            with open(file_name, "rb") as f:
                bot.send_document(chat_id, f, caption="📋 Aile Sorgu Sonuçları")
            os.remove(file_name)  # Dosyayı temizle
        else:
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")
	



import requests
import json

@bot.message_handler(commands=['sulale'])
def sulale_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) != 2:
        bot.send_message(
            chat_id,
            "⚠️ *Lütfen geçerli bir TC Kimlik Numarası girin.*\n\n*Örnek:* `/sulale 11111111110`",
            parse_mode="Markdown"
        )
        return

    tc_number = args[1]
    url = f'https://api.hexnox.pro/sowixapi/sulale.php?tc={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Önce kullanıcıya bekleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *Sülale bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        # Yeniden deneme mekanizması
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, timeout=30)  # Timeout 30 saniyeye çıkarıldı
                response.raise_for_status()
                result = response.json()
                break  # Başarılı olursa döngüden çık
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:  # Son deneme değilse
                    bot.edit_message_text(
                        f"⏳ *Bağlantı yavaş, tekrar deneniyor... ({attempt + 2}/{max_retries})*",
                        chat_id, loading_msg.message_id, parse_mode="Markdown"
                    )
                    continue
                else:
                    raise  # Son denemeyse hatayı fırlat
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    bot.edit_message_text(
                        f"⚠️ *Bağlantı hatası, tekrar deneniyor... ({attempt + 2}/{max_retries})*",
                        chat_id, loading_msg.message_id, parse_mode="Markdown"
                    )
                    continue
                else:
                    raise

        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        # API direkt liste döndürüyorsa
        if isinstance(result, list):
            members = result
        # API dict formatında döndürüyorsa
        elif isinstance(result, dict):
            if not result.get("success"):
                bot.send_message(chat_id, "❌ Sülale bilgisi bulunamadı.")
                return
            
            # Data alanını kontrol et
            data = result.get("data")
            if not data:
                bot.send_message(chat_id, "❌ Sülale verisi boş.")
                return
                
            # Eğer data bir liste değilse, liste haline getir
            if not isinstance(data, list):
                data = [data]
                
            members = data
        else:
            bot.send_message(chat_id, "❌ Beklenmeyen API yanıt formatı.")
            return
        
        # Veri yapısını kontrol et
        if not members or len(members) == 0:
            bot.send_message(chat_id, "❌ Sülale bilgisi bulunamadı.")
            return
            
        formatted_message = f"🌳 *Toplam Sülale Üyesi:* {len(members)}\n\n"

        for i, member in enumerate(members, start=1):
            # member'ın sözlük olup olmadığını kontrol et
            if not isinstance(member, dict):
                formatted_message += f"🔹 *{i}. Üye: Veri Formatı Hatası*\n\n"
                continue
            
            # Güvenli veri alımı için fonksiyon
            def safe_get(key, default='-'):
                value = member.get(key, default)
                return value if value and str(value).strip() else default
                
            formatted_message += (
                f"🔹 *{i}. Üye: {safe_get('YAKINLIK', 'Bilinmiyor')}*\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *TC:* `{safe_get('TC')}`\n"
                f"┃➥ *Ad:* {safe_get('AD')}\n"
                f"┃➥ *Soyad:* {safe_get('SOYAD')}\n"
                f"┃➥ *Doğum Tarihi:* {safe_get('DOGUMTARIHI')}\n"
                f"┃➥ *Memleket İl:* {safe_get('MEMLEKETIL')}\n"
                f"┃➥ *Memleket İlçe:* {safe_get('MEMLEKETILCE')}\n"
                f"┃➥ *Anne Adı:* {safe_get('ANNEADI')}\n"
                f"┃➥ *Anne TC:* {safe_get('ANNETC')}\n"
                f"┃➥ *Baba Adı:* {safe_get('BABAADI')}\n"
                f"┃➥ *Baba TC:* {safe_get('BABATC')}\n"
                f"┃➥ *Uyruk:* {safe_get('UYRUK', 'T.C.')}\n"
                f"╰━━━━━━━━━━━━━━\n\n"
            )

        # Uzunsa dosya olarak gönder, kısaysa direkt mesaj gönder
        if len(formatted_message) > 4000:
            file_name = "sulale_sorgu.txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(formatted_message)

            with open(file_name, "rb") as file:
                bot.send_document(chat_id, file, caption="🌳 Sülale Sorgu Sonuçları")
            
            os.remove(file_name)  # Dosyayı temizle
        else:
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as err:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"🚫 *API bağlantı hatası:*\n`{str(err)[:100]}...`", parse_mode="Markdown")
    except KeyError as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Veri yapısı hatası: {e}")
    except TypeError as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Veri tipi hatası: {e}")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")


import requests
import json

@bot.message_handler(commands=['tcpro'])
def tcpro_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tcpro.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC Pro bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)

            response.encoding = 'utf-8-sig'
            json_data = response.text

            result = json.loads(json_data)

            if result.get("success") and result.get("data"):
                person = result["data"]  # Artık data direkt obje

                # İstenen formatta mesaj oluşturma
                formatted_message = (
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                    f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                    f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                    f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                    f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                    f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                    f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                    f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                    f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                    f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                    f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                    f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )

                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "🔍 TC Pro bilgisi bulunamadı.")
        except requests.exceptions.HTTPError:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API isteği sırasında bir hata oluştu.")
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"⚠️ Beklenmeyen bir hata oluştu: {err}")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/tcpro 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['medeni'])
def medeni_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/medeni.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Medeni hal bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            result = response.json()
            
            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                person = result["data"][0]
                formatted_message = (
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ ADI: {person.get('ADI', 'Bilinmiyor')}\n"
                    f"┃➥ SOYADI: {person.get('SOYADI', 'Bilinmiyor')}\n"
                    f"┃➥ MEDENI HALI: {person.get('MEDENI_HALI', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "*🔍 Belirtilen TC kimlik numarası için medeni hal bilgisi bulunamadı.*", parse_mode="Markdown")
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/medeni 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['cocuk'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/es.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Çocuk bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # JSON verisini ayıklayın
            result = response.json()

            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                # Verileri ayrıştır
                children = [member for member in result["data"] if member.get('YAKINLIK') == 'Çocuğu']
                
                # Formatted message
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                
                # Eğer çocuklar varsa, her birini ekle
                if children:
                    for child in children:
                        formatted_message += (
                            f"┃➥ Yakınlık: Çocuğu\n"
                            f"┃➥ TC: {child.get('TC', 'Bilinmiyor')}\n"
                            f"┃➥ AD: {child.get('ADI', 'Bilinmiyor')}\n"
                            f"┃➥ SOYAD: {child.get('SOYADI', 'Bilinmiyor')}\n"
                            f"┃➥ DOĞUM TARİHİ: {child.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                            f"┃➥ İL: {child.get('NUFUSIL', 'Bilinmiyor')}\n"
                            f"┃➥ İLÇE: {child.get('NUFUSILCE', 'Bilinmiyor')}\n"
                            f"┃➥ UYRUK: {child.get('Uyruk', 'Bilinmiyor')}\n"
                            "┃━━━━━━━━━━━━━━\n"
                        )
                else:
                    formatted_message += "┃➥ Çocuk bilgisi bulunamadı.\n"

                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/cocuk 11111111110`", parse_mode="Markdown")




@bot.message_handler(commands=['es'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/es.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Eş bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # JSON verisini ayıklayın
            result = response.json()

            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                # Verileri ayrıştır
                eşi = [member for member in result["data"] if member.get('YAKINLIK') == 'Eşi']
                
                # Formatted message
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                
                # Eş bilgisi
                if eşi:
                    member = eşi[0]
                    formatted_message += (
                        f"┃➥ Yakınlık: Eşi\n"
                        f"┃➥ TC: {member.get('TC', 'Bilinmiyor')}\n"
                        f"┃➥ AD: {member.get('ADI', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {member.get('SOYADI', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {member.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ İL: {member.get('NUFUSIL', 'Bilinmiyor')}\n"
                        f"┃➥ İLÇE: {member.get('NUFUSILCE', 'Bilinmiyor')}\n"
                        f"┃➥ UYRUK: {member.get('Uyruk', 'Bilinmiyor')}\n"
                    )
                else:
                    formatted_message += "┃➥ Eş bilgisi bulunamadı.\n"
                
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id,  "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/es 11111111110`", parse_mode="Markdown")



@bot.message_handler(commands=['adres'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/adres.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Adres bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            text = response.content.decode('utf-8-sig')
            result = json.loads(text)
            
            if result.get("success") and "data" in result:
                member = result["data"]
                
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                formatted_message += (
                    f"┃➥ TC: {member.get('KimlikNo', 'Bilinmiyor')}\n"
                    f"┃➥ AD SOYAD: {member.get('AdSoyad', 'Bilinmiyor')}\n"
                    f"┃➥ DOĞUM YERİ: {member.get('DogumYeri', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ NO: {member.get('VergiNumarasi', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES: {member.get('Ikametgah', 'Bilinmiyor')}\n"
                    f"┃ \n"
                )
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "⚠️*Veri Bulunamadı.*", parse_mode="Markdown")
        
        except requests.exceptions.RequestException:
            bot.send_message(chat_id, "⚠️*Bir hata oluştu. Lütfen daha sonra tekrar deneyin.*", parse_mode="Markdown")
        except json.JSONDecodeError:
            bot.send_message(chat_id, "⚠️*API yanıtı işlenemedi.*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/adres 11111111110`", parse_mode="Markdown")

        

@bot.message_handler(commands=['iban'])
def iban(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        iban_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/iban.php?iban={iban_number}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *IBAN bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # İstek başarısız olursa bir hata fırlatılır
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            result = response.content.decode('utf-8-sig')  # UTF-8 BOM'u temizler
            result_json = json.loads(result)  # JSON verisi düzgün bir şekilde işlenir
            
            if result_json:
                banka = result_json.get('BANKA', {})
                sube = result_json.get('ŞUBE', {})
                
                formatted_message = (
                    f"╔══════════════╗\n"
                    f"║ IBAN Bilgileri\n"
                    f"╠══════════════╣\n"
                    f"║ Banka Adı: {banka.get('Adı', 'Bilinmiyor')}\n"
                    f"║ Banka Kod: {banka.get('Kod', 'Bilinmiyor')}\n"
                    f"║ Swift: {banka.get('Swift', 'Bilinmiyor')}\n"
                    f"║ Hesap No: {banka.get('Hesap No', 'Bilinmiyor')}\n"
                    f"║ Şube Adı: {sube.get('Ad', 'Bilinmiyor')}\n"
                    f"║ Şube Kod: {sube.get('Kod', 'Bilinmiyor')}\n"
                    f"║ İl: {sube.get('İl', 'Bilinmiyor')}\n"
                    f"║ İlçe: {sube.get('İlçe', 'Bilinmiyor')}\n"
                    f"║ Tel: {sube.get('Tel', 'Bilinmiyor')}\n"
                    f"║ Fax: {sube.get('Fax', 'Bilinmiyor')}\n"
                    f"║ Adres: {sube.get('Adres', 'Bilinmiyor')}\n"      
                    f"╚══════════════╝\n"
                    f"@devillerden"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz IBAN numarası veya veri bulunamadı.")
        except requests.exceptions.RequestException as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"API isteği başarısız: {str(e)}")
        except (KeyError, ValueError):
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "Geçersiz API yanıtı veya IBAN numarası bulunamadı.")
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir IBAN Numarası girin!\n\nÖrnek:* `/iban TR560001002247786851675002`', parse_mode='Markdown')


@bot.message_handler(commands=['ihbar'])
def ihbar_gonder(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        adres = ' '.join(message.text.split()[1:])
        url = f'http://api.hexnox.pro/sowixapi/ihbar.php?adres={adres}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get("success"):
                formatted_message = (
                    f"✅ *İhbar Başarıyla Gönderildi*\n\n"
                    f"📍 *Adres:* {adres}\n"
                    f"📅 *Tarih:* {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
                    f"🚨 *Durum:* İşleme Alındı\n\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "*❌ İhbar gönderilemedi. Lütfen tekrar deneyin.*", parse_mode="Markdown")
        except Exception as e:
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen bir adres girin*.\n\n*Örnek:* `/ihbar Atatürk Mahallesi İstanbul`", parse_mode="Markdown")


@bot.message_handler(commands=['vergid'])
def vergi_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/vergi.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                person = result["data"][0]
                formatted_message = (
                    f"💰 *Vergi Bilgileri*\n\n"
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ ADI: {person.get('ADI', 'Bilinmiyor')}\n"
                    f"┃➥ SOYADI: {person.get('SOYADI', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ DAİRESİ: {person.get('VERGI_DAIRESI', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ NO: {person.get('VERGI_NO', 'Bilinmiyor')}\n"
                    f"┃➥ GELİR DİLİMİ: {person.get('GELIR_DILIMI', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "*🔍 Belirtilen TC kimlik numarası için vergi bilgisi bulunamadı.*", parse_mode="Markdown")
        except Exception as e:
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/vergid 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['tcgsm'])
def tcgsm(message):
    chat_id = message.chat.id
    
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tcgsm.php?tc={tc_number}'
        
        # User-Agent başlığını ekliyoruz
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC'den GSM sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        response = requests.get(url, headers=headers)
        
        try:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # Yanıtı ham olarak al ve UTF-8 BOM'dan temizle
            raw_response = response.content
            response_text = raw_response.decode('utf-8-sig')
            
            # Yanıtı terminalde bas


            # JSON verisini işleyin
            result = json.loads(response_text)
            print(f"Parsed JSON: {result}")

            # Yanıtın formatını kontrol et
            if isinstance(result, dict) and result.get("success") and isinstance(result.get("data"), list):
                data = result['data']
                
                # TC numarasını ve GSM numaralarını listeleyin
                formatted_message = f"╭━━━━━━━━━━━━━━\n┃➥TC: `{tc_number}`\n"
                
                for entry in data:
                    gsm = entry.get('GSM', 'Bilinmiyor')
                    formatted_message += f"┃➥GSM: `{gsm}`\n"
                
                formatted_message += "╰━━━━━━━━━━━━━━\n"
                
                bot.send_message(chat_id, formatted_message, parse_mode='Markdown')
            else:
                bot.send_message(chat_id, "⚠️ Geçersiz TC numarası veya veri bulunamadı.")

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"⚠️ Geçersiz API yanıtı veya TC numarası bulunamadı. Hata: {e}")
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tcgsm 11111111110`', parse_mode='Markdown')



@bot.message_handler(commands=['gsmtc'])
def gsmtc_sorgu(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir GSM numarası girin.*\n\n*Örnek:* `/gsmtc 5553723339`", parse_mode="Markdown")
        return

    gsm_number = parts[1]
    url = f'http://api.hexnox.pro/sowixapi/gsm.php?gsm={gsm_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *GSM numarası sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        result = response.json()

        if result.get('success') and result.get('data'):
            data = result['data']
            
            formatted_message = (
                f"📱 *GSM Sorgu Sonucu*\n\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *GSM:* {data.get('GSM', '-')}\n"
                f"┃➥ *TC:* `{data.get('TC', '-')}`\n"
                f"╰━━━━━━━━━━━━━━\n"
                f"@polatalemdarsorgubot"
            )
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ Bu GSM numarası için TC bilgisi bulunamadı.")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")


@bot.message_handler(commands=['operator'])
def operator(message):
    if message.chat.type != "private":
        return

    gsm_number = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm_number:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM numarası girin!.\nÖrnek:* `/operator 5553723339`', parse_mode="Markdown")
        return

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(message.chat.id, "🔍 *Operatör bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        api_url = f"http://api.hexnox.pro/sowixapi/operator.php?gsm={gsm_number}"
        headers = {
            'User-Agent': 'YourAppName/1.0'
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Yanıtı bir dosyaya yazma
        with open('response.json', 'wb') as file:
            file.write(response.content)

        # Dosyadan okuma ve BOM karakterlerini temizleme
        with open('response.json', 'r', encoding='utf-8-sig') as file:
            response_text = file.read()

        # JSON yanıtını işleme
        data = json.loads(response_text)

        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)

        # API yanıtında 'operator' anahtarı varsa
        if data and 'operator' in data:
            result_text = (
                f"╭─━━━━━━━━━━━━─╮\n"
                f"┃*GSM:* `{data.get('gsm', 'Bilinmiyor')}`\n"
                f"┃*Operatör:* `{data.get('operator', 'Bilinmiyor')}`\n"
                f"╰─━━━━━━━━━━━━─╯"
            )
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, result_text, parse_mode="Markdown")
        else:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz bilgiler ile eşleşen bir operatör bulunamadı!*', parse_mode="Markdown")

    except requests.exceptions.HTTPError as errh:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')

    except requests.exceptions.ConnectionError as errc:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, f'⚠️ *Bir hata oluştu: {str(e)}*', parse_mode="Markdown")


@bot.message_handler(commands=['gsmdetay'])
def gsmdetay_sorgu(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir GSM numarası girin.*\n\n*Örnek:* `/gsmdetay 5553723339`", parse_mode="Markdown")
        return

    gsm_number = parts[1]
    url = f'https://api.hexnox.pro/sowixapi/gsmdetay.php?gsm={gsm_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *GSM detay bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        result = response.json()

        if result.get('success') and result.get('Data'):
            data = result['Data']
            
            formatted_message = (
                f"📱 *GSM Detay Sorgu Sonucu*\n\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *TC:* `{data.get('TC', '-')}`\n"
                f"┃➥ *Ad:* {data.get('AD', '-')}\n"
                f"┃➥ *Soyad:* {data.get('SOYAD', '-')}\n"
                f"┃➥ *Doğum Tarihi:* {data.get('DOGUMTARIHI', '-')}\n"
                f"┃➥ *Adres İl:* {data.get('ADRESIL', '-')}\n"
                f"┃➥ *Adres İlçe:* {data.get('ADRESILCE', '-')}\n"
                f"┃➥ *Anne Adı:* {data.get('ANNEADI', '-')}\n"
                f"┃➥ *Anne TC:* {data.get('ANNETC', '-')}\n"
                f"┃➥ *Baba Adı:* {data.get('BABAADI', '-')}\n"
                f"┃➥ *Baba TC:* {data.get('BABATC', '-')}\n"
                f"┃➥ *Cinsiyet:* {data.get('CINSIYET', '-')}\n"
                f"┃➥ *Vergi No:* {data.get('VergiNumarasi', '-')}\n"
                f"┃➥ *İkametgah:* {data.get('Ikametgah', '-')}\n"
                f"╰━━━━━━━━━━━━━━\n"
                f"@polatalemdarsorgubot"
            )
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ Bu GSM numarası için detay bilgisi bulunamadı.")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")



        

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

# Kullanıcıların son komut kullanma zamanlarını saklayacak bir sözlük
last_usage = {}

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return '*Arama gönderildi.*'
    else:
        return '*Arama gönderilemedi.*'

@bot.message_handler(commands=['arama'])
def handle_arama(message):
    user_id = message.from_user.id
    current_time = datetime.now()
    
   # Kullanıcının son komut kullanım zamanı kontrol ediliyor
    if user_id in last_usage:
        last_used = last_usage[user_id]
        if current_time < last_used + timedelta(minutes=1):
            bot.send_message(message.chat.id, "*⚠️ Bu komutu sadece 1 dakikada bir kullanabilirsiniz.*", parse_mode="Markdown")
            return

    try:
        phone_number = message.text.split(' ')[1]
        if not phone_number.startswith('+'):
            raise ValueError
        result = send_spam(phone_number)
        bot.send_message(message.chat.id, result, parse_mode="Markdown")
        
           # Kullanıcının son komut kullanım zamanı güncelleniyor
        last_usage[user_id] = datetime.now()
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Komutu yanlış kullandınız. Doğru kullanım: /arama +905555555555*", parse_mode="Markdown")
    except ValueError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir telefon numarası girin. Örnek: /arama +905555555555*", parse_mode="Markdown")








# IP adresi kontrolü için regex
IP_REGEX = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        ip = message.text.split(' ')[1]
        # IP adresinin geçerli olup olmadığını kontrol et
        if not IP_REGEX.match(ip):
            bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")
            return
        
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        username = message.from_user.username

        response_message = f'''
sorgulanıyor bekleyiniz
'''
        bot.send_message(message.chat.id, response_message)

        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            response_message = f'''
╭━━━━━━━━━━━━━╮
┃➥ @polatalemdar330
┃━━━━━━━━━━━━━━
┃➥ IP: {response['query'] or 'Bulunamadı'}
┃➥ Ülke: {response['country']} - {response['countryCode'] or 'Bulunamadı'}
┃➥ Şehir : {response['regionName'] or 'Bulunamadı'}
┃➥ İlçe: {response["city"] or 'Bulunamadı'}
┃➥ Posta Kodu: {response["zip"] or 'Bulunamadı'}
┃➥ Operatör: {response["isp"] or 'Bulunamadı'}
┃➥ Zaman Türü: {response["timezone"] or 'Bulunamadı'}
┃➥ Koordinatlar: {response["lat"] or 'Bulunamadı'}
╰━━━━━━━━━━━━━╯'''
            bot.send_message(message.chat.id, response_message)

            log_message = f"Yeni IP Adresi Sorgulandı!\n" \
                          f"Sorgulanan IP: {ip}\n" \
                          f"Sorgulayan ID: {user_id}\n" \
                          f"Sorgulayan Adı: {user_name}\n" \
                          f"Sorgulayan K. Adı: @{username}"
            
            bot.send_message(message.chat.id, " Başarıyla sorgulandı ✅")
    except IndexError:
        bot.send_message(message.chat.id,
        "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")


@bot.message_handler(commands=['ping'])
def ping_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir hedef belirtin!*\n\n*Örnek:* `/ping google.com`", parse_mode="Markdown")
            return
            
        target = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Ping işlemi yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Ping komutu çalıştır
        system = platform.system().lower()
        if system == "windows":
            cmd = f"ping -n 4 {target}"
        else:
            cmd = f"ping -c 4 {target}"
            
        result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=30)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if result.returncode == 0:
            # Başarılı ping sonucu
            formatted_message = f"🌐 **Ping Sonucu**\n\n```\n{result.stdout}\n```"
        else:
            formatted_message = f"❌ **Ping Başarısız**\n\n```\n{result.stderr}\n```"
            
        if len(formatted_message) > 4000:
            # Dosya olarak gönder
            with open("ping_result.txt", "w", encoding="utf-8") as f:
                f.write(result.stdout if result.returncode == 0 else result.stderr)
            with open("ping_result.txt", "rb") as f:
                bot.send_document(message.chat.id, f, caption=f"📊 {target} Ping Sonuçları")
            os.remove("ping_result.txt")
        else:
            bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
            
    except subprocess.TimeoutExpired:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, "⏰ *Ping işlemi zaman aşımına uğradı.*", parse_mode="Markdown")
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['portscan'])
def portscan_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir hedef belirtin!*\n\n*Örnek:* `/portscan google.com`", parse_mode="Markdown")
            return
            
        target = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Port taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Yaygın portlar listesi
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 1723, 3389, 5432, 5900, 8080]
        open_ports = []
        
        def scan_port(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((host, port))
                sock.close()
                if result == 0:
                    return port
            except:
                pass
            return None
        
        # Port taraması
        with threading.ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(scan_port, target, port) for port in common_ports]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if open_ports:
            open_ports.sort()
            ports_text = ", ".join(map(str, open_ports))
            formatted_message = f"🔓 **Port Tarama Sonucu**\n\n**Hedef:** {target}\n**Açık Portlar:** {ports_text}\n**Toplam:** {len(open_ports)} port"
        else:
            formatted_message = f"🔒 **Port Tarama Sonucu**\n\n**Hedef:** {target}\n**Sonuç:** Açık port bulunamadı"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['leakscan'])
def leakscan_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen sorgulamak istediğiniz veriyi belirtin!*\n\n*Örnek:* `/leakscan email@example.com`", parse_mode="Markdown")
            return
            
        query = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Leak taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # HaveIBeenPwned API (ücretsiz kullanım sınırlı)
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            # Yükleme mesajını sil
            bot.delete_message(message.chat.id, loading_msg.message_id)
            
            if response.status_code == 200:
                breaches = response.json()
                if breaches:
                    formatted_message = f"⚠️ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** {len(breaches)} veri ihlali bulundu\n\n"
                    for breach in breaches[:5]:  # İlk 5 sonuç
                        formatted_message += f"• **{breach.get('Name', 'Bilinmiyor')}**\n  Tarih: {breach.get('BreachDate', 'Bilinmiyor')}\n\n"
                else:
                    formatted_message = f"✅ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Veri ihlali bulunamadı"
            elif response.status_code == 404:
                formatted_message = f"✅ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Veri ihlali bulunamadı"
            else:
                formatted_message = f"❌ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Servis şu anda kullanılamıyor"
                
        except:
            formatted_message = f"❌ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** API erişim hatası"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['dns'])
def dns_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir domain belirtin!*\n\n*Örnek:* `/dns google.com`", parse_mode="Markdown")
            return
            
        domain = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *DNS bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # DNS sorgusu için API kullan
        url = f"https://dns.google/resolve?name={domain}&type=A"
        response = requests.get(url, timeout=15)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if response.status_code == 200:
            data = response.json()
            if 'Answer' in data:
                formatted_message = f"🌐 **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n\n"
                for record in data['Answer']:
                    formatted_message += f"**Tip:** {record.get('type', 'Bilinmiyor')}\n"
                    formatted_message += f"**IP:** {record.get('data', 'Bilinmiyor')}\n"
                    formatted_message += f"**TTL:** {record.get('TTL', 'Bilinmiyor')}\n\n"
            else:
                formatted_message = f"❌ **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n**Durum:** DNS kaydı bulunamadı"
        else:
            formatted_message = f"❌ **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n**Durum:** DNS sorgu hatası"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['defteryaz'])
def defteryaz_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen yazmak istediğiniz metni belirtin!*\n\n*Örnek:* `/defteryaz Merhaba Dünya`", parse_mode="Markdown")
            return
            
        text = args[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Deftere yaz
        with open("defter.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")
            
        bot.send_message(message.chat.id, f"✅ *Metin deftere yazıldı!*\n\n**Yazılan metin:** {text}", parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['subdomain'])
def subdomain_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir domain belirtin!*\n\n*Örnek:* `/subdomain example.com`", parse_mode="Markdown")
            return
            
        domain = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Subdomain taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Yaygın subdomain'ler
        common_subdomains = ['www', 'mail', 'ftp', 'admin', 'api', 'blog', 'dev', 'test', 'staging', 'app']
        found_subdomains = []
        
        def check_subdomain(subdomain, domain):
            try:
                full_domain = f"{subdomain}.{domain}"
                socket.gethostbyname(full_domain)
                return full_domain
            except:
                return None
        
        # Subdomain kontrolü
        with threading.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(check_subdomain, sub, domain) for sub in common_subdomains]
            for future in futures:
                result = future.result()
                if result:
                    found_subdomains.append(result)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if found_subdomains:
            subdomains_text = "\n• ".join(found_subdomains)
            formatted_message = f"🌐 **Subdomain Tarama Sonucu**\n\n**Domain:** {domain}\n**Bulunan Subdomain'ler:**\n• {subdomains_text}\n\n**Toplam:** {len(found_subdomains)} subdomain"
        else:
            formatted_message = f"❌ **Subdomain Tarama Sonucu**\n\n**Domain:** {domain}\n**Sonuç:** Subdomain bulunamadı"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['qrcode'])
def qrcode_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen QR kod için metin belirtin!*\n\n*Örnek:* `/qrcode https://example.com`", parse_mode="Markdown")
            return
            
        text = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *QR kod oluşturuluyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # QR kod oluşturma (basit implementasyon - qrcode kütüphanesi olmadan)
        # API kullanarak QR kod oluştur
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={urllib.parse.quote(text)}"
        
        response = requests.get(qr_url, timeout=15)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if response.status_code == 200:
            # QR kod resmi olarak gönder
            bot.send_photo(message.chat.id, response.content, caption=f"📱 **QR Kod**\n\n**İçerik:** {text}")
        else:
            bot.send_message(message.chat.id, "❌ *QR kod oluşturulamadı.*", parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")



@bot.callback_query_handler(func=lambda call: call.data == "komutlar")
def komutlar(call):
    mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • gsm nunaradan T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
    geri = telebot.types.InlineKeyboardButton("Geri", callback_data="geri")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.add(geri)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)
    
YEGEN_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/yegen.php?tc="

@bot.message_handler(commands=['yegen'])
def handle_yegen_command(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    chat_id = message.chat.id
 
    
        
    try:
        
        tc = message.text.split()[1]
        
        
        api_response = requests.get(YEGEN_API + tc).json()

        
        user_info = api_response.get("Yeğenler", [])

 
        response_text = (
            f""
            f""
            f""
        )

        for info in user_info:
            response_text += (
                f"\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ TC: {info['TC']}\n"
                f"┃➥ ADI: {info['ADI']}\n"
                f"┃➥ SOY ADI: {info['SOYADI']}\n"
                f"┃➥ DOĞUM TARİHİ: {info['DOGUMTARIHI']}\n"
                f"┃➥ İL: {info['NUFUSIL']}\n"
                f"┃➥ İLÇE: {info['NUFUSILCE']}\n"
                f"┃➥ ANNE ADI: {info['ANNEADI']}\n"
                f"┃➥ ANNE TC: {info['ANNETC']}\n"
                f"┃➥ BABA ADI: {info['BABAADI']}\n"
                f"┃➥ BABA TC: {info['BABATC']}\n"
                f"┃➥ UYRUK: {info['UYRUK']}\n"
                f"┃➥ YAKINLIK: {info['Yakinlik']}\n"
                f"╰━━━━━━━━━━━━━━"
            )

        
        bot.reply_to(message, response_text)

    except IndexError:
        
        bot.reply_to(message, "Lütfen geçerli bir TC kimlik numarası girin.")
    except Exception as e:
        
        bot.reply_to(message, f"Bilgiler Bulunamadı")
        
        
    
    
    
@bot.message_handler(commands=['ig'])
def aile(message):
    chat_id = message.chat.id

    if len(message.text.split()) <= 1:
        bot.send_message(chat_id, "⚠️ *Lütfen Geçerli Bir Kullanıcı Adı Girin.*\n\n*Örnek:*` /ig amedskofficial`", parse_mode="Markdown")# Kullanıcı adı yoksa mesaj gönder
        return

    tc_number = message.text.split()[1]
    url = f'http://api.hexnox.pro/sowixapi/instgram.php?search={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        text = response.content.decode('utf-8-sig')
        result = json.loads(text)
        
        if isinstance(result, list) and len(result) > 0:
            member = result[0]
            profile_pic_url = member.get('profile_pic_url', '')
            bot.send_photo(chat_id, profile_pic_url)
            
            formatted_message = (
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ İSİM: {member.get('full_name', 'Bilinmiyor')}\n"
                f"┃➥ USERNAME: {member.get('username', 'Bilinmiyor')}\n"
                f"┃➥ İD: {member.get('id', 'Bilinmiyor')}\n"
                f"┃➥ GİZLİ HESAP: {'Evet' if member.get('is_private') else 'Hayır'}\n"
                f"┃➥ MAVİ TİK: {'Evet' if member.get('is_verified') else 'Hayır'}\n"
                f"╰─━━━━━━━━━━━━━━\n"
            )
            bot.send_message(chat_id, formatted_message)
        else:
            bot.send_message(chat_id, "⚠️ *Veri Bulunamadı.*", parse_mode="Markdown")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        bot.send_message(chat_id, "⚠️ *Bir hata oluştu. Lütfen daha sonra tekrar deneyin.*", parse_mode="Markdown")
    except json.JSONDecodeError:
        bot.send_message(chat_id, "⚠️ *Lütfen Geçerli Bir Kullanıcı Adı Girin.*\n\n*Örnek:* /ig amedskofficial", parse_mode="Markdown")

   

    
import requests
import os

@bot.message_handler(commands=['ses'])
def ses_cevir(message):
    chat_id = message.chat.id
    # Komutun yanında bir mesaj var mı kontrol et
    if len(message.text.split()) > 1:
        # Mesajı al ve API'ye gönder
        text = " ".join(message.text.split()[1:])
        url = f'https://tilki.dev/api/yaziyi-ses-yapma?text={text}'
        
        try:
            # Ses dosyasını indir
            response = requests.get(url)
            response.raise_for_status()
            
            # Gelen veriyi bir ses dosyasına kaydet
            with open('mesaj_sesi.mp3', 'wb') as f:
                f.write(response.content)

            # Bot ile ses dosyasını gönder
            with open('mesaj_sesi.mp3', 'rb') as audio_file:
                bot.send_voice(chat_id, audio_file)

            # İşlem bittikten sonra dosyayı sil
            os.remove('mesaj_sesi.mp3')

        except requests.exceptions.HTTPError:
            bot.send_message(chat_id, "⚠️ Ses oluşturma sırasında bir hata oluştu.")
        except requests.exceptions.RequestException as err:
            bot.send_message(chat_id, f"⚠️ Beklenmeyen bir hata oluştu: {err}")
    else:
        # Kullanıcı sadece /ses yazdıysa hata mesajı göster
        bot.send_message(chat_id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/ses Biji Serok Apo`", parse_mode='Markdown')

          
                  
@bot.message_handler(commands=['index'])
def index(message):
    if message.chat.type != "private":
        return

    

    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir Site URL girin!*\n\n*Örnek:* `/index https://google.com`", parse_mode="Markdown")
        return

    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm Hatalı URL girdiniz Lütfen geçerli bir URL girin*\n\n*Örnek*: `/index https://instagram.com`", parse_mode="Markdown")
        return

    response = requests.get(site_url)

    if response.status_code == 200:
        file_name = "alemdar.html"
        file_content = response.text
        
        with open(file_name, 'w') as file:
            file.write(file_content)

        with open(file_name, 'rb') as file:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_document(message.chat.id, file)

        os.remove(file_name)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm bu siteye Ait Bir index Çekilemiyor!*", parse_mode='Markdown')



support_channel_id = -1002122807954

@bot.message_handler(commands=['sms']) # 
def send_sms(message):
    chat_id = message.chat.id
    user_input = message.text.split(' ', 1)

    if len(user_input) != 2:
        bot.send_message(chat_id, '*⚠️ Lütfen Geçerli Bir telefon numarası girin!\n\nÖrnek:* `/sms 5555555555`', parse_mode='Markdown')
        return

    gsm_number = user_input[1]
    api_url = f'https://sowixapi.online/api/sowixapi/sms.php?telno={gsm_number}'

    
    start_message = bot.send_message(chat_id, "Smsler Gönderiliyor...")

    
    response = requests.get(api_url)

    if response.status_code == 200:
        
        bot.send_message(chat_id, "Smsler Başarılı Bir Şekilde Gönderildi!\n\n@polatalemdar330 </>")
    else:
        bot.send_message(chat_id, "SMS gönderirken bir hata oluştu.") #                                                                                                                                                                             
   
@bot.callback_query_handler(func=lambda call: call.data == "geri")
def geri(call):
    mesaj = "👋 Merhaba! Benim adım Polat Hack bot sorgu yapmak için buradayım\nBeni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\nEn son güncellemeler hakkında bilgi almak için @devillerden kanalıma katılın.\n\n⛔ Not: Bot Dijvarhack  kanalına özel olarak yapılmıştır. Botu kullanmak için Dijvar Hack'e katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız."
    komutlar = telebot.types.InlineKeyboardButton("📜Komutlar", callback_data="komutlar")
    majeste_sohbet = telebot.types.InlineKeyboardButton(" ➕ beni grubuna ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
    iletisim = telebot.types.InlineKeyboardButton("🙋owner", url="https://t.me/polatalemdar330")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.row(komutlar)
    butonlar.row(majeste_sohbet, iletisim)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_log:"))
def copy_log_callback(call):
    try:
        # Callback data'dan log ID'yi al
        log_id = call.data.replace("copy_log:", "")
        
        # Geçici storage'dan log içeriğini al
        if log_id in temp_log_storage:
            log_content = temp_log_storage[log_id]
            
            # Kullanıcıya kopyalanabilir metin gönder
            bot.answer_callback_query(call.id, "✅ Log kopyalandı!")
            bot.send_message(call.message.chat.id, f"```\n{log_content}\n```", parse_mode="Markdown")
            
            # Geçici storage'dan sil (memory tasarrufu için)
            del temp_log_storage[log_id]
        else:
            bot.answer_callback_query(call.id, "❌ Log bulunamadı!")
        
    except Exception as e:
        bot.answer_callback_query(call.id, "❌ Kopyalama hatası!")
     

# Plaka bilgileri (örnek veri)
plaka_bilgileri = {
    "34ABC123": {
        "borç": "2,500 TL",
        "TC": "12345678901", 
        "ad_soyad": "ÖRNEK KİŞİ",
        "ceza": "Hız limiti aşımı",
        "marka_model": "TOYOTA COROLLA",
        "renk": "BEYAZ",
        "sigorta_durumu": "Aktif"
    }
}


@bot.message_handler(commands=['plaka'])
def handle_plaka(message):
    text = message.text.split()
    if len(text) < 2:
        bot.reply_to(message,'*⚠️ Lütfen Geçerli Bir Plaka girin!\n\nÖrnek:* `/plaka 34ABC123`', parse_mode='Markdown')
        return
    
    plaka = text[1].upper()  # Plaka numarasını büyük harf yaparak al
    
    # API sorgusu yerine örnek veri dönüyoruz
    if plaka in plaka_bilgileri:
        bilgiler = plaka_bilgileri[plaka]
        
        response_text = "╭─━━━━━━━━━━━━━─╮\n┃@polatalemdarsorgubot - PLAKA BORÇ\n┃─━━━━━━━━━━━━━─\n"
        response_text += (
            f"┃ Plaka: {plaka}\n"
            f"┃ Borç: {bilgiler['borç']}\n"
            f"┃ TC Kimlik No: {bilgiler['TC']}\n"
            f"┃ Ad Soyad: {bilgiler['ad_soyad']}\n"
            f"┃ Ceza: {bilgiler['ceza']}\n"
            f"┃ Marka ve Model: {bilgiler['marka_model']}\n"
            f"┃ Aracın Rengi: {bilgiler['renk']}\n"
            f"┃ Sigorta Durumu: {bilgiler['sigorta_durumu']}\n"
        )
        response_text += "╰─━━━━━━━━━━━━━─╯"
        
        bot.reply_to(message, response_text)
    else:
        bot.reply_to(message, f"*🔍 {plaka} plakası için bilgi bulunamadı.*", parse_mode="Markdown")


@bot.message_handler(commands=['adresadres'])
def adress_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://api.hexnox.pro/sowixapi/adres.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            adres_data = data["data"]
            adres_message = f"""
➥ Kimlik No: {adres_data["TC"]}
➥ Ad Soyad: {adres_data["AdSoyad"]}
➥ Doğum Yeri: {adres_data["DogumYeri"]}
➥ Vergi Numarası:  {adres_data["VergiNumarasi"]}
➥ İkametgah: {adres_data["Ikametgah"]}
➥ auth: @polatalemdar330


"""

            bot.reply_to(message, adres_message)
        else:
            bot.reply_to(message, "Bu TC numarasına ait adres bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/adres 11111111110`', parse_mode='Markdown')
  




API_ENDPOINT = 'https://apis.xditya.me/write?text={}'

@bot.message_handler(commands=['yaz'])
def yaz(message):
    if message.chat.type != "private":
        return

    
    try:
        text = message.text.split(maxsplit=1)[1]
       
        api_url = API_ENDPOINT.format(text)
        response = requests.get(api_url)
        
        if response.status_code == 200:
            bot.send_photo(message.chat.id, response.content)
        else:
            bot.send_message(message.chat.id, "⚠️ *API'de sorun var Lütfen Yönetici ile iletişime geçin!.*", parse_mode="Markdown")
    
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/yaz Ne Mutlu TÜRK'üm Diyene`", parse_mode='Markdown')




@bot.message_handler(commands=['dolar'])
def doviz(message):
    try:
        response = requests.get("https://tilki.dev/api/dolar")
        if response.status_code == 200:
            wizardapi = response.json()
            dolar = wizardapi['dolar']
            bot.send_message(message.chat.id, f"*💸 DOVIZ : 1 DOLAR = {dolar} TL ✅*", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "*API'den veri çekilemedi!*", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")

@bot.message_handler(commands=['log'])
def log_komutu(message):
    args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/log siteadi.com`", parse_mode='Markdown')
        return

    site = args[1]
    url = f"https://devilhazretleri.com/log.php?site={site}"
    
    # Yükleme mesajı gönder
    loading_msg = bot.send_message(message.chat.id, "🔍 *Log bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
    
    try:
        import requests
        resp = requests.get(url, timeout=10)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        içerik = resp.text.strip()
        if not içerik or "Kayıt bulunamadı" in içerik:
            bot.reply_to(message, "Kayıt bulunamadı!")
            return
            
        # Satırları ayıkla, ilk 10 satırı göster
        satirlar = [s for s in içerik.replace("\r", "").split("<br>") if s.strip()]
        mesaj = "\n".join(satirlar[:10])
        if len(satirlar) > 10:
            mesaj += "\n... (devamı var)"
            
        # Eğer mesaj çok uzunsa txt dosyası olarak gönder
        if len(mesaj) > 4000:
            file_name = f"log_{site}.txt"
            full_content = "\n".join(satirlar)
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(full_content)
            with open(file_name, "rb") as f:
                bot.send_document(message.chat.id, f, caption=f"📋 {site} Log Sonuçları")
            os.remove(file_name)  # Dosyayı temizle
        else:
            # Log ID oluştur ve geçici storage'da sakla
            global log_counter
            log_counter += 1
            log_id = f"log_{log_counter}"
            temp_log_storage[log_id] = mesaj
            
            # Kopyalama butonu ekle
            keyboard = types.InlineKeyboardMarkup()
            copy_button = types.InlineKeyboardButton("📋 Kopyala", callback_data=f"copy_log:{log_id}")
            keyboard.add(copy_button)
            bot.reply_to(message, f"<pre>{mesaj}</pre>", parse_mode="HTML", reply_markup=keyboard)
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f"Hata: {e}")


		# Geçerli komutlar listesi
valid_commands = [
    '/start', '/komutlar', '/adsoyad', '/adsoyadil', '/adsoyadililce', '/tc', '/aile', '/sulale', '/es', '/cocuk', '/adres', '/tcpro', '/medeni', '/iban', '/ihbar', '/vergid',
    '/gsmtc', '/tcgsm', '/operator', '/sms', '/arama', '/ip', '/ping', '/portscan', '/leakscan', '/dns', '/defteryaz', '/subdomain', '/qrcode', '/index', '/yaz', '/dolar', '/ig', '/ses', '/yegen', '/plaka', '/log'
]



# Diğer komutlarınız burada olabilir...

# Geçersiz komutları yakalayan handler
@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    if message.text not in valid_commands:
        bot.send_message(message.chat.id, 	"*⚠️ Yanlış komut kullandınız. Komutları görmek için /komutlar yazabilirsiniz.*", parse_mode="Markdown")

	


import logging
logging.basicConfig(level=logging.INFO, filename='bot.log')

def main():
    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            logging.error(f"Hata: {e}")
            time.sleep(1)
import telebot
import requests
import urllib
import time
import random
from datetime import datetime
import hashlib, random
import sqlite3
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from telebot import types
from io import BytesIO
import telebot
import json
import requests
from telebot import types
import time
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from datetime import datetime
from pytz import timezone
from datetime import timedelta
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, request
import telegram
from datetime import datetime, timedelta
import re
import socket
import subprocess
import platform
import threading
import qrcode
from PIL import Image
import base64
import threading
import pytz
import re
import os

# Geçici log storage
temp_log_storage = {}
log_counter = 0

TOKEN = "7436117955:AAGI2XAmBGzkH0M0NztXPZZQmmtBfDqt9jc1"
bot = telebot.TeleBot(TOKEN)

# Kanal ve grup kontrolünü devre dışı bırak - test amaçlı
kanal_kontrolu_aktif = False  # True yaparsan kontrol etmeye başlar

kanal_id = -1002646147395 
grup_id = -1002109722883

print("Bot Dişxwile")

from telebot import TeleBot, types

import telebot
import time

import telebot




@bot.message_handler(commands=['komutlar'])
def start(message):
    try:
        # Kanal kontrolü aktifse kontrol et
        if kanal_kontrolu_aktif:
            try:
                kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
            except:
                # Kanal kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                kanal_katildi = "left"
                
            try:
                grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
            except:
                # Grup kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                grup_katildi = "left"
            
            if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
                mesaj = "Komutları görmek için kanala ve gruba katılmanız gerekiyor. Katıldıktan sonra /komutlar yazarak komutları görebilirsiniz."
                
                kanala_katil = types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/ehliyetkimlikpasaport")
                gruba_katil = types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/dijvarhackchat")
                butonlar = types.InlineKeyboardMarkup()
                butonlar.row(kanala_katil, gruba_katil)
                bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
                return
        
        # Komutlar menüsünü göster
        mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • GSM den T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
        butonlar = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
    
    except Exception as e:
        # Chat bulunamadığında veya başka hata olduğunda komutları direkt göster
        print(f"Chat kontrolü hatası: {e}")
        mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • GSM den T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
        butonlar = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)







@bot.message_handler(commands=['start'])
def start(message):
    try:
        # Kanal kontrolü aktifse kontrol et
        if kanal_kontrolu_aktif:
            try:
                kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
            except:
                # Kanal kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                kanal_katildi = "left"
                
            try:
                grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
            except:
                # Grup kontrolü başarısız olursa, kullanıcının katılmadığını varsay
                grup_katildi = "left"
            
            # Eğer kullanıcı kanala veya gruba katılmadıysa
            if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
                mesaj = (f"Merhaba 👋 {message.from_user.first_name},\n\n"
                         "Beni kullanabilmek için ana kanala ve chat grubuna katılmanız gerekiyor!\n"
                         "Kanala ve chate katılıp /start yazarak tekrar deneyin.")
                
                # Kanal ve grup katılım butonları
                kanala_katil = telebot.types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/ehliyetkimlikpasaport")
                gruba_katil = telebot.types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/dijvarhackchat")
                butonlar = telebot.types.InlineKeyboardMarkup()
                butonlar.row(kanala_katil, gruba_katil)
                
                bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
                return
        
        # Kullanıcı kontrolleri geçti veya kontrol deaktif
        mesaj = ("👋 Merhaba! Benim adım Polat Hack bot, sorgu yapmak için buradayım.\n"
                 "Beni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\n"
                 "En son güncellemeler hakkında bilgi almak için @ehliyetkimlikpasaport kanalıma katılın.\n\n"
                 "⛔ Not: Bot @polatalemdar330'a özel olarak yapılmıştır. "
                 "Botu kullanmak için Polat Hack'a katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız.")
        
        # Gruba ekleme ve diğer butonlar
        majeste_sohbet = telebot.types.InlineKeyboardButton("➕ Beni Grubuna Ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
        iletisim = telebot.types.InlineKeyboardButton("🙋 Owner", url="https://t.me/polatalemdar330")
        komutlar = telebot.types.InlineKeyboardButton("📜 Komutlar", callback_data="komutlar")
        
        butonlar = telebot.types.InlineKeyboardMarkup()
        butonlar.row(komutlar)
        butonlar.row(majeste_sohbet, iletisim)
        
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)

    except telebot.apihelper.ApiTelegramException as e:
        # Chat bulunamadı veya bot kanal/grupa erişim hataları
        if "chat not found" in str(e).lower() or e.error_code == 400:
            print(f"Chat bulunamadı hatası: {e}")
            # Chat kontrolü yapamıyorsak direkt hoş geldin mesajı göster
            mesaj = ("👋 Merhaba! Benim adım Polat Hack bot, sorgu yapmak için buradayım.\n"
                     "Beni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\n"
                     "⛔ Not: Bot @polatalemdar330'a özel olarak yapılmıştır.")
            
            majeste_sohbet = telebot.types.InlineKeyboardButton("➕ Beni Grubuna Ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
            iletisim = telebot.types.InlineKeyboardButton("🙋 Owner", url="https://t.me/polatalemdar330")
            komutlar = telebot.types.InlineKeyboardButton("📜 Komutlar", callback_data="komutlar")
            
            butonlar = telebot.types.InlineKeyboardMarkup()
            butonlar.row(komutlar)
            butonlar.row(majeste_sohbet, iletisim)
            
            bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
        # Eğer bot, kullanıcının engellediği bir mesajı gönderirse 403 hatasını yakala
        elif e.error_code == 403 and "bot was blocked by the user" in str(e):
            print(f"Bot {message.from_user.id} tarafından engellendi.")
        else:
            # Diğer hataları işlemeye devam et
            print(f"Bir hata oluştu: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")
        # Herhangi bir hata durumunda basit hoş geldin mesajı
        mesaj = "👋 Merhaba! Bot aktif. Komutlar için /komutlar yazın."
        bot.send_message(message.chat.id, mesaj)






        
def send_long_message(chat_id, text):
    MAX_MESSAGE_LENGTH = 4096  # Telegram mesaj karakter sınırı

    # Mesajı parçalara böl
    for i in range(0, len(text), MAX_MESSAGE_LENGTH):
        bot.send_message(chat_id, text[i:i + MAX_MESSAGE_LENGTH])

@bot.message_handler(commands=['adsoyad'])
def adsoyad_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 3:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad ve soyad girin!\n\nÖrnek:* `/adsoyad ahmet yılmaz`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyad.php?ad={ad}&soyad={soyad}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadsorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad ve soyad için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['adsoyadil'])
def adsoyadil_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 4:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad, soyad ve il girin!\n\nÖrnek:* `/adsoyadil ahmet yılmaz istanbul`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        il = args[3]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyadil.php?ad={ad}&soyad={soyad}&il={il}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad il bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad İl Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadilsorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} {il} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad, soyad ve il için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['adsoyadililce'])
def adsoyadililce_sorgu(message):
    try:
        chat_id = message.chat.id
        args = message.text.split()
        
        if len(args) < 5:
            bot.send_message(chat_id, "*⚠️ Lütfen geçerli bir ad, soyad, il ve ilçe girin!\n\nÖrnek:* `/adsoyadililce ahmet yılmaz istanbul kadıköy`", parse_mode="Markdown")
            return
            
        ad = args[1]
        soyad = args[2]
        il = args[3]
        ilce = args[4]
        
        url = f"http://api.hexnox.pro/sowixapi/adsoyadililce.php?ad={ad}&soyad={soyad}&il={il}&ilce={ilce}"
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Ad soyad il ilçe bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            response_text = response.content.decode('utf-8-sig')
            result = json.loads(response_text)
            
            if result.get('success') and result.get('data'):
                data = result['data']
                total_results = len(data)
                
                formatted_message = f"🔍 **Ad Soyad İl İlçe Sorgu Sonucu**\n👥 Toplam: {total_results} Kişi\n\n"
                
                for person in data:
                    formatted_message += (
                        f"╭━━━━━━━━━━━━━━\n"
                        f"┃➥ ID: {person.get('ID', 'Bilinmiyor')}\n"
                        f"┃➥ TC: `{person.get('TC', 'Bilinmiyor')}`\n"
                        f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                        f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                        f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                        f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                        f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                        f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                        f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                        f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                        f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                        f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                        f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                        f"╰━━━━━━━━━━━━━━\n\n"
                    )
                
                if len(formatted_message) > 4000:
                    file_path = "adsoyadililcesorgu.txt"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(formatted_message)
                    with open(file_path, 'rb') as f:
                        bot.send_document(chat_id, f, caption=f"📋 {ad} {soyad} {il} {ilce} Sorgu Sonuçları")
                    os.remove(file_path)
                else:
                    bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ Bu ad, soyad, il ve ilçe için bilgi bulunamadı.")
        else:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API yanıtı alınamadı.")
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"⚠️ Bir hata oluştu: {str(e)}")

@bot.message_handler(commands=['tc'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tc.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            text = response.content.decode('utf-8-sig')
            result = json.loads(text)
            
            if result.get("success") and "data" in result:
                member = result["data"]
                
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                formatted_message += (
                    f"┃➥ TC: {member.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ AD: {member.get('AD', 'Bilinmiyor')}\n"
                    f"┃➥ SOYAD: {member.get('SOYAD', 'Bilinmiyor')}\n"
                    f"┃➥ BABA ADI: {member.get('BABAADI', 'Bilinmiyor')}\n"
                    f"┃➥ BABA TC: {member.get('BABATC', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE ADI: {member.get('ANNEADI', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE TC: {member.get('ANNETC', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İL: {member.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İLÇE: {member.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                )
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
                
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/tc 11111111110`", parse_mode="Markdown")

import os

def send_long_message_or_file(chat_id, text, file_name="output.txt"):
    MAX_MESSAGE_LENGTH = 4096  # Telegram mesaj karakter sınırı

    if len(text) > MAX_MESSAGE_LENGTH:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
        with open(file_name, 'rb') as f:
            bot.send_document(chat_id, f)
        os.remove(file_name)
    else:
        bot.send_message(chat_id, text)

@bot.message_handler(commands=['aile'])
def aile(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir TC kimlik numarası girin.*\n\n*Örnek:* `/aile 11111111110`", parse_mode="Markdown")
        return

    tc_number = parts[1]
    url = f'http://api.hexnox.pro/sowixapi/aile.php?tc={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *Aile bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)  # Timeout artırıldı
        response.raise_for_status()

        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)
        
        result = response.json()

        if not result.get("success") or "data" not in result:
            bot.send_message(chat_id, "❌ Aile bilgisi bulunamadı.")
            return

        members = result["data"]

        if not isinstance(members, list) or len(members) == 0:
            bot.send_message(chat_id, "❌ Aile üyesi bulunamadı.")
            return

        formatted_message = f"👨‍👩‍👧‍👦 *Toplam Aile Üyesi:* {len(members)}\n\n"

        for i, member in enumerate(members, start=1):
            formatted_message += (
                f"🔹 *{i}. Üye: {member.get('Yakınlık', 'Bilinmiyor')}*\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *ID:* {member.get('ID', '-')}\n"
                f"┃➥ *TC:* `{member.get('TC', '-')}`\n"
                f"┃➥ *Ad:* {member.get('AD', '-')}\n"
                f"┃➥ *Soyad:* {member.get('SOYAD', '-')}\n"
                f"┃➥ *GSM:* {member.get('GSM', '-')}\n"
                f"┃➥ *Baba Adı:* {member.get('BABAADI', '-')}\n"
                f"┃➥ *Baba TC:* {member.get('BABATC', '-')}\n"
                f"┃➥ *Anne Adı:* {member.get('ANNEADI', '-')}\n"
                f"┃➥ *Anne TC:* {member.get('ANNETC', '-')}\n"
                f"┃➥ *Doğum Tarihi:* {member.get('DOGUMTARIHI', '-')}\n"
                f"┃➥ *Ölüm Tarihi:* {member.get('OLUMTARIHI', 'YOK')}\n"
                f"┃➥ *Doğum Yeri:* {member.get('DOGUMYERI', '-')}\n"
                f"┃➥ *Memleket İl:* {member.get('MEMLEKETIL', '-')}\n"
                f"┃➥ *Memleket İlçe:* {member.get('MEMLEKETILCE', '-')}\n"
                f"┃➥ *Memleket Köy:* {member.get('MEMLEKETKOY', '-')}\n"
                f"┃➥ *Adres İl:* {member.get('ADRESIL', '-')}\n"
                f"┃➥ *Adres İlçe:* {member.get('ADRESILCE', '-')}\n"
                f"┃➥ *Ailesi Sıra No:* {member.get('AILESIRANO', '-')}\n"
                f"┃➥ *Birey Sıra No:* {member.get('BIREYSIRANO', '-')}\n"
                f"┃➥ *Medeni Hal:* {member.get('MEDENIHAL', '-')}\n"
                f"┃➥ *Cinsiyet:* {member.get('CINSIYET', '-')}\n"
                f"╰━━━━━━━━━━━━━━\n\n"
            )

        # Uzunsa dosya olarak gönder
        if len(formatted_message) > 4000:
            file_name = "aile_sorgu.txt"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(formatted_message)
            with open(file_name, "rb") as f:
                bot.send_document(chat_id, f, caption="📋 Aile Sorgu Sonuçları")
            os.remove(file_name)  # Dosyayı temizle
        else:
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")
	



import requests
import json

@bot.message_handler(commands=['sulale'])
def sulale_sorgu(message):
    chat_id = message.chat.id
    args = message.text.split()

    if len(args) != 2:
        bot.send_message(
            chat_id,
            "⚠️ *Lütfen geçerli bir TC Kimlik Numarası girin.*\n\n*Örnek:* `/sulale 11111111110`",
            parse_mode="Markdown"
        )
        return

    tc_number = args[1]
    url = f'https://api.hexnox.pro/sowixapi/sulale.php?tc={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Önce kullanıcıya bekleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *Sülale bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        # Yeniden deneme mekanizması
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, timeout=30)  # Timeout 30 saniyeye çıkarıldı
                response.raise_for_status()
                result = response.json()
                break  # Başarılı olursa döngüden çık
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:  # Son deneme değilse
                    bot.edit_message_text(
                        f"⏳ *Bağlantı yavaş, tekrar deneniyor... ({attempt + 2}/{max_retries})*",
                        chat_id, loading_msg.message_id, parse_mode="Markdown"
                    )
                    continue
                else:
                    raise  # Son denemeyse hatayı fırlat
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    bot.edit_message_text(
                        f"⚠️ *Bağlantı hatası, tekrar deneniyor... ({attempt + 2}/{max_retries})*",
                        chat_id, loading_msg.message_id, parse_mode="Markdown"
                    )
                    continue
                else:
                    raise

        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        # API direkt liste döndürüyorsa
        if isinstance(result, list):
            members = result
        # API dict formatında döndürüyorsa
        elif isinstance(result, dict):
            if not result.get("success"):
                bot.send_message(chat_id, "❌ Sülale bilgisi bulunamadı.")
                return
            
            # Data alanını kontrol et
            data = result.get("data")
            if not data:
                bot.send_message(chat_id, "❌ Sülale verisi boş.")
                return
                
            # Eğer data bir liste değilse, liste haline getir
            if not isinstance(data, list):
                data = [data]
                
            members = data
        else:
            bot.send_message(chat_id, "❌ Beklenmeyen API yanıt formatı.")
            return
        
        # Veri yapısını kontrol et
        if not members or len(members) == 0:
            bot.send_message(chat_id, "❌ Sülale bilgisi bulunamadı.")
            return
            
        formatted_message = f"🌳 *Toplam Sülale Üyesi:* {len(members)}\n\n"

        for i, member in enumerate(members, start=1):
            # member'ın sözlük olup olmadığını kontrol et
            if not isinstance(member, dict):
                formatted_message += f"🔹 *{i}. Üye: Veri Formatı Hatası*\n\n"
                continue
            
            # Güvenli veri alımı için fonksiyon
            def safe_get(key, default='-'):
                value = member.get(key, default)
                return value if value and str(value).strip() else default
                
            formatted_message += (
                f"🔹 *{i}. Üye: {safe_get('YAKINLIK', 'Bilinmiyor')}*\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *TC:* `{safe_get('TC')}`\n"
                f"┃➥ *Ad:* {safe_get('AD')}\n"
                f"┃➥ *Soyad:* {safe_get('SOYAD')}\n"
                f"┃➥ *Doğum Tarihi:* {safe_get('DOGUMTARIHI')}\n"
                f"┃➥ *Memleket İl:* {safe_get('MEMLEKETIL')}\n"
                f"┃➥ *Memleket İlçe:* {safe_get('MEMLEKETILCE')}\n"
                f"┃➥ *Anne Adı:* {safe_get('ANNEADI')}\n"
                f"┃➥ *Anne TC:* {safe_get('ANNETC')}\n"
                f"┃➥ *Baba Adı:* {safe_get('BABAADI')}\n"
                f"┃➥ *Baba TC:* {safe_get('BABATC')}\n"
                f"┃➥ *Uyruk:* {safe_get('UYRUK', 'T.C.')}\n"
                f"╰━━━━━━━━━━━━━━\n\n"
            )

        # Uzunsa dosya olarak gönder, kısaysa direkt mesaj gönder
        if len(formatted_message) > 4000:
            file_name = "sulale_sorgu.txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(formatted_message)

            with open(file_name, "rb") as file:
                bot.send_document(chat_id, file, caption="🌳 Sülale Sorgu Sonuçları")
            
            os.remove(file_name)  # Dosyayı temizle
        else:
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as err:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"🚫 *API bağlantı hatası:*\n`{str(err)[:100]}...`", parse_mode="Markdown")
    except KeyError as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Veri yapısı hatası: {e}")
    except TypeError as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Veri tipi hatası: {e}")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")


import requests
import json

@bot.message_handler(commands=['tcpro'])
def tcpro_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tcpro.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC Pro bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)

            response.encoding = 'utf-8-sig'
            json_data = response.text

            result = json.loads(json_data)

            if result.get("success") and result.get("data"):
                person = result["data"]  # Artık data direkt obje

                # İstenen formatta mesaj oluşturma
                formatted_message = (
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ AD: {person.get('AD', 'Bilinmiyor')}\n"
                    f"┃➥ SOYAD: {person.get('SOYAD', 'Bilinmiyor')}\n"
                    f"┃➥ GSM: {person.get('GSM', 'Bilinmiyor')}\n"
                    f"┃➥ BABA ADI: {person.get('BABAADI', 'Bilinmiyor')}\n"
                    f"┃➥ BABA TC: {person.get('BABATC', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE ADI: {person.get('ANNEADI', 'Bilinmiyor')}\n"
                    f"┃➥ ANNE TC: {person.get('ANNETC', 'Bilinmiyor')}\n"
                    f"┃➥ DOĞUM TARİHİ: {person.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                    f"┃➥ ÖLÜM TARİHİ: {person.get('OLUMTARIHI', 'YOK')}\n"
                    f"┃➥ DOĞUM YERİ: {person.get('DOGUMYERI', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İL: {person.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET İLÇE: {person.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                    f"┃➥ MEMLEKET KÖY: {person.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES İL: {person.get('ADRESIL', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES İLÇE: {person.get('ADRESILCE', 'Bilinmiyor')}\n"
                    f"┃➥ AİLE SIRA NO: {person.get('AILESIRANO', 'Bilinmiyor')}\n"
                    f"┃➥ BİREY SIRA NO: {person.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                    f"┃➥ MEDENİ HAL: {person.get('MEDENIHAL', 'Bilinmiyor')}\n"
                    f"┃➥ CİNSİYET: {person.get('CINSIYET', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )

                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "🔍 TC Pro bilgisi bulunamadı.")
        except requests.exceptions.HTTPError:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "⚠️ API isteği sırasında bir hata oluştu.")
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"⚠️ Beklenmeyen bir hata oluştu: {err}")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/tcpro 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['medeni'])
def medeni_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/medeni.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Medeni hal bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            result = response.json()
            
            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                person = result["data"][0]
                formatted_message = (
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ ADI: {person.get('ADI', 'Bilinmiyor')}\n"
                    f"┃➥ SOYADI: {person.get('SOYADI', 'Bilinmiyor')}\n"
                    f"┃➥ MEDENI HALI: {person.get('MEDENI_HALI', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "*🔍 Belirtilen TC kimlik numarası için medeni hal bilgisi bulunamadı.*", parse_mode="Markdown")
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/medeni 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['cocuk'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/es.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Çocuk bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # JSON verisini ayıklayın
            result = response.json()

            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                # Verileri ayrıştır
                children = [member for member in result["data"] if member.get('YAKINLIK') == 'Çocuğu']
                
                # Formatted message
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                
                # Eğer çocuklar varsa, her birini ekle
                if children:
                    for child in children:
                        formatted_message += (
                            f"┃➥ Yakınlık: Çocuğu\n"
                            f"┃➥ TC: {child.get('TC', 'Bilinmiyor')}\n"
                            f"┃➥ AD: {child.get('ADI', 'Bilinmiyor')}\n"
                            f"┃➥ SOYAD: {child.get('SOYADI', 'Bilinmiyor')}\n"
                            f"┃➥ DOĞUM TARİHİ: {child.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                            f"┃➥ İL: {child.get('NUFUSIL', 'Bilinmiyor')}\n"
                            f"┃➥ İLÇE: {child.get('NUFUSILCE', 'Bilinmiyor')}\n"
                            f"┃➥ UYRUK: {child.get('Uyruk', 'Bilinmiyor')}\n"
                            "┃━━━━━━━━━━━━━━\n"
                        )
                else:
                    formatted_message += "┃➥ Çocuk bilgisi bulunamadı.\n"

                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/cocuk 11111111110`", parse_mode="Markdown")




@bot.message_handler(commands=['es'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/es.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Eş bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # JSON verisini ayıklayın
            result = response.json()

            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                # Verileri ayrıştır
                eşi = [member for member in result["data"] if member.get('YAKINLIK') == 'Eşi']
                
                # Formatted message
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                
                # Eş bilgisi
                if eşi:
                    member = eşi[0]
                    formatted_message += (
                        f"┃➥ Yakınlık: Eşi\n"
                        f"┃➥ TC: {member.get('TC', 'Bilinmiyor')}\n"
                        f"┃➥ AD: {member.get('ADI', 'Bilinmiyor')}\n"
                        f"┃➥ SOYAD: {member.get('SOYADI', 'Bilinmiyor')}\n"
                        f"┃➥ DOĞUM TARİHİ: {member.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                        f"┃➥ İL: {member.get('NUFUSIL', 'Bilinmiyor')}\n"
                        f"┃➥ İLÇE: {member.get('NUFUSILCE', 'Bilinmiyor')}\n"
                        f"┃➥ UYRUK: {member.get('Uyruk', 'Bilinmiyor')}\n"
                    )
                else:
                    formatted_message += "┃➥ Eş bilgisi bulunamadı.\n"
                
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
        except requests.exceptions.HTTPError as errh:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')
        except requests.exceptions.ConnectionError as errc:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Bağlantı Hatası: ')
        except requests.exceptions.Timeout as errt:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Zaman Aşımı Hatası: ')
        except requests.exceptions.RequestException as err:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Hata! Genel Hata: {err}')
        except ValueError as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Geçersiz JSON yanıtı. Hata: ')
        except Exception as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f'Beklenmeyen bir hata oluştu. Hata: ')
    else:
        bot.send_message(chat_id,  "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/es 11111111110`", parse_mode="Markdown")



@bot.message_handler(commands=['adres'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/adres.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *Adres bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTPError için
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            text = response.content.decode('utf-8-sig')
            result = json.loads(text)
            
            if result.get("success") and "data" in result:
                member = result["data"]
                
                formatted_message = "╭━━━━━━━━━━━━━━\n"
                formatted_message += (
                    f"┃➥ TC: {member.get('KimlikNo', 'Bilinmiyor')}\n"
                    f"┃➥ AD SOYAD: {member.get('AdSoyad', 'Bilinmiyor')}\n"
                    f"┃➥ DOĞUM YERİ: {member.get('DogumYeri', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ NO: {member.get('VergiNumarasi', 'Bilinmiyor')}\n"
                    f"┃➥ ADRES: {member.get('Ikametgah', 'Bilinmiyor')}\n"
                    f"┃ \n"
                )
                formatted_message += "╰━━━━━━━━━━━━━━"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "⚠️*Veri Bulunamadı.*", parse_mode="Markdown")
        
        except requests.exceptions.RequestException:
            bot.send_message(chat_id, "⚠️*Bir hata oluştu. Lütfen daha sonra tekrar deneyin.*", parse_mode="Markdown")
        except json.JSONDecodeError:
            bot.send_message(chat_id, "⚠️*API yanıtı işlenemedi.*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/adres 11111111110`", parse_mode="Markdown")

        

@bot.message_handler(commands=['iban'])
def iban(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        iban_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/iban.php?iban={iban_number}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *IBAN bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # İstek başarısız olursa bir hata fırlatılır
            
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            result = response.content.decode('utf-8-sig')  # UTF-8 BOM'u temizler
            result_json = json.loads(result)  # JSON verisi düzgün bir şekilde işlenir
            
            if result_json:
                banka = result_json.get('BANKA', {})
                sube = result_json.get('ŞUBE', {})
                
                formatted_message = (
                    f"╔══════════════╗\n"
                    f"║ IBAN Bilgileri\n"
                    f"╠══════════════╣\n"
                    f"║ Banka Adı: {banka.get('Adı', 'Bilinmiyor')}\n"
                    f"║ Banka Kod: {banka.get('Kod', 'Bilinmiyor')}\n"
                    f"║ Swift: {banka.get('Swift', 'Bilinmiyor')}\n"
                    f"║ Hesap No: {banka.get('Hesap No', 'Bilinmiyor')}\n"
                    f"║ Şube Adı: {sube.get('Ad', 'Bilinmiyor')}\n"
                    f"║ Şube Kod: {sube.get('Kod', 'Bilinmiyor')}\n"
                    f"║ İl: {sube.get('İl', 'Bilinmiyor')}\n"
                    f"║ İlçe: {sube.get('İlçe', 'Bilinmiyor')}\n"
                    f"║ Tel: {sube.get('Tel', 'Bilinmiyor')}\n"
                    f"║ Fax: {sube.get('Fax', 'Bilinmiyor')}\n"
                    f"║ Adres: {sube.get('Adres', 'Bilinmiyor')}\n"      
                    f"╚══════════════╝\n"
                    f"@devillerden"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz IBAN numarası veya veri bulunamadı.")
        except requests.exceptions.RequestException as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"API isteği başarısız: {str(e)}")
        except (KeyError, ValueError):
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, "Geçersiz API yanıtı veya IBAN numarası bulunamadı.")
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir IBAN Numarası girin!\n\nÖrnek:* `/iban TR560001002247786851675002`', parse_mode='Markdown')


@bot.message_handler(commands=['ihbar'])
def ihbar_gonder(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        adres = ' '.join(message.text.split()[1:])
        url = f'http://api.hexnox.pro/sowixapi/ihbar.php?adres={adres}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get("success"):
                formatted_message = (
                    f"✅ *İhbar Başarıyla Gönderildi*\n\n"
                    f"📍 *Adres:* {adres}\n"
                    f"📅 *Tarih:* {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
                    f"🚨 *Durum:* İşleme Alındı\n\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "*❌ İhbar gönderilemedi. Lütfen tekrar deneyin.*", parse_mode="Markdown")
        except Exception as e:
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen bir adres girin*.\n\n*Örnek:* `/ihbar Atatürk Mahallesi İstanbul`", parse_mode="Markdown")


@bot.message_handler(commands=['vergid'])
def vergi_sorgu(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/vergi.php?tc={tc_number}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get("success") and isinstance(result.get("data"), list) and len(result["data"]) > 0:
                person = result["data"][0]
                formatted_message = (
                    f"💰 *Vergi Bilgileri*\n\n"
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃➥ TC: {person.get('TC', 'Bilinmiyor')}\n"
                    f"┃➥ ADI: {person.get('ADI', 'Bilinmiyor')}\n"
                    f"┃➥ SOYADI: {person.get('SOYADI', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ DAİRESİ: {person.get('VERGI_DAIRESI', 'Bilinmiyor')}\n"
                    f"┃➥ VERGİ NO: {person.get('VERGI_NO', 'Bilinmiyor')}\n"
                    f"┃➥ GELİR DİLİMİ: {person.get('GELIR_DILIMI', 'Bilinmiyor')}\n"
                    f"╰━━━━━━━━━━━━━━\n"
                    f"@polatalemdarsorgubot"
                )
                bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "*🔍 Belirtilen TC kimlik numarası için vergi bilgisi bulunamadı.*", parse_mode="Markdown")
        except Exception as e:
            bot.send_message(chat_id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id,"⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/vergid 11111111110`", parse_mode="Markdown")


@bot.message_handler(commands=['tcgsm'])
def tcgsm(message):
    chat_id = message.chat.id
    
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://api.hexnox.pro/sowixapi/tcgsm.php?tc={tc_number}'
        
        # User-Agent başlığını ekliyoruz
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(chat_id, "🔍 *TC'den GSM sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        response = requests.get(url, headers=headers)
        
        try:
            # Yükleme mesajını sil
            bot.delete_message(chat_id, loading_msg.message_id)
            
            # Yanıtı ham olarak al ve UTF-8 BOM'dan temizle
            raw_response = response.content
            response_text = raw_response.decode('utf-8-sig')
            
            # Yanıtı terminalde bas


            # JSON verisini işleyin
            result = json.loads(response_text)
            print(f"Parsed JSON: {result}")

            # Yanıtın formatını kontrol et
            if isinstance(result, dict) and result.get("success") and isinstance(result.get("data"), list):
                data = result['data']
                
                # TC numarasını ve GSM numaralarını listeleyin
                formatted_message = f"╭━━━━━━━━━━━━━━\n┃➥TC: `{tc_number}`\n"
                
                for entry in data:
                    gsm = entry.get('GSM', 'Bilinmiyor')
                    formatted_message += f"┃➥GSM: `{gsm}`\n"
                
                formatted_message += "╰━━━━━━━━━━━━━━\n"
                
                bot.send_message(chat_id, formatted_message, parse_mode='Markdown')
            else:
                bot.send_message(chat_id, "⚠️ Geçersiz TC numarası veya veri bulunamadı.")

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            # Yükleme mesajını sil
            try:
                bot.delete_message(chat_id, loading_msg.message_id)
            except:
                pass
            bot.send_message(chat_id, f"⚠️ Geçersiz API yanıtı veya TC numarası bulunamadı. Hata: {e}")
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tcgsm 11111111110`', parse_mode='Markdown')



@bot.message_handler(commands=['gsmtc'])
def gsmtc_sorgu(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir GSM numarası girin.*\n\n*Örnek:* `/gsmtc 5553723339`", parse_mode="Markdown")
        return

    gsm_number = parts[1]
    url = f'http://api.hexnox.pro/sowixapi/gsm.php?gsm={gsm_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *GSM numarası sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        result = response.json()

        if result.get('success') and result.get('data'):
            data = result['data']
            
            formatted_message = (
                f"📱 *GSM Sorgu Sonucu*\n\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *GSM:* {data.get('GSM', '-')}\n"
                f"┃➥ *TC:* `{data.get('TC', '-')}`\n"
                f"╰━━━━━━━━━━━━━━\n"
                f"@polatalemdarsorgubot"
            )
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ Bu GSM numarası için TC bilgisi bulunamadı.")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")


@bot.message_handler(commands=['operator'])
def operator(message):
    if message.chat.type != "private":
        return

    gsm_number = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm_number:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM numarası girin!.\nÖrnek:* `/operator 5553723339`', parse_mode="Markdown")
        return

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(message.chat.id, "🔍 *Operatör bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        api_url = f"http://api.hexnox.pro/sowixapi/operator.php?gsm={gsm_number}"
        headers = {
            'User-Agent': 'YourAppName/1.0'
        }
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Yanıtı bir dosyaya yazma
        with open('response.json', 'wb') as file:
            file.write(response.content)

        # Dosyadan okuma ve BOM karakterlerini temizleme
        with open('response.json', 'r', encoding='utf-8-sig') as file:
            response_text = file.read()

        # JSON yanıtını işleme
        data = json.loads(response_text)

        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)

        # API yanıtında 'operator' anahtarı varsa
        if data and 'operator' in data:
            result_text = (
                f"╭─━━━━━━━━━━━━─╮\n"
                f"┃*GSM:* `{data.get('gsm', 'Bilinmiyor')}`\n"
                f"┃*Operatör:* `{data.get('operator', 'Bilinmiyor')}`\n"
                f"╰─━━━━━━━━━━━━─╯"
            )
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, result_text, parse_mode="Markdown")
        else:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz bilgiler ile eşleşen bir operatör bulunamadı!*', parse_mode="Markdown")

    except requests.exceptions.HTTPError as errh:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'SEN KİMİN APİSİNİ ARAKLAMAYA ÇALIŞIYORSUN ORUSPU EVLADI ')

    except requests.exceptions.ConnectionError as errc:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, f'⚠️ *Bir hata oluştu: {str(e)}*', parse_mode="Markdown")


@bot.message_handler(commands=['gsmdetay'])
def gsmdetay_sorgu(message):
    chat_id = message.chat.id
    parts = message.text.strip().split(maxsplit=1)

    if len(parts) < 2:
        bot.send_message(chat_id, "⚠️ *Lütfen geçerli bir GSM numarası girin.*\n\n*Örnek:* `/gsmdetay 5553723339`", parse_mode="Markdown")
        return

    gsm_number = parts[1]
    url = f'https://api.hexnox.pro/sowixapi/gsmdetay.php?gsm={gsm_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Yükleme mesajı gönder
    loading_msg = bot.send_message(chat_id, "🔍 *GSM detay bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Yükleme mesajını sil
        bot.delete_message(chat_id, loading_msg.message_id)

        result = response.json()

        if result.get('success') and result.get('Data'):
            data = result['Data']
            
            formatted_message = (
                f"📱 *GSM Detay Sorgu Sonucu*\n\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ *TC:* `{data.get('TC', '-')}`\n"
                f"┃➥ *Ad:* {data.get('AD', '-')}\n"
                f"┃➥ *Soyad:* {data.get('SOYAD', '-')}\n"
                f"┃➥ *Doğum Tarihi:* {data.get('DOGUMTARIHI', '-')}\n"
                f"┃➥ *Adres İl:* {data.get('ADRESIL', '-')}\n"
                f"┃➥ *Adres İlçe:* {data.get('ADRESILCE', '-')}\n"
                f"┃➥ *Anne Adı:* {data.get('ANNEADI', '-')}\n"
                f"┃➥ *Anne TC:* {data.get('ANNETC', '-')}\n"
                f"┃➥ *Baba Adı:* {data.get('BABAADI', '-')}\n"
                f"┃➥ *Baba TC:* {data.get('BABATC', '-')}\n"
                f"┃➥ *Cinsiyet:* {data.get('CINSIYET', '-')}\n"
                f"┃➥ *Vergi No:* {data.get('VergiNumarasi', '-')}\n"
                f"┃➥ *İkametgah:* {data.get('Ikametgah', '-')}\n"
                f"╰━━━━━━━━━━━━━━\n"
                f"@polatalemdarsorgubot"
            )
            bot.send_message(chat_id, formatted_message, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ Bu GSM numarası için detay bilgisi bulunamadı.")

    except requests.exceptions.Timeout:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "⏰ *Zaman aşımı hatası!* API sunucusu çok yavaş yanıt veriyor. Lütfen daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.ConnectionError:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, "🌐 *Bağlantı hatası!* İnternet bağlantınızı kontrol edin veya daha sonra tekrar deneyin.", parse_mode="Markdown")
    except requests.exceptions.RequestException as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ API bağlantı hatası: {str(e)[:100]}...")
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(chat_id, loading_msg.message_id)
        except:
            pass
        bot.send_message(chat_id, f"❌ Beklenmeyen bir hata oluştu: {e}")



        

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

# Kullanıcıların son komut kullanma zamanlarını saklayacak bir sözlük
last_usage = {}

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return '*Arama gönderildi.*'
    else:
        return '*Arama gönderilemedi.*'

@bot.message_handler(commands=['arama'])
def handle_arama(message):
    user_id = message.from_user.id
    current_time = datetime.now()
    
   # Kullanıcının son komut kullanım zamanı kontrol ediliyor
    if user_id in last_usage:
        last_used = last_usage[user_id]
        if current_time < last_used + timedelta(minutes=1):
            bot.send_message(message.chat.id, "*⚠️ Bu komutu sadece 1 dakikada bir kullanabilirsiniz.*", parse_mode="Markdown")
            return

    try:
        phone_number = message.text.split(' ')[1]
        if not phone_number.startswith('+'):
            raise ValueError
        result = send_spam(phone_number)
        bot.send_message(message.chat.id, result, parse_mode="Markdown")
        
           # Kullanıcının son komut kullanım zamanı güncelleniyor
        last_usage[user_id] = datetime.now()
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Komutu yanlış kullandınız. Doğru kullanım: /arama +905555555555*", parse_mode="Markdown")
    except ValueError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir telefon numarası girin. Örnek: /arama +905555555555*", parse_mode="Markdown")








# IP adresi kontrolü için regex
IP_REGEX = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        ip = message.text.split(' ')[1]
        # IP adresinin geçerli olup olmadığını kontrol et
        if not IP_REGEX.match(ip):
            bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")
            return
        
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        username = message.from_user.username

        response_message = f'''
sorgulanıyor bekleyiniz
'''
        bot.send_message(message.chat.id, response_message)

        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            response_message = f'''
╭━━━━━━━━━━━━━╮
┃➥ @polatalemdar330
┃━━━━━━━━━━━━━━
┃➥ IP: {response['query'] or 'Bulunamadı'}
┃➥ Ülke: {response['country']} - {response['countryCode'] or 'Bulunamadı'}
┃➥ Şehir : {response['regionName'] or 'Bulunamadı'}
┃➥ İlçe: {response["city"] or 'Bulunamadı'}
┃➥ Posta Kodu: {response["zip"] or 'Bulunamadı'}
┃➥ Operatör: {response["isp"] or 'Bulunamadı'}
┃➥ Zaman Türü: {response["timezone"] or 'Bulunamadı'}
┃➥ Koordinatlar: {response["lat"] or 'Bulunamadı'}
╰━━━━━━━━━━━━━╯'''
            bot.send_message(message.chat.id, response_message)

            log_message = f"Yeni IP Adresi Sorgulandı!\n" \
                          f"Sorgulanan IP: {ip}\n" \
                          f"Sorgulayan ID: {user_id}\n" \
                          f"Sorgulayan Adı: {user_name}\n" \
                          f"Sorgulayan K. Adı: @{username}"
            
            bot.send_message(message.chat.id, " Başarıyla sorgulandı ✅")
    except IndexError:
        bot.send_message(message.chat.id,
        "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")


@bot.message_handler(commands=['ping'])
def ping_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir hedef belirtin!*\n\n*Örnek:* `/ping google.com`", parse_mode="Markdown")
            return
            
        target = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Ping işlemi yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Ping komutu çalıştır
        system = platform.system().lower()
        if system == "windows":
            cmd = f"ping -n 4 {target}"
        else:
            cmd = f"ping -c 4 {target}"
            
        result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=30)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if result.returncode == 0:
            # Başarılı ping sonucu
            formatted_message = f"🌐 **Ping Sonucu**\n\n```\n{result.stdout}\n```"
        else:
            formatted_message = f"❌ **Ping Başarısız**\n\n```\n{result.stderr}\n```"
            
        if len(formatted_message) > 4000:
            # Dosya olarak gönder
            with open("ping_result.txt", "w", encoding="utf-8") as f:
                f.write(result.stdout if result.returncode == 0 else result.stderr)
            with open("ping_result.txt", "rb") as f:
                bot.send_document(message.chat.id, f, caption=f"📊 {target} Ping Sonuçları")
            os.remove("ping_result.txt")
        else:
            bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
            
    except subprocess.TimeoutExpired:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, "⏰ *Ping işlemi zaman aşımına uğradı.*", parse_mode="Markdown")
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['portscan'])
def portscan_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir hedef belirtin!*\n\n*Örnek:* `/portscan google.com`", parse_mode="Markdown")
            return
            
        target = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Port taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Yaygın portlar listesi
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 1723, 3389, 5432, 5900, 8080]
        open_ports = []
        
        def scan_port(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                result = sock.connect_ex((host, port))
                sock.close()
                if result == 0:
                    return port
            except:
                pass
            return None
        
        # Port taraması
        with threading.ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(scan_port, target, port) for port in common_ports]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if open_ports:
            open_ports.sort()
            ports_text = ", ".join(map(str, open_ports))
            formatted_message = f"🔓 **Port Tarama Sonucu**\n\n**Hedef:** {target}\n**Açık Portlar:** {ports_text}\n**Toplam:** {len(open_ports)} port"
        else:
            formatted_message = f"🔒 **Port Tarama Sonucu**\n\n**Hedef:** {target}\n**Sonuç:** Açık port bulunamadı"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['leakscan'])
def leakscan_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen sorgulamak istediğiniz veriyi belirtin!*\n\n*Örnek:* `/leakscan email@example.com`", parse_mode="Markdown")
            return
            
        query = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Leak taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # HaveIBeenPwned API (ücretsiz kullanım sınırlı)
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            
            # Yükleme mesajını sil
            bot.delete_message(message.chat.id, loading_msg.message_id)
            
            if response.status_code == 200:
                breaches = response.json()
                if breaches:
                    formatted_message = f"⚠️ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** {len(breaches)} veri ihlali bulundu\n\n"
                    for breach in breaches[:5]:  # İlk 5 sonuç
                        formatted_message += f"• **{breach.get('Name', 'Bilinmiyor')}**\n  Tarih: {breach.get('BreachDate', 'Bilinmiyor')}\n\n"
                else:
                    formatted_message = f"✅ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Veri ihlali bulunamadı"
            elif response.status_code == 404:
                formatted_message = f"✅ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Veri ihlali bulunamadı"
            else:
                formatted_message = f"❌ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** Servis şu anda kullanılamıyor"
                
        except:
            formatted_message = f"❌ **Leak Tarama Sonucu**\n\n**Sorgu:** {query}\n**Durum:** API erişim hatası"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['dns'])
def dns_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir domain belirtin!*\n\n*Örnek:* `/dns google.com`", parse_mode="Markdown")
            return
            
        domain = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *DNS bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # DNS sorgusu için API kullan
        url = f"https://dns.google/resolve?name={domain}&type=A"
        response = requests.get(url, timeout=15)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if response.status_code == 200:
            data = response.json()
            if 'Answer' in data:
                formatted_message = f"🌐 **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n\n"
                for record in data['Answer']:
                    formatted_message += f"**Tip:** {record.get('type', 'Bilinmiyor')}\n"
                    formatted_message += f"**IP:** {record.get('data', 'Bilinmiyor')}\n"
                    formatted_message += f"**TTL:** {record.get('TTL', 'Bilinmiyor')}\n\n"
            else:
                formatted_message = f"❌ **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n**Durum:** DNS kaydı bulunamadı"
        else:
            formatted_message = f"❌ **DNS Sorgu Sonucu**\n\n**Domain:** {domain}\n**Durum:** DNS sorgu hatası"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['defteryaz'])
def defteryaz_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen yazmak istediğiniz metni belirtin!*\n\n*Örnek:* `/defteryaz Merhaba Dünya`", parse_mode="Markdown")
            return
            
        text = args[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Deftere yaz
        with open("defter.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")
            
        bot.send_message(message.chat.id, f"✅ *Metin deftere yazıldı!*\n\n**Yazılan metin:** {text}", parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['subdomain'])
def subdomain_command(message):
    try:
        args = message.text.split()
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir domain belirtin!*\n\n*Örnek:* `/subdomain example.com`", parse_mode="Markdown")
            return
            
        domain = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *Subdomain taraması yapılıyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # Yaygın subdomain'ler
        common_subdomains = ['www', 'mail', 'ftp', 'admin', 'api', 'blog', 'dev', 'test', 'staging', 'app']
        found_subdomains = []
        
        def check_subdomain(subdomain, domain):
            try:
                full_domain = f"{subdomain}.{domain}"
                socket.gethostbyname(full_domain)
                return full_domain
            except:
                return None
        
        # Subdomain kontrolü
        with threading.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(check_subdomain, sub, domain) for sub in common_subdomains]
            for future in futures:
                result = future.result()
                if result:
                    found_subdomains.append(result)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if found_subdomains:
            subdomains_text = "\n• ".join(found_subdomains)
            formatted_message = f"🌐 **Subdomain Tarama Sonucu**\n\n**Domain:** {domain}\n**Bulunan Subdomain'ler:**\n• {subdomains_text}\n\n**Toplam:** {len(found_subdomains)} subdomain"
        else:
            formatted_message = f"❌ **Subdomain Tarama Sonucu**\n\n**Domain:** {domain}\n**Sonuç:** Subdomain bulunamadı"
            
        bot.send_message(message.chat.id, formatted_message, parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=['qrcode'])
def qrcode_command(message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.send_message(message.chat.id, "*⚠️ Lütfen QR kod için metin belirtin!*\n\n*Örnek:* `/qrcode https://example.com`", parse_mode="Markdown")
            return
            
        text = args[1]
        
        # Yükleme mesajı gönder
        loading_msg = bot.send_message(message.chat.id, "🔍 *QR kod oluşturuluyor, lütfen bekleyin...*", parse_mode="Markdown")
        
        # QR kod oluşturma (basit implementasyon - qrcode kütüphanesi olmadan)
        # API kullanarak QR kod oluştur
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={urllib.parse.quote(text)}"
        
        response = requests.get(qr_url, timeout=15)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        if response.status_code == 200:
            # QR kod resmi olarak gönder
            bot.send_photo(message.chat.id, response.content, caption=f"📱 **QR Kod**\n\n**İçerik:** {text}")
        else:
            bot.send_message(message.chat.id, "❌ *QR kod oluşturulamadı.*", parse_mode="Markdown")
        
    except Exception as e:
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.send_message(message.chat.id, f"❌ *Bir hata oluştu:* {str(e)}", parse_mode="Markdown")



@bot.callback_query_handler(func=lambda call: call.data == "komutlar")
def komutlar(call):
    mesaj = """
📚 Komutlar Menüsüne Hoş geldiniz!

🔍 Kişi Bilgileri:
	
➤ /adsoyad • Girdiğiniz İsim ve Soyismi sorgular
➤ /adsoyadil • Girdiğiniz İsim, Soyismi ve İli sorgular
➤ /adsoyadililce • Girdiğiniz İsim, Soyismi, İli ve İlçeyi sorgular
➤ /tc • T.C. numarasından kişi bilgisi verir
➤ /aile • T.C.'den kişi aile bilgisi verir
➤ /sulale • T.C.'den kişi sülale bilgisi verir
➤ /es • T.C.'den eş sorgu yapar
➤ /cocuk • T.C.'den çocuk sorgu yapar
➤ /adres • T.C.'den kişi adresini verir
➤ /tcpro • T.C.'den kişi detaylı bilgi verir
➤ /medeni • T.C.'den medeni hali verir
➤ /iban • IBAN'dan kişi bilgilerini verir
➤ /ihbar • Adrese ihbar gönderir
➤ /vergid • Kişiye ait vergi bilgilerini verir

📞 GSM İşlemleri:
	
➤ /gsmtc • gsm nunaradan T.c verir
➤ /tcgsm • T.C. numarasından GSM verir
➤ /gsmdetay • GSM'den detaylı kişi bilgilerini verir
➤ /operator • GSM'den operatör bilgisini verir
➤ /sms • GSM'ye SMS saldırısı gönderir
➤ /arama • Telefona arama gönderir


🌍 Diğer İşlemler:
	
➤ /ip • IP'den konum bilgisi verir
➤ /ping • Hedef sitenin gecikme süresini verir
➤ /portscan • Hedefin açık portlarını tarar
➤ /leakscan • Girilen verinin leak durumunu sorgular
➤ /dns • Girilen sitenin dns bilgilerini gösterir
➤ /defteryaz • Deftere metin yazdırır
➤ /subdomain • Girilen sitenin subdomainlerini gösterir
➤ /qrcode • QR kod oluşturur
➤ /index • URL'den site indexini verir
➤ /yaz • Girilen mesajı deftere yazar
➤ /dolar • Güncel döviz kurunu verir
➤ /ig • instagram kullanıcı adindan bilgi verir
➤ /ses • metinden sese çevirir
➤ /log • Site log kayıtlarını getirir
 """
    geri = telebot.types.InlineKeyboardButton("Geri", callback_data="geri")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.add(geri)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)
    
YEGEN_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/yegen.php?tc="

@bot.message_handler(commands=['yegen'])
def handle_yegen_command(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    chat_id = message.chat.id
 
    
        
    try:
        
        tc = message.text.split()[1]
        
        
        api_response = requests.get(YEGEN_API + tc).json()

        
        user_info = api_response.get("Yeğenler", [])

 
        response_text = (
            f""
            f""
            f""
        )

        for info in user_info:
            response_text += (
                f"\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ TC: {info['TC']}\n"
                f"┃➥ ADI: {info['ADI']}\n"
                f"┃➥ SOY ADI: {info['SOYADI']}\n"
                f"┃➥ DOĞUM TARİHİ: {info['DOGUMTARIHI']}\n"
                f"┃➥ İL: {info['NUFUSIL']}\n"
                f"┃➥ İLÇE: {info['NUFUSILCE']}\n"
                f"┃➥ ANNE ADI: {info['ANNEADI']}\n"
                f"┃➥ ANNE TC: {info['ANNETC']}\n"
                f"┃➥ BABA ADI: {info['BABAADI']}\n"
                f"┃➥ BABA TC: {info['BABATC']}\n"
                f"┃➥ UYRUK: {info['UYRUK']}\n"
                f"┃➥ YAKINLIK: {info['Yakinlik']}\n"
                f"╰━━━━━━━━━━━━━━"
            )

        
        bot.reply_to(message, response_text)

    except IndexError:
        
        bot.reply_to(message, "Lütfen geçerli bir TC kimlik numarası girin.")
    except Exception as e:
        
        bot.reply_to(message, f"Bilgiler Bulunamadı")
        
        
    
    
    
@bot.message_handler(commands=['ig'])
def aile(message):
    chat_id = message.chat.id

    if len(message.text.split()) <= 1:
        bot.send_message(chat_id, "⚠️ *Lütfen Geçerli Bir Kullanıcı Adı Girin.*\n\n*Örnek:*` /ig amedskofficial`", parse_mode="Markdown")# Kullanıcı adı yoksa mesaj gönder
        return

    tc_number = message.text.split()[1]
    url = f'http://api.hexnox.pro/sowixapi/instgram.php?search={tc_number}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        text = response.content.decode('utf-8-sig')
        result = json.loads(text)
        
        if isinstance(result, list) and len(result) > 0:
            member = result[0]
            profile_pic_url = member.get('profile_pic_url', '')
            bot.send_photo(chat_id, profile_pic_url)
            
            formatted_message = (
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ İSİM: {member.get('full_name', 'Bilinmiyor')}\n"
                f"┃➥ USERNAME: {member.get('username', 'Bilinmiyor')}\n"
                f"┃➥ İD: {member.get('id', 'Bilinmiyor')}\n"
                f"┃➥ GİZLİ HESAP: {'Evet' if member.get('is_private') else 'Hayır'}\n"
                f"┃➥ MAVİ TİK: {'Evet' if member.get('is_verified') else 'Hayır'}\n"
                f"╰─━━━━━━━━━━━━━━\n"
            )
            bot.send_message(chat_id, formatted_message)
        else:
            bot.send_message(chat_id, "⚠️ *Veri Bulunamadı.*", parse_mode="Markdown")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        bot.send_message(chat_id, "⚠️ *Bir hata oluştu. Lütfen daha sonra tekrar deneyin.*", parse_mode="Markdown")
    except json.JSONDecodeError:
        bot.send_message(chat_id, "⚠️ *Lütfen Geçerli Bir Kullanıcı Adı Girin.*\n\n*Örnek:* /ig amedskofficial", parse_mode="Markdown")

   

    
import requests
import os

@bot.message_handler(commands=['ses'])
def ses_cevir(message):
    chat_id = message.chat.id
    # Komutun yanında bir mesaj var mı kontrol et
    if len(message.text.split()) > 1:
        # Mesajı al ve API'ye gönder
        text = " ".join(message.text.split()[1:])
        url = f'https://tilki.dev/api/yaziyi-ses-yapma?text={text}'
        
        try:
            # Ses dosyasını indir
            response = requests.get(url)
            response.raise_for_status()
            
            # Gelen veriyi bir ses dosyasına kaydet
            with open('mesaj_sesi.mp3', 'wb') as f:
                f.write(response.content)

            # Bot ile ses dosyasını gönder
            with open('mesaj_sesi.mp3', 'rb') as audio_file:
                bot.send_voice(chat_id, audio_file)

            # İşlem bittikten sonra dosyayı sil
            os.remove('mesaj_sesi.mp3')

        except requests.exceptions.HTTPError:
            bot.send_message(chat_id, "⚠️ Ses oluşturma sırasında bir hata oluştu.")
        except requests.exceptions.RequestException as err:
            bot.send_message(chat_id, f"⚠️ Beklenmeyen bir hata oluştu: {err}")
    else:
        # Kullanıcı sadece /ses yazdıysa hata mesajı göster
        bot.send_message(chat_id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/ses Biji Serok Apo`", parse_mode='Markdown')

          
                  
@bot.message_handler(commands=['index'])
def index(message):
    if message.chat.type != "private":
        return

    

    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir Site URL girin!*\n\n*Örnek:* `/index https://google.com`", parse_mode="Markdown")
        return

    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm Hatalı URL girdiniz Lütfen geçerli bir URL girin*\n\n*Örnek*: `/index https://instagram.com`", parse_mode="Markdown")
        return

    response = requests.get(site_url)

    if response.status_code == 200:
        file_name = "alemdar.html"
        file_content = response.text
        
        with open(file_name, 'w') as file:
            file.write(file_content)

        with open(file_name, 'rb') as file:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_document(message.chat.id, file)

        os.remove(file_name)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm bu siteye Ait Bir index Çekilemiyor!*", parse_mode='Markdown')



support_channel_id = -1002122807954

@bot.message_handler(commands=['sms']) # 
def send_sms(message):
    chat_id = message.chat.id
    user_input = message.text.split(' ', 1)

    if len(user_input) != 2:
        bot.send_message(chat_id, '*⚠️ Lütfen Geçerli Bir telefon numarası girin!\n\nÖrnek:* `/sms 5555555555`', parse_mode='Markdown')
        return

    gsm_number = user_input[1]
    api_url = f'https://sowixapi.online/api/sowixapi/sms.php?telno={gsm_number}'

    
    start_message = bot.send_message(chat_id, "Smsler Gönderiliyor...")

    
    response = requests.get(api_url)

    if response.status_code == 200:
        
        bot.send_message(chat_id, "Smsler Başarılı Bir Şekilde Gönderildi!\n\n@polatalemdar330 </>")
    else:
        bot.send_message(chat_id, "SMS gönderirken bir hata oluştu.") #                                                                                                                                                                             
   
@bot.callback_query_handler(func=lambda call: call.data == "geri")
def geri(call):
    mesaj = "👋 Merhaba! Benim adım Polat Hack bot sorgu yapmak için buradayım\nBeni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\nEn son güncellemeler hakkında bilgi almak için @devillerden kanalıma katılın.\n\n⛔ Not: Bot Dijvarhack  kanalına özel olarak yapılmıştır. Botu kullanmak için Dijvar Hack'e katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız."
    komutlar = telebot.types.InlineKeyboardButton("📜Komutlar", callback_data="komutlar")
    majeste_sohbet = telebot.types.InlineKeyboardButton(" ➕ beni grubuna ekle", url="https://t.me/polatalemdarsorgubot?startgroup=true")
    iletisim = telebot.types.InlineKeyboardButton("🙋owner", url="https://t.me/polatalemdar330")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.row(komutlar)
    butonlar.row(majeste_sohbet, iletisim)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_log:"))
def copy_log_callback(call):
    try:
        # Callback data'dan log ID'yi al
        log_id = call.data.replace("copy_log:", "")
        
        # Geçici storage'dan log içeriğini al
        if log_id in temp_log_storage:
            log_content = temp_log_storage[log_id]
            
            # Kullanıcıya kopyalanabilir metin gönder
            bot.answer_callback_query(call.id, "✅ Log kopyalandı!")
            bot.send_message(call.message.chat.id, f"```\n{log_content}\n```", parse_mode="Markdown")
            
            # Geçici storage'dan sil (memory tasarrufu için)
            del temp_log_storage[log_id]
        else:
            bot.answer_callback_query(call.id, "❌ Log bulunamadı!")
        
    except Exception as e:
        bot.answer_callback_query(call.id, "❌ Kopyalama hatası!")
     

# Plaka bilgileri (örnek veri)
plaka_bilgileri = {
    "34ABC123": {
        "borç": "2,500 TL",
        "TC": "12345678901", 
        "ad_soyad": "ÖRNEK KİŞİ",
        "ceza": "Hız limiti aşımı",
        "marka_model": "TOYOTA COROLLA",
        "renk": "BEYAZ",
        "sigorta_durumu": "Aktif"
    }
}


@bot.message_handler(commands=['plaka'])
def handle_plaka(message):
    text = message.text.split()
    if len(text) < 2:
        bot.reply_to(message,'*⚠️ Lütfen Geçerli Bir Plaka girin!\n\nÖrnek:* `/plaka 34ABC123`', parse_mode='Markdown')
        return
    
    plaka = text[1].upper()  # Plaka numarasını büyük harf yaparak al
    
    # API sorgusu yerine örnek veri dönüyoruz
    if plaka in plaka_bilgileri:
        bilgiler = plaka_bilgileri[plaka]
        
        response_text = "╭─━━━━━━━━━━━━━─╮\n┃@polatalemdarsorgubot - PLAKA BORÇ\n┃─━━━━━━━━━━━━━─\n"
        response_text += (
            f"┃ Plaka: {plaka}\n"
            f"┃ Borç: {bilgiler['borç']}\n"
            f"┃ TC Kimlik No: {bilgiler['TC']}\n"
            f"┃ Ad Soyad: {bilgiler['ad_soyad']}\n"
            f"┃ Ceza: {bilgiler['ceza']}\n"
            f"┃ Marka ve Model: {bilgiler['marka_model']}\n"
            f"┃ Aracın Rengi: {bilgiler['renk']}\n"
            f"┃ Sigorta Durumu: {bilgiler['sigorta_durumu']}\n"
        )
        response_text += "╰─━━━━━━━━━━━━━─╯"
        
        bot.reply_to(message, response_text)
    else:
        bot.reply_to(message, f"*🔍 {plaka} plakası için bilgi bulunamadı.*", parse_mode="Markdown")


@bot.message_handler(commands=['adresadres'])
def adress_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://api.hexnox.pro/sowixapi/adres.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            adres_data = data["data"]
            adres_message = f"""
➥ Kimlik No: {adres_data["TC"]}
➥ Ad Soyad: {adres_data["AdSoyad"]}
➥ Doğum Yeri: {adres_data["DogumYeri"]}
➥ Vergi Numarası:  {adres_data["VergiNumarasi"]}
➥ İkametgah: {adres_data["Ikametgah"]}
➥ auth: @polatalemdar330


"""

            bot.reply_to(message, adres_message)
        else:
            bot.reply_to(message, "Bu TC numarasına ait adres bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/adres 11111111110`', parse_mode='Markdown')
  




API_ENDPOINT = 'https://apis.xditya.me/write?text={}'

@bot.message_handler(commands=['yaz'])
def yaz(message):
    if message.chat.type != "private":
        return

    
    try:
        text = message.text.split(maxsplit=1)[1]
       
        api_url = API_ENDPOINT.format(text)
        response = requests.get(api_url)
        
        if response.status_code == 200:
            bot.send_photo(message.chat.id, response.content)
        else:
            bot.send_message(message.chat.id, "⚠️ *API'de sorun var Lütfen Yönetici ile iletişime geçin!.*", parse_mode="Markdown")
    
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/yaz Ne Mutlu TÜRK'üm Diyene`", parse_mode='Markdown')




@bot.message_handler(commands=['dolar'])
def doviz(message):
    try:
        response = requests.get("https://tilki.dev/api/dolar")
        if response.status_code == 200:
            wizardapi = response.json()
            dolar = wizardapi['dolar']
            bot.send_message(message.chat.id, f"*💸 DOVIZ : 1 DOLAR = {dolar} TL ✅*", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "*API'den veri çekilemedi!*", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")

@bot.message_handler(commands=['log'])
def log_komutu(message):
    args = message.text.split()
    if len(args) < 2:
        bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir mesaj girin!\n\nÖrnek:* `/log siteadi.com`", parse_mode='Markdown')
        return

    site = args[1]
    url = f"https://devilhazretleri.com/log.php?site={site}"
    
    # Yükleme mesajı gönder
    loading_msg = bot.send_message(message.chat.id, "🔍 *Log bilgileri sorgulanıyor, lütfen bekleyin...*", parse_mode="Markdown")
    
    try:
        import requests
        resp = requests.get(url, timeout=10)
        
        # Yükleme mesajını sil
        bot.delete_message(message.chat.id, loading_msg.message_id)
        
        içerik = resp.text.strip()
        if not içerik or "Kayıt bulunamadı" in içerik:
            bot.reply_to(message, "Kayıt bulunamadı!")
            return
            
        # Satırları ayıkla, ilk 10 satırı göster
        satirlar = [s for s in içerik.replace("\r", "").split("<br>") if s.strip()]
        mesaj = "\n".join(satirlar[:10])
        if len(satirlar) > 10:
            mesaj += "\n... (devamı var)"
            
        # Eğer mesaj çok uzunsa txt dosyası olarak gönder
        if len(mesaj) > 4000:
            file_name = f"log_{site}.txt"
            full_content = "\n".join(satirlar)
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(full_content)
            with open(file_name, "rb") as f:
                bot.send_document(message.chat.id, f, caption=f"📋 {site} Log Sonuçları")
            os.remove(file_name)  # Dosyayı temizle
        else:
            # Log ID oluştur ve geçici storage'da sakla
            global log_counter
            log_counter += 1
            log_id = f"log_{log_counter}"
            temp_log_storage[log_id] = mesaj
            
            # Kopyalama butonu ekle
            keyboard = types.InlineKeyboardMarkup()
            copy_button = types.InlineKeyboardButton("📋 Kopyala", callback_data=f"copy_log:{log_id}")
            keyboard.add(copy_button)
            bot.reply_to(message, f"<pre>{mesaj}</pre>", parse_mode="HTML", reply_markup=keyboard)
            
    except Exception as e:
        # Yükleme mesajını sil
        try:
            bot.delete_message(message.chat.id, loading_msg.message_id)
        except:
            pass
        bot.reply_to(message, f"Hata: {e}")


		# Geçerli komutlar listesi
valid_commands = [
    '/start', '/komutlar', '/adsoyad', '/adsoyadil', '/adsoyadililce', '/tc', '/aile', '/sulale', '/es', '/cocuk', '/adres', '/tcpro', '/medeni', '/iban', '/ihbar', '/vergid',
    '/gsmtc', '/tcgsm', '/operator', '/sms', '/arama', '/ip', '/ping', '/portscan', '/leakscan', '/dns', '/defteryaz', '/subdomain', '/qrcode', '/index', '/yaz', '/dolar', '/ig', '/ses', '/yegen', '/plaka', '/log'
]



# Diğer komutlarınız burada olabilir...

# Geçersiz komutları yakalayan handler
@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    if message.text not in valid_commands:
        bot.send_message(message.chat.id, 	"*⚠️ Yanlış komut kullandınız. Komutları görmek için /komutlar yazabilirsiniz.*", parse_mode="Markdown")

	


import logging
logging.basicConfig(level=logging.INFO, filename='bot.log')

def main():
    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            logging.error(f"Hata: {e}")
            time.sleep(1)
