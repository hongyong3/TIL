# 20200325

## Algorithm

### 디오판토스 방정식(Diophantine equation)



#### 디오판토스 방정식이란?

주어진 정수 **a**, **b**, **c**에 대하여 

ax + by = c

를 만족하는 정수 x, y를 찾는게 목적.



d = a, b의 최대공약수. 

이 때,

d | c 인 경우, 무한한 x, y가 존재(부정).

d | c 가 아닌 경우, 해는 존재하지 않음(불능).

여기서 d| c 의 의미는 d는 c를 나눌 수 있다는 의미.



해가 존재할 경우,

특수해(Particular Solution)는

x~0~ = c / d * s

y~0~ = c / d * t

로 구함.



이 때 s와 t는 

확장 유클리드 알고리즘(Extended Euclidean AlgorithmExtended Euclidean Algorithm)으로 구한 값.

<https://www.crocus.co.kr/1232> 참고



일반해(General Solution)는

where k∈Z

x = x~0~ + k(b / d)

y = y~0~ - k(a / d) 

로 구할 수 있음.



```python
def diophantine(a, b, c):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 % r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2

    return c // r1 * s1, c // r1 * t1

T = int(input())
for test_case in range(T):
    A, B, C = map(int, input().split())
    print("#{}".format(test_case + 1), *diophantine(A, B, C))
```

