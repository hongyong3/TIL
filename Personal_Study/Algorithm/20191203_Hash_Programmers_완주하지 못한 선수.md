# 20191203

## Algorithm - Hash - Programmers

### 완주하지 못한 선수



###### 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

##### 입출력 예

| participant                             | completion                       | return |
| --------------------------------------- | -------------------------------- | ------ |
| [leo, kiki, eden]                       | [eden, kiki]                     | leo    |
| [marina, josipa, nikola, vinko, filipa] | [josipa, filipa, marina, nikola] | vinko  |
| [mislav, stanko, mislav, ana]           | [stanko, ana, mislav]            | mislav |

##### 입출력 예 설명

예제 #1
leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.



#### 입력

```python
participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
print(solution(participant1, completion1))
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant2, completion2))
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]
print(solution(participant3, completion3))
```



#### 1번 시도

##### 정확성 : 통과

##### 효율성 : 시간 초과

```python
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer += participant[0]
    return answer
```



#### 2번 시도

##### 해결



##### 힌트

##### `Collections` Module의 Counter 사용

![1575374094523](C:\Users\yong_\AppData\Roaming\Typora\typora-user-images\1575374094523.png)

- `collections.Counter()`은 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체

  > A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
  >
  > 

- 리스트(List)

  > 요소 개수를 `collections.Counter()`을 이용하여 구할 수 있다.
  >
  > 결과값(return)은 dictionary 형태로 반환.



- 딕셔너리(Dict)

  > 요소의 갯수가 많은 것부터 출력해준다.
  >
  > 결과값(return)은 dictionary 형태로 반환.



- 문자열(string)

  > 문자열을 입력했을 경우 
  >
  > 결과값(return)은`{문자 : 개수}`의 dictionary 형태로 반환.





```python
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

