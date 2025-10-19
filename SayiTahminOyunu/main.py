import random

def oyun():
    hedef = random.randint(1, 100)
    tahmin_sayisi = 0
    print("🎯 1 ile 100 arasında bir sayı tuttum. Tahmin et bakalım!")

    while True:
        tahmin = int(input("Tahminin: "))
        tahmin_sayisi += 1
        if tahmin < hedef:
            print("Daha büyük bir sayı dene 🔼")
        elif tahmin > hedef:
            print("Daha küçük bir sayı dene 🔽")
        else:
            print(f"Tebrikler! 🎉 {tahmin_sayisi} denemede buldun.")
            break

if __name__ == "__main__":
    oyun()
 