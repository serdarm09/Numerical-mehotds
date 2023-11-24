import math

#sabit sayılarımız

m = 68.1
t = 10
v = 40
g = 9.81

#sonsuz döngü birden fazla işlem yaparsak diye

while True:
    devam_secim = input("Çıkmak için 'q' tuşuna basın: ")

    if devam_secim.lower() == 'q':
        print("Program sonlandırılıyor...")
        break

    # Kullanıcıdan c değerini almak
    c = float(input("Lütfen c değerini girin: "))

    # Euler değerini kullanarak hesaplama yapma
    result = (g * m / c) * (1 - math.exp(-(c / m * t))) - v

    # Sonucu ekrana yazdır
    print("Sonuç:", result)