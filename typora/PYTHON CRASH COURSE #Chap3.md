# PYTHON CRASH COURSE

## #20190115

### ##Chap3



#### 리스트란?

* 리스트에는 정보를 저장할 수 있는데, 저장할 수 있는 정보량의 제한이 없다.
* 리스트(list)는 특정 순서가 있는 항목의 모음
* 리스트는 대괄호 [ ]로 표현하며, 리스트의 각 항목은 쉼표로 구분한다.



##### 리스트 항목에 접근하기

* 리스트는 순서가 있는 모음이다. 따라서 원하는 항목의 위치, 또는 인덱스(index)를 지정해서 접근할 수 있다.

* 항목에 접근하려면 리스트 이름을 쓰고 그다음 대괄호 안에 인덱스를 쓴다.

  ```python
  >>>bicycles = ['trek', 'cannodale', 'redline', 'specialized']
  >>>print(bicycles[0])
  trek
  >>>print(bicycles[0].title())
  Trek
  ```

* 파이썬은 리스트의 첫 번째 항목의 위치를 0에서 시작한다고 정의

* 컴퓨터의 메모리가 0번부터 시작하기 때문에 컴퓨터는 수를 0부터 센다.

* 리스트의 마지막 항목에 접근하는 문법 [-1]

  ```python
  >>>bicycles = ['trek', 'cannodale', 'redline', 'specialized']
  >>>print(bicycles[0])
  specialized
  ```

* 리스트의 각 값을 다른 변수와 마찬가지로 쓸 수 있다.

  ```python
  >>>bicycles = ['trek', 'cannodale', 'redline', 'specialized']
  >>>message = "My first bicycle was a" + bicycles[0].title() + "."
  print(message)
  My first bicycle was a Trek.
  ```



#### 리스트 항목 변경, 추가, 제거

* 리스트는 동적이다.
* 동적이라는 말은 리스트를 만든 뒤에 항목을 *추가*하거나 *제거*할 수 있다는 의미



##### 리스트 항목 수정하기

* 리스트 항목을 수정은 리스트 이름 다음에 바꾸려는 항목의 인덱스를 쓰고 새 값을 지정

  ```python
  >>>motorcycles = ['honda', 'yamaha', 'suzuki']
  >>>print(motorcycles)
  ['honda', 'yamaha', 'suzuki']
  >>>motorcycles[0] = 'ducati'
  ['ducati', 'yamaha', 'suzuki']
  ```



##### 리스트 항목 추가하기

* 리스트 이름.append('값')		---> 새 항목은 리스트 마지막에 추가

  ```python
  >>>motorcycles = ['honda', 'yamaha', 'suzuki']
  >>>print(motorcycles)
  ['honda', 'yamaha', 'suzuki']
  >>>motorcycles.append('ducati')
  >>>print(motorcycles)
  ['honda', 'yamaha', 'suzuki', 'ducati']
  ```

* 리스트 이름.insert(인덱스, 값)

  ```python
  >>>motorcycles = ['honda', 'yamaha', 'suzuki']
  >>>print(motorcycles)
  ['honda', 'yamaha', 'suzuki']
  >>>motorcycles.insert(0, 'ducati')
  >>>print(motorcycles)
  ['ducati', 'honda', 'yamaha', 'suzuki']
  ```
