"""
Web Portfolio & Blog — Навчальний веб-проєкт
Автор: Оржеховський Захар (група КН-2/1)
"""

import http.server
import socketserver
import webbrowser

PORT = 8000


def main():
    print(f"==================================================")
    print(f"🚀 Запуск локального сервера для проєкту...")
    print(f"🌐 Адреса: http://localhost:{PORT}")
    print(f"⏹ Для зупинки натисніть Ctrl+C")
    print(f"==================================================")
    
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер успішно зупинено.")


if __name__ == "__main__":
    main()
