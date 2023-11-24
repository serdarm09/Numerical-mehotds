#basiteknoktali3
import math

#baslangic degeri
x =float(input("İlk değeri giriniz: "))
def dogrulukoran():
    oran = ((x1-x)/x)*100
    print("Ey oranı",oran)
#adım sayar
i=0
while True:
    
    devam_secim = input("Çıkmak için 'q' tuşuna basın: ")
    if devam_secim.lower() == 'q':
        print("Program sonlandırılıyor...")
        break
    print("Adım",i)
    x1=x
    print("Xi degeri =",x)
    x=math.exp(-x) 
    print("Xi+1 degeri = ",x)
    dogrulukoran()
    i=i+1