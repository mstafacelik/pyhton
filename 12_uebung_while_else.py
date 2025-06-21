
i=1

while i < 3 :
    print(i)
    i+=1
else:
    print("Tamamlandi.")
    
    

# Kullanıcıdan sayı al. Sayı negatifse döngüyü bitir. Pozitifse "Tamam" yaz. Ama sadece 5 hak ver.


count = 0

while count < 6:

    user_input_sayi = int(input("Bir sayi giriniz : "))

    if user_input_sayi < 0:
        print("Negatif, Ende des Codes!")

    elif user_input_sayi == 0:
        print("0 girdiniz")

    else:
        print("Pozitif sayi girdiniz")
        #count += 1  ❌ sadece else'e ait olur
        
    # Bu satır artık if-elif-else'e ait değil
        
    count += 1 # tüm koşullardan sonra bir defa artar

if count == 6:
    print("5 hak bitti!")
      
      