# 20191203

## Alogorithm - sort - Programmers

### 가장 큰 수 



- 가장 큰 수

- darklight

  sublimevimemacs

  Python3 

###### 문제 설명

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

##### 입출력 예

| numbers           | return |
| ----------------- | ------ |
| [6, 10, 2]        | 6210   |
| [3, 30, 34, 5, 9] |        |



#### 입력

```python
numbers1 = [6, 10, 2]
print(solution(numbers1))
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))
numbers3 = [12, 121]
print(solution(numbers3))
numbers4 = [21, 212]
print(solution(numbers4))
```





#### 1번 시도 : 시간초과

```python
def solution(numbers):
    answer = ''
    number = []
    numbers = list(map(str, numbers))
    for i in numbers:
        if len(i) == 4:
            number.append([i, i * 3])
        if len(i) == 3:
            number.append([i, i * 4])
        if len(i) == 2:
            number.append([i, i * 6])
        if len(i) == 1:
            number.append([i, i * 12])
    number.sort(key = lambda x:x[1], reverse = True)
    for i in number:
        answer += i[0]
    print(answer)
    return answer
```



#### 2번 시도 : 시간초과

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    number = []
    for i in numbers:
        number.append((i * 12, i))
    number = sorted(number, reverse = True)
    for i in number:
        answer += i[1]
    return answer

```



#### 3번 시도 : 시간초과

##### 힌트

![1575304097801](C:\Users\yong_\AppData\Roaming\Typora\typora-user-images\1575304097801.png)

* `int`가 아닌 `str`을 sort하면, 수의 크기에 따라 정렬하는게 아니라

  **각 자리의 크기에 따라 비교**하는 것 같다.



```python
def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    number = []
    for i in numbers:
        number.append((i * 12, i))
    numbers.sort(key =  lambda x : x * 12, reverse = True)	# 위의 과정을 lambda로
    for i in numbers:										# x * 12 : 이유는 자리수 통일
        answer += i
    return answer
```



#### 4번 시도 : 시간초과

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    numbers.sort(key =  lambda x : x * 12, reverse = True)
    for i in numbers:
        answer += i
    return answer
```



#### 5번 시도 : 해결

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    numbers.sort(key =  lambda x : x * 12, reverse = True)
    return str(int(''.join(numbers)))
```



#### 6번 시도 : 

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    numbers.sort(key =  lambda x : x * 3, reverse = True)	# x * 3 을 해도 된다.
    return str(int("".join(numbers)))
```

