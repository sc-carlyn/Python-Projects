import requests

def hava_durumu(sehir):
    api_key = "2435a6c123c861a4e64634f8d7c48baa"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&lang=tr&units=metric"
    yanit = requests.get(url).json()
    if yanit.get("cod") != 200:
        print("Şehir bulunamadı 😕")
        return
    ad = yanit["name"]
    sicaklik = yanit["main"]["temp"]
    durum = yanit["weather"][0]["description"]
    print(f"{ad}: {sicaklik}°C, {durum.capitalize()} ☀️")

if __name__ == "__main__":
    sehir = input("Şehir adı: ")
    hava_durumu(sehir)
