import math
import random

p = int(input("Asal değeri giriniz."))
q = int(input("2. Asal değeri giriniz."))
d = 3

message = input("Metin giriniz.")

sozluk = {
    'a': 1, 'b':2 , 'c': 3, 'ç': 4 , 'd' : 5, 'e' : 6, 
    'f':7, 'g':8, 'ğ': 9, 'h':10, 'ı':11, 'i':12, 'j':13, 
    'k': 14, 'l' : 15, 'm': 16, 'n': 17, 'o':18, 'ö':19, 
    'p': 20, 'r': 21, 's':22, 'ş': 23, 't':24, 'u' : 25, 
    'ü':26, 'v':27, 'y': 28, 'z': 29 
}

sayi = sozluk[message]

n = p*q
an = (p-1)*(q-1)

def ebob (sayi1,sayi2):
    i=1
    ebob=1
    while(i<=sayi1 and i<=sayi2):
        if not sayi1 % i and not sayi2 % i:
            ebob = i
        i +=1
    return ebob

e_list = []
for i in range(2,an):
    if(ebob(i,an)==1):
        e_list.append(i)

e= random.choice(e_list)

d_list = []
for i in range(2,100):
    if((i*e)%an==1):
        d_list.append(i)

d= random.choice(d_list)

c = (pow(sayi,e)%n)
m = (pow(c,d)%n)

print("Açık anahtar:({},{})".format(e,n))
print("Özel anahtar: ({},{})".format(d,n))

print("Şifreli hali: " + str (c) + "\n" + "Şifresiz Hali: "+  str (list(sozluk.keys())[list(sozluk.values()).index(m)]))







