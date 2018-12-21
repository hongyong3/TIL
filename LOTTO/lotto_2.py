import random
import requests
import json
from pprint import pprint

"""
0. random으로 로또번호를 생성합니다. (내가 살 번호)
1. api 를 통해 우승 번호를 가져옵니다. (1주일에 한번)
2. 0번과 1번을 비교하여 나의 등수를 알려준다.
----------
1. url 요청 보내서 정보를 가져온다.
    -json으로 받는다. (딕셔너리로 접근 가능)
2. api 의 당첨번호와 보너스 번호를 저장하고,
3. 뽑은게 몇등인지, 몇번만에 당첨된건지 하는거 뽑는다. 끝.
"""
# 1. random으로 로또번호를 생성한다.

# url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# main_num = []
# bonus_num = [(lotto["bnusNo"])]
# same = 0
# count = 0

# for i in range(1,7):
#     single_num = lotto.get(f"drwtNo{i}")
#     main_num.append(single_num)
# # print(main_num)


# # print(same, second_same)

# while same < 7:
#     numbers = random.sample(range(1, 46), 6)
#     same = (len(set(numbers) & set(main_num)))
#     second_same = (len(set(numbers) & set(bonus_num)))
#     count += 1
    
#     if same == 6:
#         print(f"1등입니다!!!!!!!")
#         same = 8
#     elif same ==5:
#         print(f"3등입니다!!!!!!!")
#         if bonus_num == 1:
#             print(f"2등입니다!!!!!!")
#     elif same ==4:
#         print(f"4등입니다!!")
#     elif same ==3:
#         print(f"5등입니다!!!")
#     else:
#         print(f"다음기회에..")
    
# print(f"도전 횟수는 {count}입니다.")

# l_num = set(lotto)
# lucky = res.json("")



# pprint(lotto)
# pprint(type(lotto))


#선생님 해설
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]
print("이번 주 당첨번호: " +str(winner))
print("보너스 번호: " +str(bonus))

count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등")
        break
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ',')
        print("쓴 돈은", money)
    # elif matched ==5:
    #     if bonus in my_numbers:
    #         print(" 2등")
    #     else:
    #         print("3등")
    # elif matched == 4:
    #     print("4등")
    # elif matched == 3:
    #     print("5등")
        # print(count, "번만에 당첨되셨습니다.")
        # money = format(count*1000, ',')
        # print("쓴 돈은", money)
    # else:
    #     print("응 안돼")

# 1부터 6까지 해당되는 값을 불러오는 것