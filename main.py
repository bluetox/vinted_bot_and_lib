from session import update_vinted_cookies
from get_articles import get_said_articles
from extract_articles import extract_article_data


print("Salut tu as la chance de tester la v1 de mon bot vinted opensource.\nCe que tu vas voir represente une petite nuit de travail en soit car j'avais deja beaucoup travaillé avec l'API.")
items_part = input("Rend toi sur https://www.vinted.com/catalog choisie tes criteres puis copies l'url à partir d'après catalog?: ")
per_page = input("nombre d'articles par page : ")
while True:
    headers = update_vinted_cookies()
    all_articles_data = get_said_articles(items_part,headers,per_page)

    for item in all_articles_data:
        article_data = extract_article_data(item)
        for key, value in article_data.items():
            print(f"{key}: {value}")
        
        print('')
        