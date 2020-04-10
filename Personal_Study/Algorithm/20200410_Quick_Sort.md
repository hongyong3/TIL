# 20200410

## Algorithm

### 퀵 정렬(Quick Sort)



#### 1) 퀵 정렬(Quick sort)이란?

* 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬.

* 분할 정복(Devide and Conquer)기법과 재귀 알고리즘을 이용한 정렬 알고리즘.

  항상 정 가운데를 기준으로 분할을 하는 병합 정렬과 달리,

  퀵 정렬은 피봇(pivot)이라 불리는 임의의 기준값을 사용.



#### 2) 시간 복잡도

* 퀵 정렬의 성능은 `pivot`값을 어떻게 선택하는냐에 크게 달라짐.

* 이상적인 경우의 시간 복잡도는 시간복잡도 **O(Nlog~N~)**,

  pivot 값을 기준으로 pivot보다 작은 값과 pivot보다 큰 값의 개수가 동일할 때임.

* 최악의 경우 시간 복잡도**O(N^2^)**,

  pivot 값을 기준으로 값이 한쪽으로 치우쳤을 경우임.

* 입력 배열이 차지하는 메모리만을 사용하는 **제자리 정렬(In-Place Sorting)**으로 구현할 경우, 

  **O(1)**의 공간 복잡도를 가진 코드의 구현이 가능.



#### 3) 방법

```python
data = [6, 5, 1, 4, 7, 2, 3]
pivot = 4

# 예를 들어 4를 pivot으로 설정하면,
# pivot 보다 작은 값을 왼쪽
# pivot 보다 큰 값을 오른쪽으로 위치
# 이런 방식으로 분할을 해놓으면 왼쪽에 있는 값들과 오른쪽에 있는 값들 간에는 비교를 할 필요가 없음.


			p
[3, 2, 1] < 4 < [7, 5, 6]

	  p
[1] < 2 < [3]

	 p
[] < 5 < [7, 6]

	  p
[6] < 7 < []

# 마지막으로 좌우로 분할했던 값들을 모두 합치면,
sortedData = [1, 2, 3, 4, 5, 6, 7]
```



#### 4) 코드

* 매번 재귀 호출될 때마다 새로운 리스트를 생성하여 리턴하기 때문에 메모리 사용 측면에서 비효율적.

```python
def quickSort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    less = []	# pivot보다 작은 경우.
    more = []	# pivot보다 큰 경우.
    equal = []	# pivot과 동일한 경우.
    
    for i in data:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
	return quickSort(less) + equal + quickSort(more)
```



#### 5) 최적화

* 제자리 정렬(In-Place Sorting)을 적용.

```python
def quickSOrt(data):
    def sort(low, high):
        if low >= high:
            return
        
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    	
    def partition(low, high):
        pivot = data[(low + high) // 2]
        
        while low <= high:
            while data[low] < pivot:
                low += 1
            while data[high] > pivot:
                high -= 1
            
            if low <= high:
                data[low], data[high] = data[high], data[low]
                low, high = low + 1, high - 1
        
        return low
    
    return sort(0, len(data) - 1)
```

