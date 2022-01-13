# WebsiteMasquerade
PoC on how to impersonnate/masquerade a website for a target device

Met en evidence que l'utilisation de sudo [script] est dangereux quand on connait pas le script

1. Modifier etc/host
2. Lancer serveur local (comme on a sudo on peut utiliser 443): page spawn
3. utiliser mkcert pour trust le certif
4. 


./mkcert -install
./mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1


CLEAN
mkcert -uninstall
./mkcert -CAROOT --> Chemin 
rm -rf $(./mkcert -CAROOT)
