import http.client
from bs4 import BeautifulSoup
import re

def remove_non_text_characters(text):
    return re.sub(r'[^\w\s]', '', text)

def find_article_images(item_id, title):
    image_urls = []
    
    cleaned_title = remove_non_text_characters(title)
    text_part_url = cleaned_title.replace(" ", "-").lower()
    text_part_url = text_part_url.rstrip(" -")

    conn = http.client.HTTPSConnection("www.vinted.com")
    conn.request("GET", f'/items/{item_id}-{text_part_url}')
    resp = conn.getresponse()
    if resp.status == 200:
        data = resp.read()
        soup = BeautifulSoup(data, 'html.parser')
        for i in range(1, 5):
            img_tags = soup.find_all('img', attrs={'data-testid': f'item-photo-{i}--img'})
            for img in img_tags:
                image_urls.append(img['src'])
    else:
        print("Failed to retrieve the webpage")

    conn.close()
    return image_urls
