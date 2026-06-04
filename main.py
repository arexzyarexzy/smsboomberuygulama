from flask import Flask, request
from sms import SendSms # Senin sms.py dosyan aynı klasörde olmalı
import threading

app = Flask(__name__)

def baslat(tel):
    # sms-boomber'daki döngüyü buraya gömdük
    send_sms = SendSms(tel, "")
    # Burada sadece istediğin servisleri tek tek çağırabilirsin
    # Örnek: send_sms.Ido()
    # Hepsini birden çalıştırmak için kodun içindeki listeyi kullanmalısın

@app.route('/')
def ana_sayfa():
    tel = request.args.get('numara')
    if tel:
        threading.Thread(target=baslat, args=(tel,)).start()
        return "İşlem başlatıldı: " + tel
    return "Numara gir!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)