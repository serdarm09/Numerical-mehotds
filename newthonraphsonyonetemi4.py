#newthonraphsonyonetemi4    
import math
import sympy as sp

h = 0.0001
a = 5

def denklem(a):
    #soruda verilen denklemi olustumra yerimiz
    #a**2 - 5*a + 3
    return a ** 2 - 5*a + 3

def cozum():
    cevap = a**2 - 5*a + 3
    print("fonk cevabı:",cevap)
    return cevap
def newthon():
    cevap2 = a-(fonk/turev)
    print("Newthon Raphson cevabı:",cevap2)
    return cevap2
while True:
    devam_secim = input("Çıkmak için 'q' tuşuna basın: ")
    if devam_secim.lower() == 'q':
        print("Program sonlandırılıyor...")
        break
    fonk = cozum()
    turev = (denklem(a + h) - denklem(a)) / h
    print("Türevi:",turev)
    a = newthon()

    
#algorimta oluşturduğumuz yer
