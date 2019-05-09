vue 10/js 15

##### #5) computed vs watch: cashing을 하는가 아닌가

```javascript
-computed : cashing 함/ 저장해서 변수처럼 쓰는것/ 연산작업을 덜함

watch: 지켜보는 것,  데이터 변화를 보는 것, 변할때마다 특정한 함수를 실행시키는 것, data 값이 변경될때마다 실행시키는 함수/ 비동기 할때 많이 쓰임// 호출할때마다 계산을 함


```

directive -- 다음 빈칸에 맞는 디렉티브가 무엇인가? 주관식 --- 축약 v-bind: - 생략 // v-on: @

##### #1) typeof-- 객관식 1

```javascript
1+ '1' = 11
1 * '1' = 1
typeof NaN => number 
NaN === NaN =>FALSE
typeof undefined => undefined
typeof null => object
typeof function(){} =>function
typeof (() => {}) =>function
typeof true => boolean
typeof 'a' => string
typeof [] => object
typeof {} => object
```

##### #2) 자바스크립트는 싱글쓰레드

```javascript
javascript: promise 객체

#### axios: promise 객체를 반환하고

- 파이썬이랑 다르게 동작하기 때문에 사용
- non-blocking 프린트하는 순서가 원하는대로 동작하지 않는다, then 안에 끝났을 때 하는 로직을 넣으면 

arrow function vs function : 차이: this

#2) js - 싱글스레드임에도 불구하고 multi로 보이는거는 non-blocking 때문

#### 자바스크립트는 싱글쓰레드
```



##### #3) 뚱이 일치

```javascript
===  일치 -- type까지

== 
```

##### #4) EVENTLISTENER -- 객관식 1

```javascript
click – 마우스버튼을 클릭하고 버튼에서 손가락을 떼면 발생한다. 
mouseover – 마우스를 HTML요소 위에 올리면 발생한다. 
mouseout – 마우스가 HTML요소 밖으로 벗어날 때 발생한다. 
mousemove – 마우스가 움직일때마다 발생한다. 마우스커서의 현재 위치를 계속 기록하는 것에 사용할 수 있다. 
keypress – 키를 누르는 순간에 발생하고 키를 누르고 있는 동안 계속해서 발생한다. 
keydown – 키를 누를 때 발생한다. 
keyup – 키를 누르다가 떼는 순간에 발생한다. 
load – 웹페이지에서 사용할 모든 파일의 다운로드가 완료되었을때 발생한다. 
scroll – 스크롤바를 드래그하거나 키보드(up, down)를 사용하거나 마우스 휠을 사용해서 웹페이지를 스크롤 할 때 발생한다. 페이지에 스크롤바가 없다면 이벤트는 발생하지 않다. 
change – 폼 필드의 상태가 변경되었을 때 발생한다. 라디오 버튼을 클릭하거나 셀렉트 박스에서 값을 선택하는 경우를 예로 들수 있다. 
input - input 또는 textarea 요소의 값이 변경되었을 때 
submit - form을 submit 할 때
 
```

##### #6) DOM 관련 확인

```javascript
// DOM 관련 확인할 것들
element.appendChild('hi') // error

element.classList.add('a', 'b', 'c') // 클래스 3개 추가됨

querySelectorAll() // 은 배열이 아니라 NodeList 를 return
```

##### #7) 삼항연산자

```html
x >10 ? a=1: a=2
```

#8)array helper method

#### 

array helper method

filter map foreach, !! forof-callback은 아니지만(함수를 안넣는다) 반복문을 돌림, reduce- 도전 , foreach 

```javascript
// for of

let myArray = [1,2,3]

for (let k of myArray){

console.log(k)}
```





인터폴레이션(`{{ }}`)에서 사용 가능한 것들

- 비교함수 다 가능

""를 쓰는 경우:  사이에 -, . 등이 있을 때"



### #5)appendChild는 'NODE'만 인자로 받을 수 있다 (string 안됨)

```
p에 저장하고

document.createElement('p')

document.appendChild('hi') <---- error

hi = document.createTextNode('hi')

-> document.appendChild('hi')
```

arrow function

```javascript
this -> window의 함수를 가리킴
arrow funciton -> 
    const greeting = function(){
        console.log(this) <- 계속 window를 가리키니까/ 문맥적으로 무조건 상위의 scope 가리킴
        // 내가 원하는 this를 명확하게
    }
```

eventlistner why 

```
상위스코프니까, 이벤트리스너는 도큐먼트를 잡는데, 그 상위는 window니까 내가 원하는 this를 쓰려면 
function keyword 쓰면 -- button의 오브젝트를 주니까 
여기서는 그래서 function keyword를 쓴다
this를 쓰면 완벽하게 다른 값을 프린트한다
안쓰면, 전혀 상관이없다 ---this 
코드상에 this가 없는 경우에는 상관없다
method 안에서의 callback 함수에서도 무조건 arrow function을 쓰고
```

