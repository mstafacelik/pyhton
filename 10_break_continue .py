
# break
# Bir while veya for döngüsünü hemen sonlandırır. Kosul saglansa bile, break varsa döngü biter.


while True:
    yas = int(input("lütfen yasinizi giriniz: "))

    if yas < 0:
        print("Negatif yas olmaz!")
        break
        print("test")
    elif yas < 18:
        print("Resit degilsiniz")

    else:
        print("Resitsiniz")


print("Ende")


# Bu örnekte break sadece yaş negatif girildiğinde devreye girer.
# Eger kullanici negatif sayi girerse, cikti su sekilde olur :

# Negatif yas olmaz!
# Ende


# continue
# Döngüde kalan satırları atlayıp başa döner.

i = 0

while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)


# i == 4 olduğunda print(i) atlanır.
