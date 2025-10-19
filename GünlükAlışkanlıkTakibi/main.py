import json
from datetime import date

def yukle():
    try:
        with open("data.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}

def kaydet(veri):
    with open("data.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, indent=2, ensure_ascii=False)

def aliskanlik_tamamla():
    veri = yukle()
    bugun = str(date.today())
    aliskanlik = input("Tamamladığın alışkanlık: ")
    if bugun not in veri:
        veri[bugun] = []
    veri[bugun].append(aliskanlik)
    kaydet(veri)
    print(f"✅ {aliskanlik} kaydedildi ({bugun})")

def gunluk_rapor():
    veri = yukle()
    bugun = str(date.today())
    print(f"\n📅 {bugun} Alışkanlıkları:")
    for item in veri.get(bugun, []):
        print(f" - {item}")
    print()

if __name__ == "__main__":
    while True:
        secim = input("1- Alışkanlık ekle\n2- Bugünün raporu\n3- Çıkış\nSeçim: ")
        if secim == "1":
            aliskanlik_tamamla()
        elif secim == "2":
            gunluk_rapor()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim.")
