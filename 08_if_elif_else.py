'''
Birden fazla durumu kontrol etmek gerektiğinde elif (else if) kullanilir. Yani:

İlk if kosulu yanlissa,

Sonraki elif kosullari sirayla denenir.

Hiçbiri sağlanmazsa else çalisir.

'''


# kullanicidan sinav notunu alma

user_puan = int(input("Sinav sonucunu giriniz : "))

if user_puan >= 85:
    print("AA")
elif user_puan >= 70:
    print("BB")

elif user_puan >= 60:
    print("DD")
else:
    print("Sinavdan kaldiniz")

# pozitif negatif kontrol

user_sayi= int(input("Bir sayi giriniz : "))

if user_sayi <0 :
    print("Negatif")
elif user_sayi == 0 :
    print("Sifir")
else : 
    print("Pozitif")