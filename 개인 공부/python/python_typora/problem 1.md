### 1번

초단위의 시간을 나타내는 임의의 정수를 입력 파라메타로 받아서,
아래의 예시와 같이, "O시간 O분 O초"의 형태로 화면에 출력하는 convert_second_to_hms_time(second) 함수를 작성하십시오. convert_second_to_hms_time(second) 함수는 초(second)를 입력받아 몇h 몇m 몇s의 형태로 출력합니다.
출력은 print() 함수를 이용하여 함수 내부에서 출력하십시오.

예시
입력값 : 3675, 출력 : 1h 1m 15s
입력값 : 675, 출력 : 0h 11m 15s

In [ ]:



```
def convert_second_to_hms_time(second):
    hour = second//3600
    minute = (second%3600)//60
    second2 = (second%3600)%60
    print(str(hour) +'h ' + str(minute) + 'm ' + str(second2) + 's')

"""아래는 위의 예시를 넣은 테스트용 코드"""
convert_second_to_hms_time(3675)
convert_second_to_hms_time(675)
```



### 2번

임의의 네 자리 정수를 입력받아, 아래의 예시와 같이, 각 자리수가 뒤집어진 정수를 반환(return)하는 함수
reverse_number4(number)를 작성하십시오.

reverse_number4(number)는 입력받은 네 자리 정수 number의
1000의 자리 수를 1의 자리로
100의 자리 수를 10의 자리로
10의 자리 수를 100의 자리로
1의 자리 수를 1000의 자리로 변경하는 함수입니다.

예시)
입력값 : 1234, 출력 : 4321
입력값 : 4321, 출력 : 1234

함수는 내부에서 별도의 출력 없이, 뒤집어진 정수값을 반환(return) 합니다.

In [ ]:



```
def reverse_number4(number):
    firstnumb = number//1000
    secondnumb = (number%1000)//100
    thirdnumb = ((number%1000)%100)//10
    fourthnumb = ((number%1000)%100)%10
    return fourthnumb * 1000 + thirdnumb * 100 + secondnumb * 10 + firstnumb

"""아래는 위의 예시를 넣은 테스트용 코드"""
print(reverse_number4(4321))
```



### 3번

round(float) 함수는 실수를 입력받아 소수점 첫째 자리에서 반올림하여 반환하는 함수이다.
예를 들어 입력이 3.14 인 경우, 3을 반환하며, 입력이 3.55인 경우 4를 반환한다.

Typecast(int(), float()와 같은 함수)를 활용하여, round(float)와 같이 실수를 입력받아 소수점 첫째 자리에서 반올림하여 반환하는 함수
my_round(float)함수를 작성하시오.

In [ ]:



```
def my_round(float):
    int_float = int(float)
    return int_float + int((float- int_float) * 2)

'''아래는 위의 예시를 넣은 테스트용 코드'''
print(my_round(3.14))
print(my_round(3.55))
```