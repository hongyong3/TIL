# 20200312

## Algorithm

### Boyer-Moore Algorithm(보이어-무어 알고리즘)



#### 보이어-무어 알고리즘(Boyer-Moore Algorithm)

##### 1) 보이어-무어 알고리즘이란?

* 찾고자하는 문자열 패턴(pattern)의 길이 m,  총 문자(text)의 길이 n일 때,

  오른쪽에서 왼쪽으로 문자를 비교, 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘.

  > 보통 상황에서 앞부분보다 끝부분에서 문자의 불일치가 일어날 확률이 높다는 성질을 이용한 것.

* text를 모두 보지 않아도 검색 가능.

* 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우,

  패턴의 길이만큼 Skip.

* 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재할 경우, 인덱스만큼 Skip.

* 시간복잡도는 **O(N) 이하**.

  > 최악의 경우 **O(MN)**



##### 2) 문자열 매칭 알고리즘 비교

* **고지식한 패턴검색 알고리즘(Brute Force)**

  > 텍스트의 모든 위치에서 패턴 비교하고 한칸씩 이동.
  >
  > **시간복잡도 O(MN)**.



* **KMP 알고리즘**

  > 불일치 발생한 앞부분에 대해 다시 비교하지 않고 매칭 수행.
  >
  > next배열을 생성해 불일치 발생하면 이동할 다음 위치 저장.
  >
  > 패턴의 왼쪽에서 오른쪽으로 비교.
  >
  > 시간복잡도 **O(M+N)** ==> **O(N)**.



* **카프-라빈 알고리즘**

  > 시간복잡도 **O(N)**.



* **보이어무어(Boyer-Moore Algorithm)**

  > 앞부분보다 끝부분가서 불일치 일어날 확률이 높다는 것 이용.
  >
  > skip 배열 생성해서 일치하는 칸으로 몇 칸 이동해야하는지 저장.
  >
  > 패턴의 오른쪽에서 왼쪽으로 비교.
  >
  > 상용화된 제품이나 서비스에 가장 많이 적용됨.
  >
  > 일반적으로 시간복잡도 **O(N)** 이하. 
  >
  > 최학일땐 O(MN).



##### 3) Python Code

```python
text = "a pattern matching algorithm"
pattern = "rithm"[:: - 1]

i = len(pattern) - 1
ans = 0

while not ans and i < len(text):
    if pattern[0] != text[i]:
        if text[i] in pattern:
            i += pattern.index(text[i])
        else:
            i += len(pattern)
    else:
        for x, y in zip(range(i, i - len(pattern), - 1), pattern):
            if text[x] == y:
                ans = 1
            else:
                ans, i = 0, x
                break

print(ans)
```

