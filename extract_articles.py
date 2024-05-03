from parse_image import find_article_images
import time

def extract_article_data(item_data):
    extracted_data = {
        'id': item_data['id'],
        'title': item_data['title'],
        'price': item_data['price'],
        'is_visible': item_data['is_visible'],
        'discount': item_data['discount'],
        'currency': item_data['currency'],
        'brand_title': item_data['brand_title'],
        'user_id': item_data['user']['id'],
        'is_business': item_data['user']['business'],
        'profile_url': item_data['user']['profile_url'],
        'article_urls' :  find_article_images(item_data['id'],item_data['title'])
    }
    time.sleep(2)
    return extracted_data
