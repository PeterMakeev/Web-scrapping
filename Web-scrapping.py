import requests
from bs4 import BeautifulSoup

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all("article")

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    preview_text = article.find('div').text
    date = article.find('time').text
    title = article.find(class_='tm-article-snippet__title-link').find('span').text
    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    url_post = base_url + href

    for word in KEYWORDS:
        if (word.lower() in title.lower()) or (word.lower() in hubs) or (word.lower() in preview_text.lower()):
            print(f'Дата: {date} - Заголовок: {title} - Ссылка: {url_post}')
