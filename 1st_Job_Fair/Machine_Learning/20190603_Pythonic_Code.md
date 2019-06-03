# 20190603

## Machine Learning

### Pythonic Code



#### Pythonic Code Overview

* 파이썬 스타일의 코딩 기법
* **파이썬 특유의 문법**을 활용하여 효율적으로 코드를 표현함
* 고급 코드를 작성 할 수록 더 많이 필요해짐



##### General Style

```python
colors = ["red", "blue", "green", "yellow"]
result = ""

for s in colors:
    result += s
print(result)

----
redbluegreenyellow
```



##### pythonic Code

```python
colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)
print(result)

---
redbluegreenyellow
```



#### Pythonic Code

* Split & Join
* List Comprehension
* Enumerate & Zip



#### Why Pythonic Code?

* **남 코드에 대한 이해도**
  * 많은 개발자들이 python 스타일로 코딩한다.
* **효율**
  * 단순 for, loop, append 보다 list가 조금 더 빠르다.
  * 익숙해지면 코드도 짧아진다.
* **간지**
  * 쓰면 왠지 코드 잘 짜는 거처럼 보인다.



---

### Pythonic Code - Split & Join



#### Split 함수

* String Type의 값을 나눠서 List 형태로 변환

```python
items = 'zero one two three'.split()	# 빈칸을 기준으로 문자열 나누기
print(items)
---
['zero', 'one', 'two', 'three']

example = 'python, jquery, javascript'	# ","을 기준으로 무나열 나누기
example.split(",")
---
['python', 'jquery', 'javascript']

a, b, c = example.split(",")
# 리스트에 있는 각 값을 a, b, c 변수로 unpacking

example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split('.')
# ","을 기준으로 문자열 나누기 -> Unpacking
```



#### Join 함수

* String List를 합쳐 하나의 String으로 반환할 때 사용

```python
colors = ['red', 'blue', 'green', 'yellow']

result = ''.join(colors)	
print(result)
'redbluegreenyellow'

result = ' '.join(colors)	# 연결 시 빈칸 1칸으로 연결
print(result)
'red blue green yellow'

result = ', '.join(colors)	# 연결 시 ", "으로 연결
print(result)
'red, blue, green, yellow'

result = '-'.join(colors)	# 연결 시 "-"으로 연결
print(result)
'red-blue-green-yellow'
```



---

### Pythonic Code - List comprehensions

* 기존 List 사용하여 간단히 다른 List를 만드는 기법
* 포괄적인 List, 포함되는 리스트라는 의미로 사용됨
* 파이썬에서 가장 많이 사용되는 기법 중 하나
* 일반적으로 for + append 보다 속도가 빠름



#### List comprehension (1/4)

##### General Style

```python
result = []
for i in range(10):
    result.append(i)
print(result)
---
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



##### List comprehension

```python
reslut = [i for i in range(10)]
print(result)
---
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in range(10) if i % 2 == 0]
print(result)
---
[0, 2, 4, 6, 8]
```



#### List comprehension (2/4)

```python
word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
print(result)
---
['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo', 'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol', 'od']
```



#### List comprehension (3/4)

```python
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i + j for i in case_1 for j in case_2]
print(result)
---
['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

result = [[i + j for i in case_1] for j in case_2]
print(result)
---
[['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']]

result = [i + j for i in case_1 for j in case_2 if not(i==j)]
# Filter : i랑 j가 같다면 List에 추가하지 않음
print(result)
---

['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']
result.sort()
print(result)
---
['AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']
```



##### List comprehension (4/4)

```python
words = 'The quick brown fox jumps over lazy dog'.split()
# 문장을 빈칸 기준으로 나눠 List로 변환
print(words)
---
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# List의 각 element들을 대문자, 소문자, 길이로 변환하여 two dimensional List로 변환
for i in stuff:
    print(i)
---
['THE', 'the', 3]
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['FOX', 'fox', 3]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['LAZY', 'lazy', 4]
['DOG', 'dog', 3]
```



---

### Pythonic Code : Enumerate & Zip



#### Enumerate

* List의 element를 추출할 때 번호를 붙여서 추출

```python
for i, v in enumerate(['tic', 'tac', 'toe']):
# List에 있는 index와 값을 unpacking
	print(i, v)
---
0 tic
1 tac
2 toe

mylist = ["a", "b", "c", "d"]
list (enumerate(mylist))	# list에 있는 index와 값을 unpacking하여 list로 저장
---
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

{i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())}
# 문장을 List로 만들고 List의 index와 값을 unpacking하여 dict로 저장
---
{0: 'Gachon', 1: 'University', 2: 'is', 3: 'an', 4: 'academic', 5: 'institute', 6: 'located', 7: 'in', 8: 'South', 9: 'Korea.'}
```



#### Zip

* 두 개의 List의 값을 병렬적으로 추출함

```python
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):	# 병렬적으로 값을 추출
    print(a, b)
