import requests
import random

def get_photos(query):
    api_key = 'SNdbZYcePk7TjGrXpC3e9BQsrzxe4fHUpP4B2e2wLvGaXPYdS2K3iiaz'
    headers = {'Authorization': api_key}
    search_query = query
    url = f'https://api.pexels.com/v1/search?query={search_query}&per_page=10&page=1'

    # Ver se faço algum código caso o nome da imagem não esteja disponível, ou for em uma forma que a pesquisa não ache
    response = requests.get(url, headers=headers)
    data = response.json()



    array = []

    for row in data['photos']:
        original_url = row['src']['original']
        array.append(original_url)

    random_num = random.randint(0, 4)

 

    return array[random_num]
