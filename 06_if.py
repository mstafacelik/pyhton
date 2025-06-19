

# if ifadesi bir koşul True olduğunda belirli kodları çalıştırmak için kullanılır.


yas = 10

if yas >= 18:
    print("Resitsiniz!")

yas = int(input("lütfen yasinizi giriniz : "))

if yas >= 18:
    print("Resitsiniz, ehliyet alabilirsiniz!")


# Kullanıcıdan bir sayı al ve eğer sayı çiftse "Çift sayı girdiniz", değilse hiçbir şey yazmasın (sadece if kullanılacak).


kullanici_sayi = int(input("Lütfen bir sayi giriniz "))

if kullanici_sayi % 2 == 0:
    print("Çift sayi girdiniz")
