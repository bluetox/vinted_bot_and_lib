import http.client
import socks
import json
from urllib.parse import quote_plus

def get_said_articles(search_params, vinted_session_headers,per_page):
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)  # Tor proxy running on localhost:9050
    http.client.HTTPConnection = socks.socksocket
    get_articles_data = http.client.HTTPSConnection("www.vinted.com")
    get_articles_data.request("GET", f"/api/v2/catalog/items?page=1&per_page={per_page}&{search_params}", headers=vinted_session_headers)
    raw_articles_data = get_articles_data.getresponse().read().decode('utf-8')
    return json.loads(raw_articles_data)['items']
