
'''
-Kullaniciya en fazla 4 giriş hakki ver.
-Şifre "python2024" ise → 'Giriş başarili'
-Hataliysa tekrar denesin.
-4 kez yanlişsa → 'Hesap bloke oldu' yaz.

'''


sifre=""
sayac=0

while sifre !="kartal1903" :

      user_input_sifre=input("Lütfen sifrenizi girin : ")
      sayac+=1
      
      if user_input_sifre=="kartal1903" :
          print("Giris basarili")
          break 
      
      if sayac==4 :
          print("Hesap bloke oldu")
          break

        


        
    
      

      
 
