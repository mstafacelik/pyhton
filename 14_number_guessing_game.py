

'''
🎮 OYUNUN KURALLARI:
Bilgisayar 1 ile 20 arasinda rastgele bir sayi tutacak.

Oyuncunun 5 tahmin hakki olacak.

Her tahminden sonra oyuncuya şöyle geri bildirim verilecek:

🔼 “Daha büyük bir sayi gir” (tahmin küçükse)

🔽 “Daha küçük bir sayi gir” (tahmin büyükse)

✅ “Tebrikler, doğru tahmin!”

5 hakki da biterse: “Tahmin hakkiniz bitti. Doğru sayi: X” mesaji verilecek.
'''


'''
🧠 İpuçlari:
random.randint(1, 20) → sayiyi bilgisayar seçecek

while/for döngüsüyle 3 hak taniyacağiz

break ile doğru tahminde döngüyü bitireceğiz

if, elif, else ile yönlendirme yapacağiz
'''


import random

dogru_sayi = random.randint(1, 20)

sayac=0

while sayac < 3 :
    tahmin=int(input("Tahmin et : "))
    
    if tahmin==dogru_sayi :
        print("Bingo")
        break
    elif tahmin < dogru_sayi:
         if sayac < 2 :
            print("El büyüt")
    else:
        if sayac<2:
            print("El büyüt")
    sayac+=1
    print("sayac: ", sayac)
            
if sayac==3 :
    print("Yetti gariiiii")
    
    




    
    
    
    


    


      