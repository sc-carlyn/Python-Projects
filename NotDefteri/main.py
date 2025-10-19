def not_yaz():
    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        not_metni = input("Yeni not: ")
        dosya.write(not_metni + "\n")
    print("Not kaydedildi! 🖊️")

def notlari_oku():
    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            print("\n📖 Kayıtlı Notlar:")
            print(dosya.read())
    except FileNotFoundError:
        print("Henüz hiç not yok.")

if __name__ == "__main__":
    while True:
        secim = input("\n1- Not yaz\n2- Notları oku\n3- Çıkış\nSeçim: ")
        if secim == "1":
            not_yaz()
        elif secim == "2":
            notlari_oku()
        elif secim == "3":
            print("Görüşmek üzere! 👋")
            break
        else:
            print("Geçersiz seçim.")
