#문제 0번

calender = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
            7: 31, 8:31, 9: 30, 10: 31, 11: 30, 12: 31
}
weeks = ['일', '월', '화', '수', '목', '금', '토']

for month, count_day in calender.items():
    count = 0
    print(month, '월')
    for day in weeks:
        print(day, end =' ')
    print()

    for i in range(1, count_day + 1):
        print(i, end=' ')
        count += 1
        if count == 7:
            print()
            count = 0
    print(end='\n\n')

#문제 1번
#두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 
#가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

n = 5
m = 9

#정답
print(("*" * n + "\n")*m)