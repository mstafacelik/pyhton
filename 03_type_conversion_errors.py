

# Type Conversion Errors:

# ValueError: Bu tip doğru ama bu değer kabul edilemez
# Bu hatalar genellikle kullanicidan veri alirken, dönüşüm yaparken ya da liste işlemlerinde görülür.

# 1# int + str (toplama hatasi)
# String ve int TOPLANAMAZ, CARPMA MÜMKÜN !

isim = "hulki"
yas = 5

# print(isim + yas)  TypeError

print(isim, yas)  # sadece yazdirma var, matematiksel islem yok, calisir


print(isim, str(yas))

print(isim*yas)

# 2# str → int dönüşümünde sayi olmayan string

sayi = "on"

# print(int(sayi))  ValueError

# 3#  float yerine nokta yerine virgül kullanmak (Türkçe alişkanliği)

pi_sayisi_false = "3,14"
pi_sayisi_true = "3.14"

# print(float(pi_sayisi_false)) ValueError

print(float(pi_sayisi_true))

# 4# Boş stringi int'e dönüştürmeye calisma

bos_yapma = ""

# print(int(bos_yapma)) #  -> ValueError:

# 5#  Listeyi int'e çevirmeye çalişmak

my_list = [1, 2, 3]

# print(int(my_list)) TypeError

# 6# None tipini int'e çevirmeye çalişmak

a = None

# print(int(a)) TypeError


# 7# String içinde boşluk varsa

my_str01 = "  42  "
my_str02 = "42a"

print(int(my_str01))  # -> calisir
# print(int(my_str02))  -> ValueError


"""
Tip Dönüşümde Dikkat Edilmesi Gerekenler

- int()   → yalnizca tam sayi gibi görünen string'lerde çalişir.
- float() → yalnizca nokta (.) ile ayrilmiş ondalikli string'lerde çalişir.
- str()   → hemen her tip çevrilebilir ama bazilari mantikli olmayabilir (örneğin str(None) → "None").

"""
a = 5
b = 9

print(a+b)

print(10/3)
