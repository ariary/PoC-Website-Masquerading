<div align=center>
<p><strong><code>Another good reason to be careful when running script from untrusted source with sudo, or to not give to all users root capabilities</code></strong></p>
</div>

|DEMO|
|:---:| 
|![demo](https://github.com/ariary/JSextractor/blob/main/img/jse-tui.gif)|

## PoC

This a simple PoC on how to impersonnate a website locally. 

After that you can imagine multiple scenarios. For example stealing credentials, by making the local server (which impersonates the target website) having the same frontend as the target but interacting with a remote server to exfiltrate the credentials. 

It highlights the importance to monitor the capabilities given to scripts/users etc as it this snipset could be integrated in any malicious script or by any user having root privileges.

### How it works

<strong>~> Launch `poc-impersonate` </strong>

1. Modify `/etc/host` to route the target domain to localhost. **Note**:the content of `/etc/hosts` is used before making DNS resolution at each request so it is priority. <sup>need sudo</sup>
2. Make locally trusted certificates, it is important to avoid the "warning" page of the browser. Certs could be installed in the trusted store of the whole system, in this PoC it is only installed for the user launching the script.
3. Launch a local server on port `443`. <sup>need sudo</sup>

<strong>~> Visit the target website (here `https://www.github.com`) </strong>

See that you aren't were you wanted to. (You reach the local server) 

<strong>~> Clear your tracks with `clean`</strong>

It stops local server, withdraws certs in trust store, and put `/etc/hosts` as it was before the PoC






curl https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64 -LO

./mkcert -install ~creation key + cert + cert in trust store exemple pour Firefox in ~/.mozilla/certificates
https://wiki.mozilla.org/CA/AddRootToFirefox
https://betterprogramming.pub/trusted-self-signed-certificate-and-local-domains-for-testing-7c6e6e3f9548
./mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1

./mkcert -key-file key.pem -cert-file cert.pem github.com localhost 127.0.0.1 ::1

CLEAN
mkcert -uninstall
./mkcert -CAROOT --> Chemin 
rm -rf $(./mkcert -CAROOT)


{ echo -ne "HTTP/1.0 200 OK\r\n\r\n"; cat some.file; } | nc -l -p 8080 //simple server https://unix.stackexchange.com/questions/32182/simple-command-line-http-server

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
