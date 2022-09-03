import requests
import bs4

# ret = requests.get('https://2ip.ru/')
# text = ret.text
# # print(ret.text)
#
# id_pos = ret.text.find('id="d_clip_button"')
# ip_start_pos = ret.text.find('<span>', id_pos) + len('<span>')
# ip_end_pos = ret.text.find('</', ip_start_pos)
# ip = ret.text[ip_start_pos:ip_end_pos]
# print(ip)


# Работаем через bs4
# soup =  bs4.BeautifulSoup(text, features='html.parser')
# d_clip_button = soup.find(id='d_clip_button')
# # print(d_clip_button.text) # тут только один тег с текстом, тч можно выодить сразу текст
# ip_adr = d_clip_button.find('span')
# print(ip_adr.text)

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'habr_web_home_feed=/all/; hl=ru; fl=ru; _ym_uid=1635146998930217765; _ym_d=1660119369; _ga=GA1.2.415524467.1660119369; visited_articles=470285:473838; _ym_isad=1; _gid=GA1.2.1543349228.1661929232',
    'Host': 'habr.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "macOS",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text

FAVORITE_HUBS = {'История IT', 'Игры и игровые консоли'}

soup = bs4.BeautifulSoup(text, 'html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = {hub.find('a').text.strip() for hub in hubs}
    print(hubs)
    if hubs & FAVORITE_HUBS:
        article_tag_a = article.find('h2').find('a')
        article_name = article_tag_a.text
        article_date = article.find(class_='tm-article-snippet__datetime-published')
        href = article_tag_a.attrs['href']
        url = 'https://habr.com' + href
        print(f'<{article_date.text}> - <{article_name}> -  {url}')
        print('-' * 50)

# for article in articles:
#     print(article.text)

# if __name__ == '__main__':
#     pass