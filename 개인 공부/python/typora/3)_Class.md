# 20190205

## 클래스(Calss)

### 4) 클래스에 메서드 추가하기



앞서 정의한 BusinessCard 클래스는 클래스 내부에 변수나 함수가 없었습니다. 그래서 인스턴스를 만들었음에도 해당 인스턴스로 할 수 있는 일이 별로 없었습니다. 이번에는 BusinessCard 클래스에 사용자로부터 데이터를 입력받고 이를 저장하는 기능을 수행하는 함수를 추가해보겠습니다. 참고로 클래스 내부에 정의돼 있는 함수를 특별히 메서드(method)라고 합니다.

다음 코드는 BusinessCard 클래스에 set_info라는 메서드를 추가한 것입니다. 메서드를 정의할 때도 함수를 정의할 때와 마찬가지로 def 키워드를 사용합니다. set_info 메서드는 네 개의 인자를 받는데, 그중 name, email, addr은 사용자로부터 입력받은 데이터를 메서드로 전달할 때 사용하는 인자입니다. 



그렇다면 메서드의 첫 번째 인자인 self는 무엇일까요?



```python
>>> class BusinessCard:
        def set_info(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
```



파이썬 클래스에서 self의 의미를 정확히 이해하는 것이 중요하지만 아직 제대로 설명하기는 조금 이른 감이 있습니다. 일단 클래스 내부에 정의된 함수인 메서드의 첫 번째 인자는 반드시 self여야 한다고 외우길 바랍니다.

위 코드에서 메서드 내부를 살펴보면 메서드 인자로 전달된 name, email, addr 값을 self.name, self. email, self.addr이라는 변수에 대입하는 것을 볼 수 있습니다. 앞서 여러 번 설명한 것처럼 파이썬에서 대입은 바인딩을 의미합니다. 따라서 set_info 메서드의 동작은 그림 6.5와 같이 메서드 인자인 name, email, addr이라는 변수가 가리키고 있던 값을 self.name, self.email, self.addr이 바인딩하는 것입니다.



