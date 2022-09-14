import requests
import bs4


HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

def get_page(url):
    s = requests.Session()
    responce = s.get(url=url, headers=HEADERS)

    with open('index.html', 'w') as file:
        file.write(responce.text)

def main():
    get_page(url='https://salomon.ru/catalog/')


if __name__ == '__main__':
    main()



# response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
# text = response.text
#
# FAVORITE_HUBS = {'История IT', 'Игры и игровые консоли'}
#
# soup = bs4.BeautifulSoup(text, 'html.parser')
# articles = soup.find_all(class_='tm-article-snippet')
# post_list = []
# for article in articles:
#     article_tag_a = article.find('h2').find('a')
#     article_name = article_tag_a.text
#     article_date = article.find(class_='tm-article-snippet__datetime-published')
#     href = article_tag_a.attrs['href']
#     url = 'https://habr.com' + href
#     post_list.append(url)
# print(post_list)


# def get_habr_link(initial_link, headers):
#     ret = requests.get(initial_link, headers=headers)
#     text = ret.text
#     soup = BeautifulSoup(text, 'html.parser')
#     posts = soup.find_all('article', class_='tm-articles-list__item')
#     post_links = []
#     for post in posts:
#         post_link = post.find('a', class_='tm-article-snippet__hubs-item-link').get('href')
#         post_links.append(post_link)
#
#     print(post_links)
#     return post_links


# for article in articles:
#     hubs = article.find_all(class_='tm-article-snippet__hubs-item')
#     hubs = {hub.find('a').text.strip() for hub in hubs}
#     print(hubs)
#     if hubs & FAVORITE_HUBS:
#         article_tag_a = article.find('h2').find('a')
#         article_name = article_tag_a.text
#         article_date = article.find(class_='tm-article-snippet__datetime-published')
#         href = article_tag_a.attrs['href']
#         url = 'https://habr.com' + href
#         print(f'<{article_date.text}> - <{article_name}> -  {url}')
#         print('-' * 50)

