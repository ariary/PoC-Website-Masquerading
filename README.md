<div align=center>
<p><strong><code>Another good reason to be careful when running script from untrusted source with sudo, or to not give to all users root capabilities</code></strong></p>
</div>

|DEMO  🎭 |
|:---:| 
|![demo](https://github.com/ariary/PoC-Website-Masquerading/blob/main/poc.gif)|

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


### Notes

* 2 command needs sudo (modifying /etc/host & launch https server on 443)
* To ease cert regisstration in trust store the PoC use [`mkcert`](https://github.com/FiloSottile/mkcert) but it could be done manually w/ `openssl` 
    * Hence the "certutil" is a prerequisite to make the PoC works for Chrome or Firefox
* Need Browser restart to make it works
