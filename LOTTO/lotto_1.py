from bs4 import BeautifulSoup
import requests
import random

# numbers = random.sample(range(800, 838), 8)
# for times in range(8):
#     url = f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" +str(times)
#     req = requests.get(url).text
#     Soup = BeautifulSoup(req, 'html.parser')
#     lucky = ".nums .win .ball_645")
#     bonus = ('#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span')
#    lucky = info
#     print(f"{name} 차 당첨번호는 {lucky} + {bonus}입니다.")


numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url =f"https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    Soup = BeautifulSoup(req, 'html.parser')
    lucky = Soup.select(".ball_645")
    print(f"{num} 회차번호")
    for i in lucky:
        # end는 일렬로 만들어주는 것, 숫자를 불러와서 {에 하나씩 나오도록 만들기
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()