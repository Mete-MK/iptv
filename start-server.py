import http.server, socketserver, socket, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8000
socketserver.TCPServer.allow_reuse_address = True

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

with socketserver.ThreadingTCPServer(("", PORT), Handler) as srv:
    print("IPTV Player laeuft.")
    print("Oeffne in Safari auf iPhone/iPad (gleiches WLAN):\n")
    print(f"    http://{lan_ip()}:{PORT}\n")
    print("Beenden mit Strg+C")
    srv.serve_forever()
