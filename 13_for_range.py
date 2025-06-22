
# while döngüsü, kosul doğru olduğu sürece döner.  Peki ya bir kod bloğunu belirli bir sayida calistirmak istersek?
# 📌 İste bu gibi durumlar icin for döngüsü daha uygundur.
# for döngüsü, bir koleksiyonun (örneğin liste, dizi, metin, range) her bir öğesi üzerinde sirayla islem yapmak icin kullanilir.
# Özellikle tekrar sayisi belli olan durumlarda while yerine for daha kullanislidir.




#  range() fonksiyonu

# Sayi araliği üretir. Genelde for ile birlikte kullanilir.
# range() fonksiyonu kullanilarak, döngü belirli bir sayi kadar çalistirilir.

# range(baslangic, bitis, adim)

'''

- baslangic → varsayilan 0
- bitis → bu sayiya kadar (dahil degil!)
- adim → varsayilan 1


| Kullanim         | Anlami                          |
| ---------------- | ------------------------------- |
| range(n)         | 0'dan n'ye kadar (n hariç)      |
| range(a, b)      | a'dan b'ye kadar (b hariç)      |
| range(a, b, c)   | a'dan b'ye kadar, c'ser artisla |

'''


for i in range(5):
    print(i)
    
'''
0
1
2
3
4

'''    

for i in range(2, 6):
    print(i)
  
'''
2
3
4
5

'''

for i in range(1, 10, 2):
    print(i)
'''
1
3
5
7
9

'''

for i in range(10, 0, -2):
    print(i)
'''
for i in range(10, 0, -2):
    print(i)
'''


# Karakterleri tek tek yazdir:
# String'ler aslında karakter dizisidir.
# for harf in string: ifadesiyle her karakter sırayla alınabilir.


for harf in "Tastatur" :
    print(harf)


# Python, "Tastatur" kelimesindeki her karakteri sirayla harf değişkenine atar.
# Ve her döngüde o harf ekrana yazdirilir.

'''
T
a
s
t
a
t
u
r

'''




'''
Kullanicidan bir sayi al.
O sayiya kadar olan tek sayilari ekrana yazdir.

(Yani range ve if birlikte kullanilmali.)

'''

# 1 .yol
user_input_sayi=int(input("Bir sayi giriniz : "))

for i in range(1,user_input_sayi , 2):
    print(i)




#2. yol
user_input_sayi=int(input("Bir sayi giriniz : "))

for i in range(0, user_input_sayi) :
    if i%2 !=0:
        print(i)




# Kullanıcıdan isim al ve harf harf yazdır


name_user_input=input("isim giriniz : ")

for harf in name_user_input : 
    print(harf.upper())
    
    
name_user_input=input("isim giriniz : ")

for harf in name_user_input : 
    print(harf.lower())


