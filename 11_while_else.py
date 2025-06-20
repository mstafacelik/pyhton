
# while...else temel örnek
a = 0
while a < 3:
    print(a, end=", ")
    a += 1
else:
    print("\nLoop ici Ende")

print("########################")
# while...else örnek (with break)
# break olursa else çalışmaz. Loop tan cikilir
b = 0
while b < 5:

    if b == 3:
        print("\nRulet break ile patladi, Loop burada sona erdi")
        break
    print(b, end=", ")
    b += 1
else:
    print("Loop ici Ende")

print("Loop sonrasi devam...")

print("##########################")
# while...else örnek (with continue)
c=0
while c < 5:

    if c == 3:
        c += 1
        print()
        print("Yasakli sayi atlandi")
        continue
    print(c, end=", ")
    c += 1
else:
    print("Loop ici Ende")

print("Loop sonrasi devam...")
