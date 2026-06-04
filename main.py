from flask import Flask, request
from sms import SendSms
import threading

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    numara = request.args.get('tel')
    if numara:
        # SMS atma motorunu arka planda çalıştır
        s = SendSms(numara, "")
        # Buraya sms.py içindeki servisleri tek tek tetikleyecek döngü eklemelisin
        return f"İşlem başlatıldı: {numara}"
    return "Numara girmedin!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
