# 20190604

## Machine Learning

### Data Structure - Collections



#### Collections

* List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)
* 편의성, 실행 효율 등을 사용자에게 제공함
* 아래의 모듈이 존재함

```python
from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
```



#### deque

* stack과 Queue를 지원하는 모듈
* List에 비해 효율적인 자료 저장 방식을 지원함

```python
from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
---
deque([0, 1, 2, 3, 4])

deque_list.appendleft(10)
print(deque_list)
---
deque([10, 0, 1, 2, 3, 4])
```



#### OrderedDict

* DIct와 달리, 데이터를 입력한 순서대로 dict를 반환함
* Dict type의 값을, value 또는 key 값으로 정렬할 때 사용 가능

##### General Style

```python
d = {}
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

```



##### OrderedDict

```python
from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)
---
x 100
y 200
z 300
l 500

# Dict type의 값을, value 또는 key 값으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
	print(k, v)
---
l 500
x 100
y 200
z 300

for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
	print(k, v)
---
x 100
y 200
z 300
l 500
```



#### defaultdict

* Dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법



##### General Style

```python
d = dict()
print(d["first"])
---
Traceback (most recent call last):
  File "test.py", line 206, in <module>
    print(d["first"])
KeyError: 'first'
    
# first라고 하는 키값이 존재하지 않아서 에러
```



##### defaultdict

```python
from collections import defaultdict

d = defaultdict(object)		# Default dictionary를 생성
d = defaultdict(lambda: 0)		# Default 값을 0으로 설정함

print(d["first"])
---
0
```



```python
from collections import OrderedDict
from collections import defaultdict

text = """A press release is the quickest and easiest way to get free publicity. """.lower().split()

word_count = {}
for word in text:
    if word in word_count.keys():
	    word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
---
{'a': 1, 'press': 1, 'release': 1, 'is': 1, 'the': 1, 'quickest': 1, 'and': 1, 'easiest': 1, 'way': 1, 'to': 1, 'get': 1, 'free': 1, 'publicity.': 1}

word_count = defaultdict(object)		# Default dictionary를 생성
word_count = defaultdict(lambda: 0)		# Default 값을 0으로 설정함

for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
	print(i, v)
---
a 1
press 1
release 1
is 1
the 1
quickest 1
and 1
easiest 1
way 1
to 1
get 1
free 1
publicity. 1
```



#### Count

* Sequence type의 data element들의 갯수를 dict 형태로 반환
* Dict type, keyword parameter 등도 모두 처리 가능

```python
from collections import Counter

c = Counter()				# a new, empty counter
c = Counter('gallahad')		# a new counter from aniterable
print(c)
---
Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
```



```python
from collections import Counter
c = Counter({'red':4, 'blue':2})	# a new counter from a mapping
print(c)
print(list(c.elements()))
---
Counter({'red': 4, 'blue': 2})
['red', 'red', 'red', 'red', 'blue', 'blue']

c = Counter(cats=4, dogs=8)			# a new counter fom keyword args
print(c)
print(list(c.elements()))
---
Counter({'dogs': 8, 'cats': 4})
['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']
```



#### namedtuple

