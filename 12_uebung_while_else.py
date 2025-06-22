
i=1

while i < 3 :
    print(i)
    i+=1
else:
    print("Tamamlandi.")
    
# indentation (girinti) yapisinin önemi


i = 0
while i < 3:
    sayi = int(input("Sayi gir: "))
    if sayi < 0:
        print("Negatif")
    elif sayi == 0:
        print("Sifir")
    else:
        print("Pozitif")
        i += 1  # sadece pozitifse calisir!


    

# Kullanicidan sayi al. Sayi negatifse döngüyü bitir. Pozitifse "Tamam" yaz. Ama sadece 5 hak ver.


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
        
    # Bu satir artik if-elif-else'e ait değil
        
    count += 1 # tüm koşullardan sonra bir defa artar

if count == 6:
    print("5 hak bitti!")
    
    

'''
-Kullaniciya en fazla 4 giriş hakki ver.
-Şifre "python2024" ise → 'Giriş başarili'
-Hataliysa tekrar denesin.
-4 kez yanlişsa → 'Hesap bloke oldu' yaz.

'''

#1. yol

sayac=0

while sayac < 4 :
    giris=input("Lütfen Sifrenizi giriniz : ")
    sayac +=1
        
    if giris == "kartal1903":
        print("Giris basarili")
        break
        
    if sayac == 4:
        print("Gecmis olsun hesap bloke oldu")
        
#2.yol

sayac=0

while sayac < 4 :
    
    giris=input("Lütfen Sifrenizi giriniz : ")
    
        
    if giris == "kartal1903":
        print("Giris basarili")
        break
        
    print("Hatali giris, tekrar deneyin")
    sayac+=1
    
    if sayac ==4:
        print("Gecmis olsun hesap bloke oldu")

#3. yol
sifre=""
sayac=0

while sifre !="kartal1903" :
#   
      user_input_sifre=input("Lütfen sifrenizi girin : ")
      sayac+=1
      
      if user_input_sifre=="kartal1903" :
          print("Giris basarili")
          break 
      
      if sayac==4 :
          print("Hesap bloke oldu")
          break
      

      
 

      
      