![img](https://wikidocs.net/images/page/3456/6.05.png)

​								**그림 6.5 변수의 바인딩**



BusinessCard 클래스를 새롭게 정의했으므로 새롭게 정의된 클래스로 인스턴스를 생성해 봅시다. 붕어빵에 비유해 보면 붕어빵을 굽는 틀을 새롭게 바꿨으므로 새로 붕어빵을 구워보는 것입니다.



```python
>>> member1 = BusinessCard()
>>> member1
<__main__.BusinessCard object at 0x030248F0>
```



새롭게 정의된 BusinessCard 클래스는 set_info라는 메서드를 포함하고 있습니다. 따라서 member1 인스턴스는 set_info 메서드를 호출할 수 있습니다.

그림 6.6을 보면 member1이라는 클래스 인스턴스를 통해 set_info라는 메서드를 호출할 수 있음을 확인할 수 있습니다. 단, 메서드에 인자를 전달하기 위해 파이썬 IDLE에서 괄호를 입력하면 메서드의 인자가 네 개가 아니라 세 개로 표시됩니다. 앞서 set_info 메서드를 정의할 때는 self, name, email, addr의 네 개의 인자가 사용됐는데 메서드를 호출할 때는 왜 세 개만 사용될까요?



![img](https://wikidocs.net/images/page/3456/6.06.png)

​								**그림 6.6 클래스 인스턴스를 통한 메서드 호출**



일단 다음 코드처럼 파이썬 IDLE가 알려주는 대로 세 개의 인자만 set_info 메서드의 입력으로 전달합니다. 항상 그렇듯이 파이썬 IDLE에서 에러가 발생하지 않았다면 정상적으로 코드가 실행된 것을 의미합니다.



```python
>>> member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")
```



set_info 메서드는 메서드 인자로 전달된 값을 self.name, self.email, sellf.addr로 바인딩했습니다. 그런데 현재 사용 가능한 변수는 클래스 인스턴스인 member1뿐입니다. 어떻게 하면 member1을 통해 self.name, self.email, self.addr에 접근할 수 있을까요?

self.name, self.email, self.addr과 같이 ‘self.변수명’과 같은 형태를 띠는 변수를 인스턴스 변수라고 합니다. 인스턴스 변수는 클래스 인스턴스 내부의 변수를 의미합니다. 위 코드에서 member1이라는 인스턴스를 생성한 후 set_info 메서드를 호출하면 메서드의 인자로 전달된 값을 인스턴스 내부 변수인 self.name, self.email, self.addr이 바인딩하는 것입니다. 클래스를 정의하는 순간에는 여러분이 생성할 인스턴스의 이름이 member1인지 모르기 때문에 self라는 단어를 대신 사용하는 것입니다.

정리해보면 set_info 메서드 내에서 self.name이라는 표현은 나중에 생성될 클래스 인스턴스 내의 name 변수를 의미합니다. 따라서 다음과 같이 인스턴스 이름을 적고 ‘.’를 붙인 후 인스턴스 변수의 이름을 지정하는 식으로 특정 인스턴스 변수에 접근할 수 있습니다.



```python
>>> member1.name
'Yuna Kim'
>>> member1.email
'yunakim@naver.com'
>>> member1.addr
'Seoul'
```



클래스는 한번 정의해두면 해당 클래스를 이용해 여러 클래스 인스턴스를 만들 수 있습니다. 아직도 개념이 잘 이해되지 않는다면 항상 붕어빵 틀을 생각하세요. 붕어빵 틀을 한 번 만들어두면 붕어빵을 계속해서 구울 수 있는 것과 비슷합니다.

이번에는 두 번째 회원에 대한 정보를 저장하는 인스턴스를 만들어보겠습니다. 다음 코드를 보면 먼저 member2라는 인스턴스를 생성한 후 set_info 메서드를 호출해 인스턴스에 값을 저장하는 것을 확인할 수 있습니다.



```python
>>> member2 = BusinessCard()
>>> member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
```



새로 생성한 인스턴스 역시 member2라는 이름을 통해 해당 인스턴스 내의 변수에 접근할 수 있습니다.



```python
>>> member2.name
'Sarang Lee'
>>> member2.email
'sarang.lee@naver.com'
>>> member2.addr
'Kyunggi'
>>>
```



그림 6.7은 클래스 인스턴스인 member1과 member2를 그림으로 표현해 본 것입니다. member1과 member2는 서로 동일한 이름의 인스턴스 변수인 name, email, addr을 갖고 있지만 각각 다른 데이터를 바인딩하고 있습니다.



![img](https://wikidocs.net/images/page/3456/6.07.png)



​								**그림 6.7 클래스 인스턴스 상태**



이번에는 BusinessCard 클래스에 명함을 출력하는 메서드를 추가해보겠습니다. 다음과 같이 print_info 메서드를 추가해 BusinessCard 클래스를 새롭게 정의합니다. 새로 추가된 print_info 메서드를 살펴보면 self라는 인자 값만을 사용합니다. 앞서 간단히 설명한 것처럼 파이썬 클래스의 메서드는 항상 self라는 기본 인자를 하나 갖고 있어야 하므로 self를 제외하면 print_info 메서드는 사실 인자 가 없는 함수나 마찬가지입니다.



```python
>>> class BusinessCard:
        def set_info(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
        def print_info(self):
                print("--------------------")
                print("Name: ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")
```



print_info 메서드의 내부를 살펴보면 print 함수를 통해 self.name, self.email, self.addr 값을 출력하는 것을 확인할 수 있습니다. 앞서 set_info 메서드에서 이름을 저장할 때 self.name에 저장했으므로 print_info 메서드에서도 self.name을 통해 바로 데이터에 접근하면 됩니다.

BusinessCard 클래스를 재정의했으므로 다음과 같이 새로 인스턴스를 생성해 봅시다.



```python
>>> member1 = BusinessCard()
>>> member1.set_info("YunaKim", "yuna.kim@naver.com", "Seoul")
```



member1이라는 인스턴스에 값이 제대로 저장됐는지 확인하기 위해 member1.name과 같이 인스턴스 변수에 바로 접근할 수도 있습니다. 하지만 BusinessCard 클래스에 print_info 메서드를 정의해뒀기 때문에 다음과 같이 해당 메서드를 호출해 값을 화면에 출력해 볼 수 있습니다.



```python
>>> member1.print_info()
--------------------
Name:  YunaKim
E-mail:  yuna.kim@naver.com
Address:  Seoul
--------------------
```



### 5) 클래스 생성자

6.1절에서 파이썬의 클래스에 대해 배웠습니다. 지금까지 배운 내용을 정리해보면 다음과 같습니다.

- 파이썬의 클래스를 이용하면 프로그래머가 원하는 새로운 타입을 만들 수 있다.
- 생성된 타입은 데이터와 데이터를 처리하는 메서드(함수)로 구성돼 있다.

그럼 지난 시간에 만든 클래스를 다시 한 번 살펴볼까요?



```python
>>> class BusinessCard:
        def set_info(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
        def print_info(self):
                print("--------------------")
                print("Name: ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")
```



파이썬의 class 키워드를 통해 BusinessCard라는 새로운 타입을 만들었으니 인스턴스를 생성해야겠죠? 다시 한번 말씀드리면 클래스 인스턴스를 생성하려면 ‘클래스 이름()’과 같이 적으면 됩니다. 그리고 생성된 인스턴스에 점(.)을 찍어서 인스턴스 변수나 메서드에 접근할 수 있었습니다.



```python
>>> member1 = BusinessCard()
>>> member1.set_info("kim", "kim@gmail.com", "USA")
>>>
```



위 코드를 살펴보면 먼저 인스턴스를 생성하고 생성된 인스턴스에 데이터를 입력하는 순으로 코드가 구성돼 있습니다. 붕어빵에 비유해 보면 붕어빵 틀(클래스)을 이용해 팥소를 넣지 않은 상태로 붕어빵을 구운 후(인스턴스생성) 나중에 다시 붕어빵 안으로 팥소를 넣는 것과 비슷합니다. 어떻게 하면 클래스 인스턴스 생성과 초깃값 입력을 한 번에 처리할 수 있을까요?

파이썬 클래스에는 인스턴스 생성과 동시에 자동으로 호출되는 메서드인 생성자가 존재합니다. 참고로 생성자는 C++나 자바 같은 객체지향 프로그래밍 언어에도 있는 개념입니다. 파이썬에서는 `__init__ (self)`와 같은 이름의 메서드를 생성자라고 하며, 파이썬 클래스에서`__`로 시작하는 함수는 모두 특별한 메서드를 의미합니다.

다음은 생성자인 `__init__(self)` 메서드를 가진 MyClass 클래스를 정의한 것입니다. 앞서 설명한 것처럼 생성자의 첫 번째 인자도 항상 self여야 합니다. 생성자 내부에는 print 문을 통해 간단한 메시지를 출력했습니다.



```python
>>> class MyClass:
        def __init__(self):
                print("객체가 생성되었습니다.")
```



MyClass라는 클래스를 정의했으니 이제 이 클래스의 인스턴스를 생성해보겠습니다. 다음 코드를 보면 인스턴스를 생성하자마자 화면에 메시지가 출력되는 것을 확인할 수 있습니다. 이는 인스턴스가 생성되는 시점에 자동으로 생성자인 `__init__(self)` 메서드가 호출됐기 때문입니다. 참고로 init이라는 영어 단어는 ‘초기화하다’라는 뜻이 있는 initialize의 약어입니다.



```python
>>> inst1 = MyClass()
객체가 생성되었습니다.
```



클래스 생성자를 이해했다면 BusinessCard 클래스를 수정해 인스턴스의 생성과 동시에 명함에 필요한 정보를 입력받도록 클래스를 새롭게 정의해 봅시다. 눈치가 빠르신 분들은 벌써 정답을 맞혔지요? 기존에 구현했던 BusinessCard 클래스의 set_info 메서드가 데이터를 입력받는 역할을 수행했으므로 set_info 메서드를 `__init__` 메서드로 이름만 변경하면 됩니다.



```python
>>> class BusinessCard:
        def __init__(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
        def print_info(self):
                print("--------------------")
                print("Name: ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")
```



새로 정의된 BusinessCard 클래스의 생성자는 인자가 4개임을 확인할 수 있습니다. 물론 첫 번째 인자인 self는 생성되는 인스턴스를 의미하고 자동으로 값이 전달되므로 인스턴스를 생성할 때 명시적으로 인자를 전달해야 하는 것은 3개입니다. 따라서 인스턴스를 생성할 때 3개의 인자를 전달하지 않으면 오류가 발생합니다. 생성자 호출 단계에서 오류가 발생하면 인스턴스도 정상적으로 생성되지 않게 됩니다.



```python
>>> member1 = BusinessCard()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    member1 = BusinessCard()
TypeError: __init__() missing 3 required positional arguments: 'name', 'email', and 'addr'
```



새로 정의된 BusinessCard 클래스는 생성자에서 3개의 인자(name, email, addr)를 받기 때문에 다음과 같이 인스턴스를 생성할 때 3개의 인자를 전달해야 정상적으로 인스턴스가 생성됩니다. member1이라는 인스턴스가 생성된 후에는 인스턴스 메서드를 호출해 인스턴스 변수의 값을 화면에 출력할 수 있습니다. 어떤가요? 클래스의 생성자를 사용하니 인스턴스의 생성과 초깃값 저장을 한 번에 할 수 있어 편리하지요?



```python
>>> member1 = BusinessCard("Kangsan Lee", "kangsan.lee", "USA")
>>> member1.print_info()
--------------------
Name:  Kangsan Lee
E-mail:  kangsan.lee
Address:  USA
--------------------
```