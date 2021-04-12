# 20190404

## Algorithm

### 순열, 조합의 구조



#### 기본구조

~~~python
def 함수(idx, start):
    
    if idx == N: # 원하는결과수
        print('결과')
        return
    for i in range(start, 경우의수): # 순열 : start = 0 / 결과를 뽑을 수 있는 경우의 수 
        # if visit[i]: continue
        # visit[i] = 1
        check[idx] = i
        함수(idx+1, start or start+1)
      # visit[i] = 0

```



### start 값 있으면(이전에 선택한것부터 시작하면) 조합

- start 에서 시작하면 중복조합
- start + 1 에서 시작하면 조합



### start 값 없으면(처음부터 시작하면) 순열

- visit 체크하면 순열
- visit 체크 안하면 중복순열
~~~



---

# 20190921

## Algorithm

### 순열과 조합



#### 순열(permutation)

- 순열은 서로 다른 n개의 대상에서 r개를 뽑아 일렬로 배열한 것.
- 경우의 수는 **~n~P~r~**로 표현



```python
def permutation(arr, r):
    # 1
    arr = sorted(arr)
	used = [0 for _ in range(len(arr))]
    
    # 2
    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return
        
        # 3
       	for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
	generate([], used)
    
------------------------------------------------------------------------------
permutation([1, 2, 3, 4, 5], 3)
permutation('ABCD', 2)
```



##### # 1.

> 먼저 사용자가 원하는 arr과 r을 받음.
>
> used 변수를 만드는데, 이 변수는 i번째 값을 썼는지 저장하는데 사용.
>
> 중복값 저장 X



##### # 2.

> 실제 수열을 만들 generate() 함수를 생성.
>
> chosen 변수는 순열의 원소를 저장하는 변수인데 이 배열에 값을 하나씩 저장하다가 그 개수가
>
> r이 되는 순간 하나의 순열이 만들어진 것이므로 출력 후 종료



##### # 3. ( 핵 심)

> 모든 순열은 arr의 0 ~ i - 1번째 값으로 시작하기에 for 문으로 다 만들어야함.
>
> 그리고 chosen에 값을 추가 후, used에 해당 변수를 사용했다고 check.
>
> 그 다음 generate를 반복.
>
> 순열 하나가 만들어 진 후 그 값을 uncheck



------



#### 조합(combination)

- n개 중에 r개를 뽑되, 순서를 고려하지 않음.
- 경우의 수는 **~n~C~r~**로 표현



```python
def combination(arr, r):
    # 1
    arr = sorted(arr)
    # 2
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        # 3
        start = arr.index(chosen[- 1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen)
            chosen.pop()
	generate([])
    
------------------------------------------------------------------------------
combination('ABCDE', 3)
combination([1, 2, 3, 4, 5], 3)
```



##### # 1.

> 배열을 정렬.



##### # 2.

> 조합을 만드는 generate() 함수를 생성.
>
> chosen에 저장된 아이템의 개수가 r개이면 출력하고 함수를 종료.



##### # 3.

> for 문을 돌리되, 시작을 chosen에 저장된 마지막 값 다음으로 정함.
>
> 조합은 순열과 달리 순서를 고려하지 않고 뽑기 때문에, 가짓수를 제한해줘야 함.
>
> start가 chosen이 비어있을 경우 0이 되는 것도 참고.
>
> 빈 값일 때는 그냥 0을 넣어야 함.





---

# 20210412

## Algorithm

### 조합



```python
def combi(arr, m):
    ret = []
    if m > len(arr):
        return ret
    if m == 1:
        for i in arr:
            ret.append([i])
    else:
        for i in range(len(arr) - m + 1):
            for j in combi(arr[i + 1:], m - 1):
                ret.append([arr[i]] + j)
    return ret

arr = [i for i in range(1, n + 1)]
ans = combi(arr, m)

for i in ans:
    print(*i)
```

