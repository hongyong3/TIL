# 20190216

## 클래스(Class)

### 10) 연습문제



**문제 6-1**

다음의 조건을 만족하는 Point라는 클래스를 작성하세요.

- Point 클래스는 생성자를 통해 (x, y) 좌표를 입력받는다.
- setx(x), sety(y) 메서드를 통해 x 좌표와 y 좌표를 따로 입력받을 수도 있다.
- get() 메서드를 호출하면 튜플로 구성된 (x, y) 좌표를 반환한다.
- move(dx, dy) 메서드는 현재 좌표를 dx, dy만큼 이동시킨다.
- 모든 메서드는 인스턴스 메서드다.



```python
>>> class Point:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def setx(self, x):
                self.x = x
        def sety(self, y):
                self.y = y
        def get(self):
                return (self.x, self.y)
        def move(self, dx, dy):
                self.x += dx
                self.y += dy
```



**문제 6-2**

문제 6-1에서 생성한 Point 클래스에 대한 인스턴스를 생성한 후 4개의 메서드를 사용하는 코드를 작성하세요.



```python
>>> a = Point(3,3)
>>> a.get()
(3, 3)
>>> a.setx(4)
>>> a.sety(2)
>>> a.get()
(4, 2)
>>> a.move(-4, -2)
>>> a.get()
(0, 0)
```



**문제 6-3**

아래 Stock 클래스에 대해 2개의 인스턴스를 생성했을 때 클래스와 a와 b 인스턴스의 네임스페이스를 그려보세요.

```python
>>> class Stock:
        market = "kospi"

>>> a = Stock()
>>> b = Stock()
```



![img](https://wikidocs.net/images/page/3466/6.16.png)

​							**그림 6.16 Stock 클래스와 인스턴스의 네임스페이스**



**문제 6-4**

문제 6-3의 코드에서 추가로 아래와 같은 코드를 수행했을 때 '???'로 표시된 부분의 결괏값을 적어보세요.

```python
>>> a.market
???
>>> b.market
???
>>> Stock.market
???
>>> a.market = "kosdaq"
>>> b.market = "nasdaq"
>>> a.market
???
>>> b.market
???
>>> Stock.market
???
```

```python
>>> a.market
'kospi'
>>> b.market
'kospi'
>>> Stock.market
'kospi'
>>> a.market = "kosdaq"
>>> b.market = "nasdaq"
>>> a.market
'kosdaq'
>>> b.market
'nasdaq'
>>> Stock.market
'kospi'
>>>
```





**문제 6-5**

문제 6-3, 6-4의 코드가 모두 수행된 후의 Stock 클래스, a 인스턴스와 b 인스턴스의 네임스페이스를 그려보세요.



![img](https://wikidocs.net/images/page/3466/s6.17.png)

​						**그림 6.17 Stock 클래스와 인스턴스의 네임스페이스(2)**

