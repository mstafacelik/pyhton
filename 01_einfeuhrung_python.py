print("Hallo Welt")


# input() -> kullanicidan veri alma
# kullanici input'unun output'u her zaman String!

isim = input("bitte geben Sie Ihren Namen ein : ")

soyisim = input("bitte geben Sie Ihren Nachamen ein : ")

print("Hi", isim, soyisim,  "schön, dass du da bist!")

# len() -> String uzunluk/karakter sayisi


print("isim", len(isim), "karaktere,\n" "soyisim",
      len(soyisim), "karaktere sahip!")

# Girinti (Indentation):
# Python'da girintiler (boşluklar) kod bloklarini belirler. Ayni blokta tüm satirlar ayni sayida boşlukla başlamali.


# Değişken İsimlendirme Kurallari:

""" 
- Harf veya _ ile başlamali.
- Sayilarla başlayamaz.
- Sadece harf, rakam ve _ karakteri içerebilir.
- Büyük/küçük harf duyarlidir (isim ve Isim farklidir).
- Python'da anahtar kelimeler kullanilamaz (if, for, while, class vb.).

 """


ad_soyad = "Esra Celik"
_age = 18
TOTAL_SUM = 100
