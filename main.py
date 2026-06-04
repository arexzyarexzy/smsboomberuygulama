from flask import Flask, request
from sms import SendSms
import threading

app = Flask(__name__)

def baslat(tel):
    # SendSms sınıfını başlat
    send_sms = SendSms(tel, "")
    # Tüm fonksiyonları bul (servisler)
    servisler = [attr for attr in dir(send_sms) if callable(getattr(send_sms, attr)) and not attr.startswith("__")]
    
    # Her bir servisi ayrı bir iş parçacığında çalıştır
    threads = []
    for servis in servisler:
        t = threading.Thread(target=getattr(send_sms, servis))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

@app.route('/')
def ana_sayfa():
    numara = request.args.get('tel') # Linke ?tel=05xxxxxxxxx ekleyince çalışır
    if numara:
        threading.Thread(target=baslat, args=(numara,)).start()
        return f"SMS gönderimi başlatıldı: {numara}"
    return "Lütfen numara parametresi girin: ?tel=05XXXXXXXXX"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
