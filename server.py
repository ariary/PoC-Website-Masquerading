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
