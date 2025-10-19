from http.server import HTTPServer, SimpleHTTPRequestHandler

def baslat(port=8000):
    print(f"🌍 Web sunucusu başlatılıyor... http://localhost:{port}")
    sunucu = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    sunucu.serve_forever()

if __name__ == "__main__":
    baslat()
