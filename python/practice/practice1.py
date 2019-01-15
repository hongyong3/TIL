import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.international_lst .stock_up'):
    a = tag.select_one('.stock_item').text
    b = tag.select_one('.stock_price').text
    print(f'{a} - {b}입니다.')

    