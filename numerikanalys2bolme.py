import math

m = 68.1
t = 10
v = 40
g = 9.81
i = 0
fonkxr = []

def dogrulukoran():
    oran = ((b - fonkxr[i]) / fonkxr[i]) * 100
    print(oran)

def degerbulucu(c):
    result = (g * m / c) * (1 - math.exp(-c / m * t)) - v
    return result

xa = float(input("Xa değerini giriniz: "))
xu = float(input("Xu değerini giriniz: "))   

while True:
    i = i + 1
    
    devam_secim = input("Çıkmak için 'q' tuşuna basın: ")
    if devam_secim.lower() == 'q':
        print("Program sonlandırılıyor...")
        break
    
    xr = (xa + xu) / 2
    print(xa)
    print(xu)
    print(xr)
    fonkxa = degerbulucu(xa)
    fonkxu = degerbulucu(xu)
    fonkxr.append(degerbulucu(xr))
    b = fonkxr[i - 1]
    dogrulukoran()
    
    a = (fonkxa * fonkxr[-1])
    
    if a < 0:
        xu = xr
 
    a = (fonkxu * fonkxr[-1])
    
    if a < 0:
        xa = xr