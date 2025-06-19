

# Eğer if koşulu doğruysa bir işlem yapılır; değilse else bloğu çalıştırılır. Yani iki alternatifli karar yapısıdır.

'''
if kosul:
    # kosul doğruysa calisacak kod
else:
    # kosul yanlissa calisacak kod

'''

sifre = "Pyhton1903."

user_sifre = input("Lütfen sifrenizi giriniz : ")

if user_sifre == sifre:
    print("Basarili giris")
else:
    print("Yanlis sifre")


yas = int(input("Yasinizi giriniz : "))

if yas > 18:
    print("Resitsiniz")
else:
    print("Resit degilsiniz")


''' user_sayi01 = input("Bir sayi giriniz : ")

if user_sayi01> "0" :
    print("Pozitif")
else    :
    print("Negatif ya da sifir")
    
'''

user_sayi02 = int(input("Bir sayi giriniz : "))

if user_sayi02 > 0:
    print("Pozitif")
else:
    print("Negatif ya da sifir")
