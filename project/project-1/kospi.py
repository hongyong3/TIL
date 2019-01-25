import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com")
url = 'https://finance.naver.com/sise/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print(f'현재 코스피 지수는 {kospi.text}')



# soup = Beautifulsoup.(req, 'html.parse')
# kospi = requests.get("https://www.google.com")
# kospi = soup.select_one('경로')
