# Altersberechnung

input_yas = input("Bitte geben Sie Ihr Geburtsjahr ein !")

input_yas = int(input_yas)

print("Ihr Alter ist : ", 2025-input_yas)


# Mathe

zahl01 = int(input("Gebe eine Zahl ein : "))

zahl02 = int(input("Gebe eine weitere Zahl ein : "))

kare = zahl01*zahl01

iki_kati = zahl02*2

ergebnis = kare+iki_kati


print(str(kare) + "+" + str(iki_kati) + " = " + str(ergebnis))

print(f"{kare}+{iki_kati}=  {ergebnis}")

a = 5
b = 7

print(f"{a}  + {b} = {a+b}")


'''
Kullanicidan adini ve doğum yilini al.
Sonra ekrana şu şekilde yaz:
"Mustafa, şu an 2025 yilindayiz. Sen {yaş} yaşindasin."
f-string kullan.
Doğum yilini int olarak al ve 2025 - doğum_yili işlemi yap.
'''

ad = input("adinizi girin : ")

dogum_yili = int(input("Dogum yilini girin : "))

print(f"{ad}, su an 2025 yilindayiz. Sen {2025-dogum_yili} yasindasin ")

print(ad, ", şu an 2025 yilindayiz. Sen", (2025-dogum_yili), "yasindasin")
