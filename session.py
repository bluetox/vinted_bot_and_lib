import http.client
import re

def update_vinted_cookies():
    
    headers_connexion = http.client.HTTPSConnection("www.vinted.com")
    headers_connexion.request("GET", "/")
    headers_connexion_response = headers_connexion.getresponse()
    set_cookie_headers = headers_connexion_response.getheaders()
    session_value = None
    for header in set_cookie_headers:
        if header[0] == 'Set-Cookie':
            match = re.search(r'_vinted_fr_session=([^\s;]+)', header[1])
            if match:
                session_value = match.group(1)
                break
    headers = {
        "Cookie": f"_vinted_fr_session={session_value}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
    }
    return headers