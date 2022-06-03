from __future__ import unicode_literals
import youtube_dl
import time
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.WHITE)

sarki = input('Lütfen indirmek istediğiniz video url si ---> ')

tür = input("MP3 mü istersiniz ? MP4 mü ?  ===> ")
if tür == "mp3" or "MP3":
    print(Fore.GREEN)
    print("MP3 seçildi!")
    ayarlar = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': "mp3",
    }
    sonuc = "Müziğiniz"
if tür == "MP4" or "mp4":
    print(Fore.GREEN)
    print("MP4 seçildi!")
    ayarlar = {}
    sonuc = "Videonuz "
else:
    print(Fore.RED)
    print("Lütfen geçerli bir tür seçin!")
    time.sleep(1)
    print("HATA KODU 10")
    time.sleep(4)
    exit()
with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([sarki])
print(Fore.CYAN)
print(Style.DIM)
print(sonuc+"Başarılı şekilde dönüştü ve indirmeye koyuldu!")
time.sleep(2)
print(sonuc + "bulunduğunuz klasöre kaydedilmiştir.")
time.sleep(0.3)
