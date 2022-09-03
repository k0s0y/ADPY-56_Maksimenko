import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/'
              'apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'habr_web_home_feed=/all/; hl=ru; fl=ru; _ym_uid=1635146998930217765; '
              '_ym_d=1660119369; _ga=GA1.2.415524467.1660119369; visited_articles=470285:473838; '
              '_ym_isad=1; _gid=GA1.2.1543349228.1661929232',
    'Host': 'habr.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "macOS",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
link = 'https://habr.com/ru/all/'

DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']


def get_habr_link(initial_link, headers):
    ret = requests.get(initial_link, headers=headers)
    text = ret.text
    soup = BeautifulSoup(text, 'html.parser')
    posts = soup.find_all(class_='tm-article-snippet')
    post_links = []
    for post in posts:
        post_tag_a = post.find('h2').find('a')
        href = post_tag_a['href']
        post_links.append(href)
    return post_links


def check_habr_links(post_links):
    for post_link in post_links:
        ret = requests.get(f'https://habr.com{post_link}')
        text = ret.text
        soup = BeautifulSoup(text, 'html.parser')
        post_habs = soup.find_all(class_='tm-article-snippet__hubs-item')
        post_text = soup.find(id='post-content-body').get_text(' ')
        if (check_post_habs(post_habs) or check_post_text(post_text)) == 1:
            post_time = soup.find('time').get('title')
            post_header = soup.find('h1').find('span').text
            print(f'\n {post_time} - {post_header} - https://habr.com{post_link}')


def check_post_habs(post_habs):
    for post_hab in post_habs:
        post_hab_span = post_hab.find('span').text
        post_hab_low = post_hab_span.lower().strip(' ')
        if any([post_hab_low in desired for desired in DESIRED_HUBS]):
            return 1


def check_post_text(post_text):
    for word in DESIRED_HUBS:
        if word in post_text:
            return 1


if __name__ == '__main__':
    check_habr_links(get_habr_link(link, HEADERS))
