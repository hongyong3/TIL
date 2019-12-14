# 20191214

## Algorithm

### collections Module - defaultdict



#### 1) defaultdic란?

* `collections.defaultdict`는 딕셔너리(`dictionary`)와 거의 비슷하지만,

  *key*값이 없을 경우, 미리 지정해 놓은 초기(default)값을 반환하는 `dictionary`다.

* 기본 `dict` 와 `defaultdict`를 비교해보면, 

  기본 딕셔너리는 해당 키가 없는 값을 출력할 경우 `keyError Exception` 에러가 발생.

  반면에

  `defaultdict`는 `default_factory()`라는 함수가 초기값(default)를 *null*로 지정해줬기 때문에

  해당키가 없는 값을 출력할 경우 초기값인 *null*이 출력.

```python
import collections

# 기본 dict

test1 = {'a' : 1, 'b' : 2}
print(test1)
print(test1['c'])


'''
결과
{'a': 1, 'b': 2}
Traceback (most recent call last):
    print(test1['c'])
    
KeyError: 'c'

'''

# collections.defaultdict

# defaultdict의 초기값 생성
def default_factory():
    return 'null'

test2 = collections.defaultdict(default_factory, a = 1, b = 2)
print(test2)
print(test2['c'])

'''
결과
defaultdict(<function default_factory at 0x03510930>, {'a': 1, 'b': 2})
null
'''
```



#### 2) defaultdict의 인자(factor)

* `collections.defaultdict(default_factory, key = value)`는 

  `default_factory`와 key~1~ = value~1~, key~2~ = value~2~, ..., key~n~ = value~n~를 인자(factor)로 받는데, 

  `default_factory`는 `defaultdict`의 초기값을 지정하는 인자다.

  `default_factory`인자를 넣어주지 않으면 기본 딕셔너리와 마찬가지로 `KeyError Exception` 에러 발생.

```python
import collections

# default_factory를 지정하지 않은 경우

test3 = collections.defaultdict(a = 1, b = 2)
print(test3)
print(test3['c'])

'''
결과
defaultdict(None, {'a': 1, 'b': 2})
Traceback (most recent call last):
    print(test3['c'])
    
KeyError: 'c'
'''

# default_factory를 지정한 경우

def default_factory():
    return 'null'

test2 = collections.defaultdict(default_factory, a = 1, b = 2)
print(test2)
print(test2['c'])

'''
결과
defaultdict(<function default_factory at 0x03510930>, {'a': 1, 'b': 2})
null
'''
```



* `default_factory` 인자는  method 형태의 값을 인자로 받는데, 

  `list()`, `int()`, `set()`나 사용자가 직접 method를 생성할 수 있다.

```python
import collections

# list()

test_list = collections.defaultdict(list, a = [1, 2], b = [3, 4])
print(test_list)
print(test_list['c'])

'''
결과
defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3, 4]})
[]
'''

# set()

test_set = collections.defaultdict(set, a = {1, 2}, b = {3, 4})
print(test_set)
print(test_set['c'])

'''
결과
defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {3, 4}})
set()
'''

# int()

test_int = collections.defaultdict(int, a = 1, b = 2)
print(test_int)
print(test_int['c'])

'''
결과
defaultdict(<class 'int'>, {'a': 1, 'b': 2})
0
'''
```



#### 3) dict.setdefault VS defaultdict

* 기본 `dict`에서도 defaultdict의 `default_factory`와 같은 기능을 하는 method인 `setdefault`를 통해

  초기값을 지정할 수 있도록 제공한다.

  하지만,

  `defaultdict`의 `default_factory`가 더 간단하고, 빠르다.

```python
import collections

test_string = ['a', 'b', 'c', 'b', 'a', 'b', 'c']

# 기본 dict

test_dict = {}
for i in test_string:
    test_dict.setdefault(i, 0) # 기본 dict의 초기값 지정
    test_dict[i] += 1
print(list(test_dict.items()))

'''
결과
[('a', 2), ('b', 3), ('c', 2)]
'''

# defaultdict

test_defaultdict = collections.defaultdict(int)
for i in test_string:
    test_defaultdict[i] += 1
print(list(test_defaultdict.items()))

'''
결과
[('a', 2), ('b', 3), ('c', 2)]
'''

# 위의 예제들은 collections.Counter()를 이용해도 구할 수 있다.

test_Counter = collections.Counter(test_string)
print(list(test_Counter.items()))

'''
결과
[('a', 2), ('b', 3), ('c', 2)]
'''
```