* Tuple 형태로 Data 구조체를 저장하는 방법
* 저장되는 data의 variable을 사전에 지정해서 저장함

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y = 22)
print(p[0] + p[1])
---
33

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x = 11, y = 22))
---
11 22
33
Point(x=11, y=22)
```



---

### 선형대수(Linear Algebra) - 선형대수학을 위한 벡터란?

##### 선형대수학은 `벡터 공간`, `벡터`, `선형 변환`, `행렬`, `연립 선형 방정식`, 등을 연구하는 대수학의 한 분야이다. 현대 선형대수학은 그중에서도 벡터 공간이 주 연구 대상이다.



#### What is vector?

* Vector : magnitude & direction
* 벡터는 크기와 방향을 동시에 나타낸다.
* 벡터는 크기와 방향만 신경쓰면된다. 어디서 시작하든 어디에 표현하든 상관없다.

<img width="1126" alt="1" src="https://user-images.githubusercontent.com/45934494/58821696-996c9500-8670-11e9-8ab4-42008663aafa.PNG">



---

### 선형대수(Linear Algebra) - 실좌표공간(Real coordinate space)



#### R^2^ : 2차원 실수좌표공간

* ##### R^2^ : 2-Dimensional Real Coordinate space (2차원 실수좌표공간)

  > 단순좌표평면에서 다룸(시각적으로 표현하는 것은 실수좌표공간을 이해하는 하나의 방법)
  >
  > all possible real-value 2-tuple

* ##### R^2^에서

  > `2`는 다루는 차원을 의미
  >
  > `R`은 실수좌표공간을 의미

* 2차원 실수좌표공간은 실수값을 가진 모든 `2-튜플(2-tuple)`을 말한다.

  > 튜플은 순서가 정해져 있는 숫자들의 리스트
  >
  > 2-튜플은 숫자 2개의 순서리스트이자 실수 2개의 순서리스트이다.

* ##### R^2^을 다룬다는 것은 모든 가능한 실수값을 가지는 2-튜플을 다루는 것

* 크기는 없고 방향은 정해지지 않은 `영벡터`를 포함한 모든 2-튜플에 대해서

  이 벡터들을 조합하여 2차원 실수좌표공간도 만들어낼 수 있다.

  

#### R^3^ : 3차원 실수좌표공간

* ##### R^3^ : 3-Dimentional Real Coordinate Space(3차원 실수좌표공간)

* 3차원 실수좌표공간은 실수값을 가진 모든 `3-튜플(3-tuple)`을 말한다.

* ##### R^3^에 속하지 않은 것들

  > R^2^에 속하는 벡터
  >
  > 허수성분을 가진 벡터



<img width="1200" alt="1" src="https://user-images.githubusercontent.com/45934494/58823684-3fba9980-8675-11e9-88ee-9eaddf453ad2.PNG">



---

### 선형대수(Linear Algebra) - 대수와 그래프를 이용한 벡터의 덧셈(Adding vectors)



#### 벡터의 합

* **Vector a = (6, -2)**	|	**Vector b = (-4, 4)**	=> Vector a와 Vector b는 R^2^
* Vector a + Vector b = (2, 2)
* Vector b + Vector a = (2, 2)
* 더하는 순서가 바뀌어도 결과는 동일
* 벡터를 꼭 원점에서 그릴 필요는 없다. 중요한 것은 벡터의 방향과 크기

![1](https://user-images.githubusercontent.com/45934494/58852617-33b0f500-86d2-11e9-9633-284a2de01a55.PNG)



---

### 선형대수(Linear Algebra) - 벡터와 스칼라의 곱셈(Multiplying a vector by a Scalar)



#### 벡터와 스칼라의 곱

* **Vector a = (2, 1)**

* 스칼라를 곱한 벡터는 여전히 2차원 벡터

* 3 * Vector a = 3 * (2, 1) = (3 * 2, 3 * 1) = (6, 3)

  > **양수의 스칼라**값을 곱하면 **방향은 동일**하고, 크기는 **스칼라** 값에 비례

* -1 * Vector a = (-2, -1)

  > **음수의 스칼라**값을 곱하면 **방향은 반대**하고, 크기는 **스칼라** 값에 비례

![1](https://user-images.githubusercontent.com/45934494/58853240-770c6300-86d4-11e9-8ab4-51e464b7fe63.PNG)



---

### 선형대수(Linear Algebra) - 단위벡터(Unit Vector notation)



#### 단위벡터

* ##### Vector i = (1, 0) 	|	`수평방향 단위벡터`

* ##### Vector j = (0, 1) 	|	`수직방향 단위벡터`

* Vector v = (2, 3) 

  > **단위벡터를 이용**하여 vector v를 나타내면= 2 * vector i + 3 * vector j ===> 2 * i + 3 * j
  >
  > **2i + 3j**와 같이 표현한 것을 **단위벡터 표기법**
  >
  > **(2, 3)**와 같이 표현한 것을 **열벡터 표기법**



---

### 선형대수(Linear Algebra) - 직선의 매개변수 표현(Parametric representations of lines)



#### 벡터를 직선의 매개변수로 표현

##### R^2^에서

* ##### vector a = (2, 1)	|	vector b = (0, -3)

* ##### 집합 l = {vector b + t(vector b - vector a) | t = 모든 실수}

  > x = - 2t
  >
  > y = 2t + 1



##### R^3^에서

* ##### vector p~1~ = (-1,2, 7)	|	vector p~2~ = (0, 3, 4)

* ##### 집합 l = { vector p~1~ + t(vector p~1~ - vector p~2~) | t = 모든 실수}

  > x = - t - 1
  >
  > y = - t + 2
  >
  > z = 3t + 7
  >
  > x + y + z = k	=> 면(plane) not a line