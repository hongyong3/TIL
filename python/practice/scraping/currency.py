#원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.
#import requests
#req = requests.get('주소').text

# import requests
# from bs4 import BeautifulSoup   

# #그 사이트에서 요청을 받는다.
# #BeautifulSoup로 전체를 꾸며준다.
# #그 중 특정 내용을 뽑은다.
# #print(kospi)를 하면 그 내용 전체가 나오고 // print(kospi.text)를 하면 코스피 지수만 나온다.

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)

# req = requests.get("https://www.coupang.com/vp/products/147536347?itemId=426849212&vendorItemId=4051746003&from=home_CategoryBest_ranking&traid=home_CategoryBest_ranking").text
# soup = BeautifulSoup(req, 'html.parser')
# price = soup.select_one("#contents > div.prod-atf > div > div.prod-buy.new-oos-style.not-loyalty-member.not-eligible-address.without-subscribe-buy-type.DISPLAY_0.only-one-delivery > div.prod-price-container.prod-not-show-ccid-ifip > div.prod-price > div > div.prod-sale-price.prod-major-price > span.total-price > strong")
# print(price.text)

import requests
from bs4 import BeautifulSoup

# url = "https://www.naver.com/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# '.PM_CL_realtimeKeyword_rolling '>' ah_item'   //------------ '>'는 직속 자식의 개념이고, ' .'은 어떤관계에 상관없이 그 하위버전 아무거나 가능하다.

# for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
#     rank = tag.select_one(' .ah_r').text
#     name = tag.select_one(' .ah_k').text
#     print(f'{rank}위는 {name} 입니다.')


req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
for tag in soup.select(' .PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one(' .ah_r').text
    name = tag.select_one(' .ah_k').text
    print(f'{rank}위는 {name} 입니다.')