# WebsiteMasquerade
PoC on how to impersonnate/masquerade a website for a target device

Met en evidence que l'utilisation de sudo [script] est dangereux quand on connait pas le script

1. Modifier etc/host
2. Lancer serveur local (comme on a sudo on peut utiliser 443): page spawn
3. utiliser mkcert pour trust le certif
4. 

curl https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64 -LO

./mkcert -install
./mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1

./mkcert -key-file key.pem -cert-file cert.pem github.com localhost 127.0.0.1 ::1

CLEAN
mkcert -uninstall
./mkcert -CAROOT --> Chemin 
rm -rf $(./mkcert -CAROOT)

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Beware when you run sudo for anything!')

httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="/tmp/headi/example.com+5-key.pem", 
        certfile='/tmp/headi/example.com+5.pem', server_side=True)

httpd.serve_forever()
