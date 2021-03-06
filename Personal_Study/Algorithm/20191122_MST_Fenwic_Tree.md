# 20191122

## Algorithm

### 펜윅 트리(Fenwick Tree, Binary Indexed Tree; BIT)



#### 1) 펜윅 트리

* 펜윅 트리는 세그먼트 트리의 메모리를 절약하기 위해 만든 방법으로 코드도 매우 간결

  즉, 펜윅 트리는 세그먼트 트리의 변형으로써

* update *O(logN)*에 query *O(logN)*를 수행 할 수 있어 메모리는 세그먼트 트리에 비해 덜 소모

* 펜윅 트리의 핵심은 `구간 합 대신 부분 합만을 빠르게 계산할 수 있는 자료 구조를 만들어도 구간 합을 계산할 수 있다`

  (이 때 부분 합은 `0 ~ k`까지의 합이고, 구간 합은 `a ~ b` 까지의 합을 의미)



#### 2) 세그먼트 트리와 펜윅 트리의 비교

##### 1) 세그먼트 트리

![img](https://t1.daumcdn.net/cfile/tistory/2506D04D58C91F6005)



##### 2) 펜윅 트리

![img](https://t1.daumcdn.net/cfile/tistory/257FDE4858C9211F04)



##### 2 - 1 ) 초기 펜윅 트리 도식화

![img](https://t1.daumcdn.net/cfile/tistory/223A5E5058C922EE23)



* 펜윅 트리는 비트를 이용하기 때문에 인덱스를 0이 아닌 1번부터 시작(index + 1)



##### 2 - 2) 최종 펜윅 트리 도식화

![img](https://t1.daumcdn.net/cfile/tistory/2333064C58C9236F0E)



#### 3) 펜윅 트리의 동작 방식

##### 3 - 1) 펜윅 트리의 업데이트 방식

* ex) 1번 인덱스의 값을 변경한다면?

![img](https://t1.daumcdn.net/cfile/tistory/2372B04E58C9246738)

​	`(1)`, `(1 - 2)`, `(1 - 4)`, `(1 - 8)`, `(1 - 16)` 업데이트



* ex) 7번 인덱스의 값을 변경한다면?

![img](https://t1.daumcdn.net/cfile/tistory/2373BF4958C924E411)

​	`(7)`, `(1 - 8)`, `(1 - 16)` 업데이트



* ex 15번 인덱스의 값을 변경한다면?

![img](https://t1.daumcdn.net/cfile/tistory/2605124858C9254B17)

​	`(15)`, `(1 - 16)` 업데이트



##### 3 - 2) 펜윅 트리의 구간 합 방식

* ex) 인덱스 5~15번 사이의 구간합을 구하고 싶다면?

![img](https://t1.daumcdn.net/cfile/tistory/257E9F4F58C9266E15)

​	`(1 - 8)` + `(9 - 12)` + `(13 - 14)` + `(15)` - `(1 - 4)`



* ex) 인덱스 1~7번 사이의 구간합을 구하고 싶다면?

![img](https://t1.daumcdn.net/cfile/tistory/273DA74958C926D20A)

​	`(1 - 4)` + `(5 - 6)` + `(7)`



#### 4) 펜윅 트리의 비트 방식

##### 4 - 1) 비트 방식으로 도식화한 펜윅 트리

![img](https://t1.daumcdn.net/cfile/tistory/247AA84D58C9299317)



* ex) 인덱스 5 ~ 15번 사이의 구간합을 구하고 싶다면?

![img](https://t1.daumcdn.net/cfile/tistory/2606F64958C92AFC24)

* `(1 - 8)` + `(9 - 12)` + `(13 - 14)` + `(15)` - `(1 - 4)`에서

  `(1 - 8)` + `(9 - 12)` + `(13 - 14)` + `(15)` -> 8 + 12 + 14 + 15로 나타낼 수 있다.

  또한, 111**1** + 11**1**0 + 1**1**00 + 1000 이라는 비트로 바뀌는 것을 확인 할 수 있다.

  즉, **1이 있는 가장 오른쪽(최하위 비트)가 0으로 바뀌는 모습을 볼 수 있다.**



* ex) 인덱스 1 ~ 13번 사이의 구간합을 구하고 싶다면?

![img](https://t1.daumcdn.net/cfile/tistory/2373AB4D58C92E3125)

* `(1 - 8)` + `(9 - 12)` + `(13)`에서

  `(1 - 8)` + `(9 - 12)` + `(13)` -> 8 + 12 + 13으로 나타낼 수 있다.

  또한, 110**1** + 1**1**00 + 1000 이라는 비트로 바뀌는 것을 확인 할 수 있다.

  이 역시, **1이 있는 가장 오른쪽(최하위 비트)가 0으로 바뀌는 모습을 볼 수 있다.**



##### **반대로 업데이트는 ** 있는 가장 오른쪽 최하위 비트에 1을 더해가면 update가 가능

- ex) 7번 인덱스의 값을 변경한다면?

![img](https://t1.daumcdn.net/cfile/tistory/2373BF4958C924E411)

* `(7)`,  `(1 - 8)`, `(1 - 16)`에서

  `(7)`,  `(1 - 8)`, `(1 - 16)` -> 7, 8, 16으로 나타낼 수 있다.

  또한, 11**1 **-> **1**000 -> 10000 이라는 비트가 되는데

  이 역시 11**1**에  1을 더하면 1000이 되고, **1**000에 1을 더하면 10000이 된다는 것을 알 수 있다.



# 20191124

## Algorithm

### 펜윅 트리(Fenwick Tree, Binary Indexed Tree; BIT)



#### 5) 펜윅 트리 소스코드

```python
import sys
sys.stdin = open("D4_3064_input.txt", "r")

def getSum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        # 핵심 코드
        # :: 원리 ::
        # 1100이 있다고 생각하면 1100의 2의 보수는 0011에서 + 1을 한 0100
        # 즉, 1100은 val 0100은 - val
        # 이 두개를 & 연산을 하게 된다면 0100이 되는데 이때 1은 최하위 비트 위치를 의미.
        #  위의 예시를 이용하여 일반적인 식을 도출하면 ( i & - i)을 이용하면 최하위 비트를 구할 수 있음.
        i -= (i & - i)  # 최하위 비트 지우기
    return ans

def addTree(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & - i)  # 최하위 비트 더하기

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data, tree = [0], [0] * (N + 1)
    data.extend(list(map(int, input().split())))
    answer = []
    for i in range(1, N + 1):
        addTree(i, data[i])

    for i in range(M):
        c, x, y = map(int, input().split())
        if c == 1:
            addTree(x, y)
        else:
            answer.append(getSum(y) - getSum(x - 1))
    print("#{}".format(test_case + 1), *answer)



```

