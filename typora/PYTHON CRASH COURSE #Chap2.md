# PYTHON CRASH COURSE

## #20190114

### ##Chap2

```
>>> import this

The Zen of Python, by Tim Peters  파이썬 계명 by Tim Peters
Beautiful is better than ugly. 아름다움이 추함보다 좋다.
Explicit is better than implicit. 명시가 암시보다 좋다. 
Simple is better than complex. 단숨함이 복잡함보다 좋다.
Complex is better than complicated. 복합함이 난해한 것보다 좋다.
Flat is better than nested. 수평이 계층보다 좋다.
Sparse is better than dense. 여유로운 것이 밀집한것 보다 좋다.
Readability counts. 가독성은 중요하다.
Special cases aren't special enough to break the rules. 특별한 경우라는 것은 규칙을 어겨야 할 정도로 특별한 것이 아니다.
Although practicality beats purity. 허나 실용성은 순수성에 우선한다.
Errors should never pass silently. 오류 앞에서 절대 침묵하지 말지어다.
Unless explicitly silenced. 명시적으로 오류를 감추려는 의도가 아니라면.
In the face of ambiguity, refuse the temptation to guess. 모홈함을 앞에 두고, 이를 유추하겠다는 유혹을 버려라.
There should be one-- and preferably only one --obvious way to do it. 어떤 일에든 명확한 - 바람직하며 유일한 - 방법이 존재한다.
Although that way may not be obvious at first unless you're Dutch. 비록 그대가 우둔하여 그 방법이 처음에는 명확해 보이지 않을지라도.
Now is better than never. 지금 하는게 안하는 것보다 낫다.
Although never is often better than *right* now. 아예 안하는 것이 지금 *당장*보다 나을 때도 있지만.
If the implementation is hard to explain, it's a bad idea. 구현 결과를 설명하기 어렵다면, 그 아이디어는 나쁘다.
If the implementation is easy to explain, it may be a good idea. 구현 결과를 설명하기 쉽다면, 그 아이디어는 좋은 아이디어일 수 있다.
Namespaces are one honking great idea -- let's do more of those! 이네임스페이스는 대박 좋은 아이디어다. --마구 남용해라!
```





#### 변수

* 파이썬은 항상 변수의 현재 값만 기억한다.
* 변수 이름에는 글자와 숫자, 밑줄만 쓸 수 있다. 숫자로 변수이름을 시작할 수 없다.
* 변수 이름에는 공백을 쓸 수 없으므로 변수 이름에 단어를 두 개 이상 쓸 때는 밑줄로 분리



#### 에러

* 프로그램에 에러가 생기면 파이썬 인터프리터는 문제가 어디서 발생했는지 찾을 수 있도록 도와준다.

* 프로그램이 성공적으로 동작하지 않으면 인터프리터에서 트레이스백을 제공한다.
* *트레이스백* 은 인터프리터가 코드 실행 중에 어디서 문제가 생겼는지 기록한 보고서다.



#### 문자열

* 파이썬은 따옴표안에 들어 있는 것은 무엇이든 문자열로 인식한다.
* 큰따옴표든 작은따옴표든 쓸 수 있다.



#### 메서드(method)

* 메서드란 파이썬이 데이터 조각에 취하는 행동이다.



#### 문자열 함수

* title()은 각 단어의 첫 글자를 대문자로 표시
* upper()는 대문자
* lower()는 소문자



#### 문자열에 공백 추가하기

* 텍스트에 탭을 추가하려면 \(역슬래쉬) \t

* 행을 바꾸려면 \n

* 탭과 줄바꿈 문자를 결합해 쓸 수 있다. \n\t

  ```python
  print("Languages\n\tPython\n\tC\n\tJavaScript")
  Languages:
      Python
      C
      JavaScript
  ```



#### 공백 제거 함수

* strip() 양 옆 공백 제거

* lstrip()왼쪽 공백 제거

* rstrip()오른쪽 공백 제거

* 공백 제거 함수는 입력한 내용을 저장하기전에 가장 자주 사용.

* 문자열에서 공백을 제거하려면 문자열의 공백을 제거한 후 그 값을 원래 변수에 다시 저장해야 한다.

  ```python
  favorite_language = 'python '
  favorite_language = favorite_language.strip()
  favorite_language
  'python'
  ```



#### 문자열에서 문법 에러 피하기

* 문법 에러(Syntax Error)는 파이썬이 코드 일부를 유효한 파이썬 코드라고 인식하지 않을 때 발생.
* *문법 에러*는 인터프리터가 코드 일부를 유효한 파이썬 코드로 인식하지 않았을 때 발생
* 예를 들어 작은따옴표 사이에 apostrophe를 쓰면 에러가 일어남.
* 작은따옴표와 apostophe를 구분하지 못하기 때문.



#### 공백

* 공백은 파이썬이 코드를 해석할 때 아무 영향을 주지 않는다.
* 공백은 그저 우리가 코드를 해석할 때 중요한 부분을 더 빨리 찾아내려는 목적으로 사용.

#### 

#### 부동소수점 숫자

* 파이썬은 소수점이 있는 숫자를 모두 부동소수점 숫자(float)라고 부른다.

  ```python
  >>>0.1 + 0.1
  0.2
  
  -------------
  
  가끔은
  >>>0.2+0.1
  0.30000000000000000000004
  
  >>>3 * 0.1
  0.30000000000000000000004
  와 같은 숫자를 나타내는데 이는 파이썬이 2진법이라서 그렇다.
  ```

​	

#### str() 함수를 이용해 타입 에러 피하기

* 정수(int)값을 문자열(str)과 연결 할 수 없다.

  ```python
  age = 23
  message = "Happy" + age + "rd Birthday!"
  print(message)
  #TypeError: can't convert 'int' objecttostr implicitly
  
  message = "Happy" + str(age) + "rd Birthday!"
  print(message)
  Happy 23rd Birthday!
  ```

* str() 함수를 사용하면 문자열이 아닌 값을 문자열로 변환할 수 있다.



#### 파이썬3과 파이썬2의 차이

* 파이썬2에서는 정수를 정수로 나눈 결과는 정수다. 소수 부분을 버린 값
* 이런 동작을 예방하려면 *숫자 중 최소한 하나는 부동소수점 숫자*여야 한다.

```python
#파이썬3
>>>3 / 2
1.5

#파이썬2
>>>3 / 2
1

---> 예방법
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```



#### 주석(코멘트:Comment)

* 프로그램이 더 길고 복잡해지면

  프로그램 안에 해결하려는 문제에 대한 전반적 접근법을 설명하는 노트를 남겨야한다.

* 해시 기호(#)가 주석
* 파이썬 인터프리터는 해시 기호 다음에 있는 코드는 무시한다.