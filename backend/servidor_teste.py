import http.server
import socketserver

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Servidor de teste rodando em http://0.0.0.0:{PORT}")
    httpd.serve_forever()
