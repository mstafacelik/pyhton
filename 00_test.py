
import random

dogru_sayi = random.randint(1, 20)

for hak in range(3):
    tahmin = int(input("Random sayiyi tahmin et: "))

    if tahmin == dogru_sayi:
        print("Doğru tahmin!")
        break
    elif tahmin < dogru_sayi:
        if hak < 2:
            print("El büyüt")
    else:
        if hak < 2:
            print("El kücült")

else:
    print(f"Game over, hakkin doldu. Dogru sayi: {dogru_sayi}")