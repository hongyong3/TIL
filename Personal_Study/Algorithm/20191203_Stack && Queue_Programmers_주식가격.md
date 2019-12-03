# 20191203

## Algorithm - Stack && Queue - Programmers

### 주식가격



###### 문제 설명

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

##### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

##### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

##### 입출력 예 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.



#### 입력

```python
prices1 = [1, 2, 3, 2, 3]
print(solution(prices1))
prices2 = [4, 7, 2, 5, 3]
print(solution(prices2))
prices3 = [4, 1, 2, 7, 7]
print(solution(prices3))
```



#### 1번 시도

##### 정확성 : 통과

##### 효율성 : 시간 초과

```python
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        j = i + 1
        while j < len(prices):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            if j == len(prices) - 1:
                answer[i] = j - i
            j += 1
    return answer
```



#### 2번 시도

##### 해결

```python
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):	# while을 for로 변경
            if prices[i] > prices[j]:		# 이유
                answer[i] = j - i			# 속도 : for > while
                break						# 메모리사용량 : for > while
            if j == len(prices) - 1:
                answer[i] = j - i
    return answer
```

