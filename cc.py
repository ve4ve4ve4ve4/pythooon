import datetime
from smtplib import SMTP

if __name__ == '__main__':
    toplanti = input("Toplantı,Etkinlik Adı Giriniz :")
    print(toplanti)
    yil =int(input("Toplantı,Etkinlik Yılını Giriniz :"))
    print(yil)
    if (yil < 2023):
        print("Hatalı Bir Yıl Girdiniz,Yıl 2023 veya daha büyük Olmalıdır.")
        yil = int(input("Toplantı,Etkinlik Yılını Giriniz :"))
        print(yil)
    ay =int(input("Toplantı,Etkinlik Ayını Giriniz :"))
    print(ay)
    if (ay<0 or ay>12):
        print ("Hatalı Bir Ay Girdiniz, Ay 0,12 Arası Olmalıdır.")
        ay = int(input("Toplantı,Etkinlik Ayını Giriniz :"))
        print(ay)
    if (yil==2023 and ay<5):
        print ("Hatalı Bir Ay Girdiniz, Ay 5,12 Arası Olmalıdır.")
        ay = int(input("Toplantı,Etkinlik Ayını Giriniz :"))
        print(ay)   
    gun =int(input("Toplantı,Etkinlik Günü Giriniz :"))
    print(gun)
    if ((ay==1 or ay==3 or ay==5 or ay==7 or ay==8 or ay==10 or ay==12) and gun>31):
        print ("Hatalı Bir Gün Girdiniz, Gün 0,31 Arası Olmalıdır.")
        gun = int(input("Toplantı,Etkinlik Günü Giriniz :"))
        print(gun)
    if ((ay==4 or ay==6 or ay==9 or ay==11) and gun>30):
        print ("Hatalı Bir Gün Girdiniz, Gün 0,30 Arası Olmalıdır.")
        gun = int(input("Toplantı,Etkinlik Günü Giriniz :"))
        print(gun)
    if (ay==2 and gun>28):
        print ("Hatalı Bir Gün Girdiniz, Gün 0,28 Arası Olmalıdır.")
        gun = int(input("Toplantı,Etkinlik Günü Giriniz :"))
        print(gun)
    saat = int(input("Toplantı,Etkinlik Saatini Giriniz :"))
    print(saat)
    if (saat<0 or saat>23):
        print ("Hatalı Bir Saat Girdiniz, Saat 0,23 Arası Olmalıdır.")
        saat = int(input("Toplantı,Etkinlik Saatini Giriniz :"))
        print(saat)
    dakika =int(input("Toplantı,Etkinlik Dakikasını Giriniz :"))
    print(dakika)
    if (dakika < 0 or dakika > 60):
        print("Hatalı Bir Dakika Girdiniz, Saat 0,60 Arası Olmalıdır.")
        dakika = int(input("Toplantı,Etkinlik Dakikasını Giriniz :"))
        print(dakika)
    tarih=datetime.datetime(yil,ay,gun,saat,dakika)
    print (tarih)
    katilimci=int(input("Toplantı,Etkinliğe Kaç Kişi Katılacağını Giriniz :"))
    print (katilimci)
    if (katilimci<=0):
        print ("Hatalı Kişi Sayısı Girdiniz, 0dan Büyük Olmalıdır.")
        katilimci = int(input("Toplantı,Etkinliğe Kaç Kişi Katılacağını Giriniz :"))
        print(katilimci)
x=("Toplantının Adı: " + toplanti + "\n" + "Toplantı Tarihi: " + str(tarih) + "\n" + "Toplantıya Katılacak Kişi Sayısı: " + str(katilimci))
print (x)
# class
class Etkinlik:
    # class attributes 
    # constructor (yapıcı metod)
    def __init__(etkinlik,toplanti,tarih,katilimci):
        # object attributes
        etkinlik.toplanti = toplanti
        etkinlik.tarih = tarih
        etkinlik.katilimci = katilimci
        print('init metodu çalıştı.')

    # methods


# object (instance)
p1 = Etkinlik(toplanti=toplanti,tarih=tarih,katilimci=katilimci)

# updating
p1.etkinlik = 'cey'

# accessing object attributes
print(f'p1:  toplanti: {p1.toplanti} :tarih: {p1.tarih} :katilimci: {p1.katilimci}')


print(p1)
print(type(p1))
x = ("Toplantının Adı: " + toplanti + "\n" + "Toplantı Tarihi: " + str(tarih) + "\n" + "Toplantıya Katılacak Kişi Sayısı: " + str(katilimci))
print (x)