---
a1 b1
a2 b2
a3 b3

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))	# 각 tuple의 같은 index끼리 묶음
---
(1, 10, 100) (2, 20, 200) (3, 30, 300)

[sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
# 각 tuple의 같은 index를 묶어 합을 list로 변환
[111, 222, 333]
```



#### Enumerate & Zip

```python
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate (zip(alist, blist)):
    print(i, a, b)	# index alist [index] blist [index] 표시
---
0 a1 b1
1 a2 b2
2 a3 b3
```



---

### Pythonic Code - Lambda & MapReduce



#### Lambda

* 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
* 수학의 람다 대수에서 유래함
* Python 3부터는 권장하지는 않으나 여전히 많이 쓰임



##### General function

```python
def f(x, y):
    return x + y

print(f(1, 4))
```



##### Lambda function

```python
f = lambda x, y ; x + y
print(f(1, 4))

f = lambda x: x ** 2
print(f(3))

f = lambda x: x / 2
print(f(3))

print((lambda x: x + 1)(5))
```



#### Map function

* Sequence 자료형 각 element에 동일한 function을 적용함

```python
ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))

f = lambda x, y : x + y
print(list(map(f, ex, ey)))

x = [value ** for value in ex]
```



#### Reduce function

* map function과 달리 list에 똑같은 함수를 적용해서 통합

```python
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
print(factorial(5))
```



#### Summary

* Lambda, map, reduce는 간단한 코드로 다양한 기능을 제공
* 그러나 코드의 직관성이 떨어져서 lambda나 reduce는 **python3에서 사용을 권장하지 않음**
* Legacy library나 다양한 **머신러닝 코드에서 여전히 사용중**



---

### Pythonic Code - Asterisk



#### Asterisk

* 흔히 알고 있는 * 를 의미함
* 단순 곱셈, 제곱연산, 가변 인자 활용 등 다양하게 사용됨



##### *args

```python
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))
    
asterisk_test(1, 2, 3, 4, 5, 6)
---
1 (2, 3, 4, 5, 6)
<class 'tuple'>
```



##### **kargs

```python
def asterisk_test(a, **kargs):	# **kargs는 키워드인자
    print(a, kargs)
    print(type(kargs))
    
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
---
1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
<class 'dict'>
```



#### Asterisk - unpacking a container

* tuple, dict 등 자료형에 들어가 있는 값을 unpacking
* 함수의 입력값, zip 등에 유용하게 사용가능

```python
def asterisk_test(a, *args):
    print(a, args[0])	# (2, 3, 4, 5, 6)는 한개의 변수이므로 args[0]를 하면 (2, 3, 4, 5, 6)
    print(type(args))

asterisk_test(1, *(2, 3, 4, 5, 6))
---
1 (2, 3, 4, 5, 6)
<class 'tuple'>

def asterisk_test(a, *args):
    print(a, args[0][0])
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))
---
1 2
<class 'tuple'>
```



```python
def asterisk_test(a, *args):
    print(a, *args)
    print(type(args))
    
asterisk_test(1, (2, 3, 4, 5, 6))
---
1 (2, 3, 4, 5, 6)
<class 'tuple'>
```



```python
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))
```



#### Asterisk - unpacking a container

```python
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
---
[1, 2] [3, 4] [5, 6]

data = ([1, 2], [3, 4], [5, 6])
print(*data)
---
[1, 2] [3, 4] [5, 6]
```



```python
def asterisk_test(a, b, c, d,):
    print(a, b, c, d)
    
data = {"b":1, "c":2, "d":3}
asterisk_test(10, **data)
---
10 1 2 3
```



```python
for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)
    print(sum(data))
---
(1, 3, 5)
9
(2, 4, 6)
12
```



```python
def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)
    
data = {"d":1, "c":2, "b":3, "e":56}
asterisk_test(10, **data)
---
10 3 2 1 56
```









