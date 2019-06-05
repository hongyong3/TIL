# 20190605

## Machine Learning

### 선형대수(Linear Algebra) - 선형결합과 생성(Linear Combinations and span)



#### 선형결합(Linear Combination)

* vector v~1~, v~2~, ... in R^n^

* 선형결합이란 벡터들의 합의 결합을 의미

  > c~1~v~1~ + c~2~v~2~ + .... c~n~v~n~ 	|	c~1~ ~ c~n~ =>R(실수)

* vector a = (1, 2)	|	vector b = (0, 3)

* vector a와 vector b의 선형결합

  > 0 * vector a + 0 * vector b = (0, 0)	=> **영벡터 또한 선형결합**
  >
  > 3 * vector a - 2 * vector b = (3, 0)	=> **선형결합**
  >
  > `벡터끼리의 곱이 아니다.`

* 모든 벡터의집합은 무엇일까?

  > **R^2^위의 모든 점이 vector a와 vector b의 선형결합.**

* **Span(vector a, vector b) = R^2^** 

  > R^2^ 혹은 R^2^ 위의 모든 벡터와 같다.
  >
  > R^2^ 위의 모든 벡터를 vector a와 vector b의 선형결합으로 나타낼 수 있다는 뜻
  >
  > 영벡터는 자신의 선형결합으로 얻을 수 있는 유일한 벡터는 영벡터 자신

* 만약 vector v~1~, v~2~, ... v~n~으로 이루어진 집합의 생성이라고 하면 그 집합의 생성은 벡터들을 모으는데 어떤 벡터들을 모으냐면 c~1~v~1~ + c~2~v~2~ + .... c~n~v~n~으로 표현이 되는 그런 벡터들을 다 모음.

  * Span(v~1~, v~2~, ... v~n~) = {c~1~v~1~ + c~2~v~2~ + .... c~i~v~n~ | c~i~ => R for 1 <= n <= n}



---

### 선형대수(Linear Algebra) -  선형독립이란?(Introduction to Linear Independence)



* ##### {(2, 3), (4, 6)} => 위치벡터(Position Vector)

  > 이 두 벡터로 나타낼 수있는 모든 벡터는?
  >
  > **생성은 벡터의 선형결합으로 나타낼 수 있는 모든 벡터를 의미**
  >
  > 따라서 이것은 임의의 실수 c~1~과 c~2~에 대해서 c~1~ * (2, 3) + c~2~ * (4, 6)으로 나타낼 수 있는 모든 벡터의 집합
  >
  > c~1~ * (2, 3) + c~2~ * (4, 6) = c~1~ * (2, 3) + c~2~ * 2 * (2, 3) = (c~1~ + 2 * c~2~) * (2, 3)
  >
  > 임의의 상수와 다른 임의의 상수의 두 배 값을 더한 것.
  >
  > c~1~ * (2, 3) + c~2~ * (4, 6) = c~1~ * (2, 3) + c~2~ * 2 * (2, 3) = (c~1~ + 2 * c~2~) * (2, 3) = c~3~ * (2, 3)
  >
  > 두 벡터로 시작했지만 벡터들 사이의 임의의 선형결합으로 만들어질 수 있는 모든 벡터를 말함.
  >
  > 치환을 이용하여 첫 번째 벡터의 스칼라곱으로 간단히 나타낼 수 있음.

* ##### 벡터 집합의 생성

  > Span ({(2, 3), (4, 6)}) => 두 벡터가 동일선상에 있음. 
  >
  > 이 집합을 **선형 종속(Linear Independence)**이라고 함.
  >
  > R^2^의 두 벡터가 동일선상에 있을 때 직선 하나로 간단히 나타낼 수 있음.
  >
  > 이런 벡터는 이 두 벡터의 선형결합으로 나타낼 수 없음.

* v~1~ = (2, 3) | v~2~ = (7, 2) | v~3~ = (9, 5)

  > v~1~ + v~2~ = v~3~ 따라서 선형종속 집합
  >
  > Span (v~1~, v~2~) = R^2^

* v~1~ = (7, 0) | v~2~ = (0, -1) 

  > 두 벡터가 서로 선형결합이 안됨.
  >
  > 따라서 `선형독립`
  >
  > Span (v~1~, v~2~) = R^2^
  >
  > Span (v~1~, v~2~, v~3~) = R^2^
  >
  > 여기서 v~3~는 R^2^를 생성하는데 도움이 되지 않음. 그래서 v~3~를 `여분벡터`라고 함. 

* v~1~ = (2, 0, 0) | v~2~ = (0, 1, 0) | v~3~ = (0, 0, 7)

  > Span (v~1~, v~2~, v~3~) = R^3^



---

### 선형대수(Linear Algebra) -  선형독립 더 알아보기(More on Linear Independence)



* ##### s = {v~1~, v~2~, ... v~n~} 	=> 선형종속(Linear Dependent) 필요충분조건(if and only if; iff)으로서

  > c~1~v~1~ + c~2~v~2~ + .... c~n~v~n~ = 0(영벡터) 을 만족	=> for some c~i~'s not all are zero => at least 1 is non zero 

![1](https://user-images.githubusercontent.com/45934494/58939036-35051f00-87b1-11e9-8a89-d703bae02fd0.PNG)
![2](https://user-images.githubusercontent.com/45934494/58939038-359db580-87b1-11e9-85ad-7a859da04952.PNG)
![3](https://user-images.githubusercontent.com/45934494/58939039-359db580-87b1-11e9-9fe8-18bce739de63.PNG)