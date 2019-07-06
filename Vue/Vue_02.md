[TOC]

## Vue_02

**Content**

0. To Do App
1. v-for
2. v-if
3. v-on
4. v-bind
5. v-model
6. 인터폴레이션
7. filters
8. more v-model
9. Class Binding
10. Style Binding
11. Group by status
12. key
13. computed
14. Web Storage API
15. Watch

> 2019.05.07 Tue

---

### 0. To Do App

> To Do App 을 만들면서 Vue 의 문법들을 익혀보자.

- 새로운 html 파일을 생성하고, Vue CDN, 간단하게 인스턴스를 생성해서 연결해보자.

  ```html
  <div id="app"></div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
      const app = new Vue({
          el: '#app',
      })
  </script>
  ```

- todo 들이 저장될 속성(data)을 작성하자.

- 일단 문자열로 된 todo 리스트를 넣어 배열을 만들어보자.

  ```javascript
  const app = new Vue({
      el: '#app',
      data: {
          todos: [
              '점심 메뉴 고민',
              '사다리 타기',
              '야외수업하기',
              '야자하기',
          ],
      }
  })
  ```

- 이 todo리스트를 사용자가 볼 수 있게 View(html) 에 출력해보자.

  ```html
  <div id="app">
      {{ todos }}
  </div>
  ```

- 그런데 아래와 같이 배열의 형태로 나온다. todos 에 배열을 할당했기 때문이다.

  ```
  [ "점심 메뉴 고민", "사다리 타기", "야외수업하기", "야자하기" ]
  ```

---

### 1. v-for

> **디렉티브**
>
> - 디렉티브는 Vue에서 제공하는 특수 속성임을 나타내는 `v-` 접두어가 붙어있으며, 사용자가 짐작할 수 있듯 렌더링 된 DOM에 특수한 반응형 동작을 한다.
> - 디렉티브 속성의 값은 단일 JavaScript 표현식이다. (v-for은 예외)

- 이렇게 배열로 된 data는 디렉티브 `v-for`를 사용하여 하나씩 꺼내 사용할 수 있다.

- DOM 

  - 파이썬과 굉장히 유사한 문법을 가지고 있다.

  - `v-for`은 해당 디렉티브가 사용된 element 를 반복을 하는 것이다. 따라서 아래의 예시에서는 li element 를 todo의 개수만큼 반복한다.

    ```html
    <li v-for="todo in todos">
    	{{ todo }}
    </li>
    ```

- 지금은 todo가 단순 문자열인 내용만으로 되어 있는데, 추가적은 정보들을 더 가지고 있을 수 있도록 구조를 바꿔 보자.

  - 각각의 todo를 string이 아닌 object로 변경을 하고, completed라는 완료한 todo인지에 대한 정보를 추가한다.

  - 일단 '점심 메뉴 고민하기'만 완료(`true`)한 상태로 두자.

    ```javascript
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
                {
                    content: '점심 메뉴 고민',
                    completed: true,
                },
                {
                    content: '사다리 타기',
                    completed: false,
                },
                {
                    content: '야외수업하기',
                    completed: false,
                },
                {
                    content: '야자하기',
                    completed: false,
                },
            ],
        }
    })
    ```

  - todos의 구조가 바뀌었기 때문에 내용이 보이도록 하려면 DOM에서도 변경을 해주어야 한다.

    ```html
    <div id="app">
        <li v-for="todo in todos">
            {{ todo.content }}
        </li>
    </div>
    ```

  - 잘 나오는지 확인해보자.

---

### 2. v-if

- 우리가 completed 라는 완료를 했는지에 대한 정보를 추가했다. 완료한 todo는 보이지 않도록 만들어보자.

- 디렉티브 `v-if`를 사용해서 특정 조건을 만족 할 때만 보여지도록(렌더링되도록) 할 수 있다.

  ```html
  <div id="app">
      <li v-for="todo in todos" v-if="!todo.completed">
          {{ todo.content }}
      </li>
  </div>
  ```

  > **우선순위**
  >
  > 동일한 노드에 두가지 모두 있다면, `v-for`가 `v-if`보다 높은 우선순위를 가진다.
  >
  > 즉, `v-if`는 루프가 반복될 때마다 실행된다. 이는 일부 항목만 렌더링 할 때 유용하다.

- 완료한 todo는 `[완료!]`라는 메세지가 보이도록 변경해보자.

  - 이때는 디렉티브 `v-else`를 추가해서 특정 조건을 만족하지 않을때 렌더링 되는 것을 지정할 수 있다.

  - `v-else`는 `v-if` 엘리먼트 바로 뒤에 와야 인식된다.

    ```html
    <div id="app">
        <li v-for="todo in todos" v-if="!todo.completed">
            {{ todo.content }}
        </li>
        <li v-else>[완료!]</li>
    </div>
    ```

    > `v-else-if`도 존재한다.

---

### 3. v-on

- 이제는 클릭하면 완료된 것으로 처리해보자.

- 이때는 디렉티브 `v-on`을 사용해서 이벤트 리스너를 추가할 수 있다.

  - vanilla JS 의 addEventListener 와 같은 역할을 한다.

    - 다른 점이라면 vanilla JS의 이벤트 리스너는 JS 영역으로 HTML element를 querySelector로 가져와 이벤트를 붙여줬다면, Vue 는 HTML element 에다가 이벤트를 붙여준다.

  - `v-on:` 뒤에 오는 친구를 '**전달인자**' 라고 한다.

    - `v-on:click`, `v-bind:href`과 같이 `:`을 붙여 사용하는, 디렉티브 바로 뒤에 붙는 친구들을 지칭하며, `v-on`에서는 이벤트 리스너의 Trigger과 같은 친구이다.

  - 이렇게 inline 으로 할 수도 있고

    ```html
    <div id="app">
        <li v-for="todo in todos" v-if="!todo.completed" v-on:click="todo.completed = true">
            {{ todo.content }}
        </li>
        <li v-else>[완료!]</li>
    </div>
    ```

  - method 를 정의해서 할 수도 있다.

    ```javascript
    const app = new Vue({
        el: '#app',
        data: {
            todos: [
    			...
            ],
        },
        methods: {
            check: function(todo) {
                todo.completed = true
            },
        }
    })
    ```

- 그런데 한번 완료 되어버리면, 완료 취소를 할 수가 없다. Toggle 되도록 작성해보자.

  ```html
  <div id="app">
  		...
      <li v-else v-on:click="check(todo)">[완료!]</li>
  </div>
  ```

  ```javascript
  methods: {
      check: function(todo) {
          todo.completed = !todo.completed
      },
  }
  ```

---

### 4. v-bind

- HTML 태그의 속성 값을 데이터값으로 바인딩할 때 사용하는 디렉티브이다.

  ```html
  <!-- 예시 -->
  <img src="URL">
  <img v-bind:src="URL">
  ```

- js 수업에서 진행했던 dog and cat 과 axios 을 사용해서 실습해보자.

- 사전 준비

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  
  <body>
      <div id="main">
          <button>냐옹</button>
          <button>멍멍</button>
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
      <script>
  
      </script>
  </body>
  </html>
  ```

- Vue 인스턴스와 Dom 을 마운트(연결) / data 에 빈 이미지 주소 추가.

  ```javascript
  const dogsAndCats = new Vue({
      el: '#main',
      data: {
          image: '',
      },
  ```

- axios 를 통해 해당 이미지 주소를 가져오는 함수를 만들어서 method 로 만들기

  ```javascript
  const dogsAndCats = new Vue({
  		...
      methods: {
          getCatImage: function(){
              const URL = 'https://api.thecatapi.com/v1/images/search'
              axios.get(URL)
                  .then(response => {
                      this.image = response.data[0].url
                  })
          },
          getDogImage: function(){
              const URL = 'https://dog.ceo/api/breeds/image/random'
              axios.get(URL)
                  .then(response => {
                      this.image = response.data.message
                  })
          },
      }
  })
  ```

- View 설정

  ```html
  <div id="main">
      <button v-on:click="getCatImage">냐옹</button>
      <button v-on:click="getDogImage">멍멍</button>
      <hr>
      <img v-bind:src="image">
  </div>
  ```

- 이제 반복문(v-for)을 통해 데이터를 뿌려주자.

  - images 를 빈 배열로 만든다.
  - push 메서드를 통해 배열에 axios 로 응답받은 이미지 주소를 넣어준다.
  - 완성 코드

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <style>
          img {
              width: 300px;
              height: 300px;
          }
      </style>
  </head>
  
  <body>
  <div id="main">
      <button v-on:click="getCatImage">냐옹</button>
      <button v-on:click="getDogImage">멍멍</button>
      <span>냐옹 {{ countCat }}</span>
      <span>멍멍 {{ countDog }}</span>
      <hr>
      <img v-for="image in images" v-bind:src="image">
  </div>
    
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
  const dogsAndCats = new Vue({
      el: '#main',
      data: {
          countCat: 0,
          countDog: 0,
          images: [],
      },
      methods: {
          getCatImage: function(){
              const URL = 'https://api.thecatapi.com/v1/images/search'
              axios.get(URL)
                  .then(response => {
                      this.images.push(response.data[0].url)
                      this.countCat++
                  })
          },
          getDogImage: function(){
              const URL = 'https://dog.ceo/api/breeds/image/random'
              axios.get(URL)
                  .then(response => {
                      this.images.push(response.data.message)
                      this.countDog++
                  })
          },
      }
  })
  </script>
  </body>
  </html>
  ```

- 위 코드가 와닿지 않는다면 아래처럼도 가능하다.

  - 각 함수를 먼저 만들고 Vue methods 에 추가만 해주는 방식.

  ```html
  <script>
  const Cat = function() {
      const URL = 'https://api.thecatapi.com/v1/images/search'
      axios.get(URL)
          .then(response => {
              this.images.push(response.data[0].url)
              this.countCat++
          })
  }
  const Dog = function() {
      const URL = 'https://dog.ceo/api/breeds/image/random'
      axios.get(URL)
          .then(response => {
              this.images.push(response.data.message)
              this.countDog++
          })
  }
  const dogsAndCats = new Vue({
      el: '#main',
      data: {
          countCat: 0,
          countDog: 0,
          images: [],
      },
      methods: {
          getCatImage: Cat,
          getDogImage: Dog,
      }
  })
  </script>
  ```

---

### 5. v-model

- 여기까지는 이미 정해져 있는 todo들에 대해서만 조작을 했다. 우리는 To Do App을 만들고 있으니까 우리가 해야할 일을 추가하는 것도 당연히 가능해야한다.

- `todo 를 추가 한다는 것 === todos 배열에 새로운 item 을 추가한다는 것`이라는 사실을 단번에 알아차릴 것이다.

-  vanilla JS 였다면 input 태그를 만들고 여기에 값을 입력해서 버튼 누르면, input 태그의 value를 가져와서 `todos.push` 라고 생각하는 것이 맞다.

- 하지만 Vue는 HTML element와 Vue 인스턴스의 동기화(반응형)가 특징이다. 따라서 input 태그에 작성된 value와 data(속성)의 동기화가 디렉티브 `v-model`을 통해서 가능하다.

  - DOM

    ```html
    <div id="app">
      ...
      <input type="text" v-model="newTodo">
    </div>
    ```

  - Vue instance

    ```javascript
    data: {
      ...,
      newTodo: '',
    }
    ```

- 코드를 작성하고, Vue devtools를 켜고 data의 newTodo 값을 확인하면서 input에 값을 넣어보자. 두개가 한몸인듯 같은 값이 들어가는 것을 확인할 수 있다.

- 이렇게 input 태그의 값이 Vue instance와 동기화가 된다면, 해당 값을 Vue instance 내부의 method를 통해서 조작하는 것이 가능하게 된다.

  - `newTodo`에 있는 값을 `todos`에 추가하는 method를 작성하자.

    - 여기서 사용하는 `this`는 Vue instance를 뜻한다.

    - todos에 들어있는 item들은 object이기 때문에 object 형태로 만들어서 넣어주자.

      ```javascript
      methods: {
        ...,
        addTodo: function(){
          this.todos.push({
      			content: this.newTodo,
      			completed: false,
      		})
        }
      }
      ```

  - 그리고 input 태그에다가 enter를 치면, `addTodo` method가 실행되도록 하자. 파라미터는 필요없다.

    ```html
    <div id="app">
      ...
    	<div>
    		<input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
    	</div>
    </div>
    ```

- 값을 입력하고 enter를 쳐보자.

- 값은 잘 추가되는데, input에 있는 값이 사라지지 않는다. clear를 해주면 된다. 

- input value를 변경했을 때 newTodo도 같이 변경 되었듯이 newTodo 를 변경해도 input value가 변경이 된다.

- 따라서 newTodo를 todos에 추가한 후, newTodo를 빈 문자열로 만들어주면 input이 clear 될 것이다.

  ```javascript
  methods: {
    ...,
    addTodo: function(){
      this.todos.push({
        content: this.newTodo,
        completed: false,
      })
      this.newTodo = ''
    }
  }
  ```

- enter 말고 버튼으로도 추가할 수 있도록 하자.

  ```html
  <div id="app">
    ...
  	<div>
  	  <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
  		<button v-on:click="addTodo">+</button>
  	</div>
  </div>
  ```

- 완료한 todo들을 일괄 삭제하는 버튼을 만들어보자.

  - 핵심은 `.filter`를 사용하는 것이다.

  ```html
  <footer>
  	<button v-on:click="clearCompleted">Clear</button>
  </footer>
  ```

  ```javascript
  methods: {
    ...,
    clearCompleted: function () {
        // filter 로 false 애들만 필터해서 todos 에 다시 할당.
        const notCompletedTodos = this.todos.filter(todo => !todo.completed)
        this.todos = notCompletedTodos
    },
  }
  ```

---

### 6. 인터폴레이션

- `{{ }}` 장고와 같은 이중 중괄호를 사용한다.

  ```html
  <div id="app">
    {{ message }}
  </div>
  
  <script>
    var app = new Vue({
      el: '#app',
      data: {
        message: 'Hello, ssafy!',
      }
    })
  </script>
  ```

- JavaScript 표현식도 사용가능하다

  ```html
  {{ number + 1 }}
  
  {{ ok ? 'YES' : 'NO' }}
  
  {{ message.split('').reverse().join('') }}
  
  <div v-bind:id="'list-' + id"></div>
  ```

---

### 7. filters

- 인터폴레이션을 통해서 문자열을 보여주거나 v-bind를 통해 HTML 속성에 값을 표현할 때, 값의 형식을 바꿀 수 있도록 하는 기능

- Django에서의 templatetags 와 같은 역할을 한다.

  ```html
  <div id="app">
    {{ name | capitalize }}
  </div>
  
  <script>
    var app = new Vue({
      el: '#app',
      data: {
        name: 'google',
      },
  		filters: {
  		  capitalize: function (value) {
  		    if (!value) return ''
  		    value = value.toString()
  		    return value.charAt(0).toUpperCase() + value.slice(1)
  		  }
  		}
    })
  </script>
  ```

  - 왼쪽의 속성 값(name)이 오른쪽 filter(capitalize)의 첫번째 인자로 넘어가게 된다. 따라서, Vue 인스턴스 내부에 정의된 capitalize 함수의 파라미터 value에는 name의 값이 오게 된다.

---

### 8. more v-model

- 문자열 & input text 만 동기화 되는 것 아니다. 다른 케이스도 살펴보자.

- 현재 todo를 클릭하면 `[완료!]` 텍스트로 바뀌도록 되어 있다. 

  - 흔하게 볼 수 있는 to do app의 UI 처럼 checkbox를 이용해서 완료를 표시해보자.
  - checkbox 태그와 v-model로 데이터 바인딩을 하게 되면 boolean 값이 바인딩 되며, 체크를 할 경우 true, 체크를 해제할 경우 false로 data 속성 값이 업데이트 된다.

  ```html
  <!-- checkbox로 변경. v-if, v-on:click 제거. -->
  <li v-for="todo in todos">
    <input type="checkbox" v-model="todo.completed">
  	<span>{{ todo.content }}</span>
  </li>
  ```

  - Vue devtools 로 todo의 completed 값이 true, false 로 잘 토글 되는지 확인한다.

---

### 9. Class Binding

- CSS Rule을 하나 만들어서 완료된 todo는 취소선을 긋고 투명도도 설정해보자.

  - HTML element 속성인 class에 Vue 인스턴스 data 속성의 값을 주는거라 `class="{{ todo.complete }}"`처럼 사용할 수 없고 디렉티브 `v-bind`를 사용해야 한다.

  - 값에 단순히 class 문자열이 저장되어 있다면 그냥 `v-bind:class="className"`으로 사용하면 되겠지만, 우리는 `todo.completed`의 참, 거짓에 따라 class 값을 주고 안 주고를 결정해야한다.

  - 따라서, 다음 예제와 같이 객체를 사용해야 한다. 객체의 value 값이 true면, key 값으로 된 class를 추가하게 된다.

    ```html
    <style>
      .completed {
        text-decoration: line-through;
        opacity: 0.6;
      }
    </style>
    
    <li v-for="todo in todos" v-bind:class="{completed: todo.completed}">
      ...
    </li>
    ```

---

### 10. Style Binding

- Class Binding과 유사하게 객체를 값으로 넘겨주어 인라인 스타일을 부여할 수 있다. 

  - key에는 CSS 속성, value에는 JS로 된 표현식이 온다.

  ```html
  <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
  ```

  ```javascript
  data: {
    activeColor: 'red',
    fontSize: 30,
  }
  ```

---

### 11. Group by Status

- 지금 Todo들은 미완료/완료 구분 없이 하나의 리스트에 함께 나오고 있는데, 완료된 todo, 진행중인 todo 끼리 따로 모아서 보여지도록 만들어 보자.

  ```html
  <li v-for="todo in todosByStatus()" ... >
    ...
  </li>
  ```

  ```javascript
  data: {
  	...,
  	status: 'all',
  },
  methods: {
    ...,
      todosByStatus: function () {
          if (this.status === 'active') {
              return this.todos.filter(todo => !todo.completed)
          }
          if (this.status === 'completed') {
              return this.todos.filter(todo => todo.completed)
          }
          return this.todos
      },
  }
  ```

- console에서 `app.status = 'completed' `같이 status 값을 변경해보면서 리스트가 어떻게 변하는지 살펴보자.

- 처음 상태는 status가 'all'이기 때문에 모든 todo가 보여지는데 앞서 사용 했었던 `v-model`을 이용해서 status를 선택할 수 있는 `select` 태그를 만들어 보도록 하자.

  ```html
  <div id="app">
    <select v-model="status">
      <option value="all" selected>all</option> 
      <option value="active">active</option>
      <option value="completed">completed</option>
    </select>
    ...
  </div>
  ```

- select에서 고른 대로 status 값이 바뀌는지 확인해보고, todo 리스트도 잘 바뀌는지 확인해보자.

- 그런데 체크박스를 클릭하면 동작하다 보면 의도치 않게 이상하게 동작하는 부분이 한가지 있을 것이다.

---

### 12. key

- 위와 같이 예상치 못한 동작을 하는 이유는 렌더링 된 element list에 `key` 속성이 없기 때문이다.

- Vue는 렌더링된 element list를 갱신할 때 기준으로 삼을 고유한 `id 값`이 필요하며 이를 기준으로 어떤 위치에 있는 요소를 변경을 하고 업데이트를 하고 위치를 변경할 지 계산한다.

  > Vue가 v-for에서 렌더링된 엘리먼트 목록을 갱신할 때 기본적으로 "in-place patch" 전략을 사용합니다. 데이터 항목의 순서가 변경된 경우 항목의 순서와 일치하도록 DOM 요소를 이동하는 대신 Vue는 각 요소를 적절한 위치에 패치하고 해당 인덱스에서 렌더링할 내용을 반영하는지 확인합니다. - 공식문서

- key 속성을 v-bind를 사용하여 부여

  - key 속성의 값은 문자열이나 숫자만 가능(배열, 객체 불가능)

    ```html
    <li v-for="todo in todosByStatus()" ... v-bind:key="todo.id">
    	...
    </li>
    ```

- todo들에게 id 값 부여

  ```javascript
  todos: [
    {
      id: 1,
      content: '점심 메뉴 고민하기',
      completed: true,
    },
    {
      id: 2,
      content: '사다리 타기',
      completed: false,
    },
    {
      id: 3,
      content: '야외수업',
      completed: false,
    },
    {
      id: 4,
      content: '야자하기',
      completed: false,
    },
  ],
  ```

- 새로운 todo가 생길 때 마다, 중복된 id 생성 방지를 위하여 `Date.now()` 사용

  ```javascript
  methods: {
    ...
    addTodo: function(){
      this.todos.push({
        id: Date.now(), // 추가
        content: this.newTodo,
        completed: false,
      })
      this.newTodo = ''
    },
  	...
  }
  ```

---

### 13. computed

- methods에 `todosByStatus` 만들 것을 이렇게 computed 속성에 정의할 수도 있다.

  ```javascript
  computed: {
      todosByStatus: function () {
          if (this.status === 'active') {
              return this.todos.filter(todo => !todo.completed)
          }
          if (this.status === 'completed') {
              return this.todos.filter(todo => todo.completed)
          }
          return this.todos
      },
  ```

  ```html
  <li v-for="todo in todosByStatus" ... >
    ...
  </li>
  ```

---

### 14. Web Storage API

- 여태까지 새로고침을 하면 수정사항이 다 날아가버렸다. 이 내용들을 어딘가에 저장해야 한다.

- 브라우저는 특정 도메인을 위한 Storage(저장 공간)를 제공한다.

  - 개발자 도구 > Application 탭 > Storage 항목에서 어떠한 데이터들이 저장되어있는지 볼 수 있다.

- Storage의 종류 

  - sessionStorage 
    - 페이지의 세션이 유지되는 동안(브라우저가 종료되기 전까지) 사용할 수 있는 저장 공간
  - localStorage 
    - sessionStorage와 같은 역할을 하지만, 브라우저가 닫히거나 다시 열리더라도 유지

- Storage는 단순한 key-value 저장소이며, 이는 객체와 비슷하다. (콘솔에서 예시로 입력해보고 개발자 도구에서 값이 저장되는 것을 확인해 보자.) 

  - `localStorage.getItem(key)` : 아이템을 가져
  - `localStorage.setItem(key, value)` : 아이템을 저장
  - `localStorage.removeItem(key)` : 아이템을 삭제
  - `localStorage.length` : 길이

- localStorage를 이용하여 To Do 들을 저장해보자. 

  - localStorage를 todo를 저장하는데 사용을 하게 되면, localStorage가 MVVM에서 Model이 된다.

    ```javascript
    const STORAGE_KEY = 'vue-todos'	// 임의로 지정 가능
    const todoStorage = {
        fetch: function () {
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
        },
        save: function (todos) {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
        }
    }
    ```

---

### 15. Watch

```javascript
const app = new Vue({
	...
	watch: {
    todos: {
      handler: function (todos) {
        todoStorage.save(todos)
      },
      deep: true,
    }
  },
	...
})
```

> - handler : 특정 데이터가 변경되었을 때, 실행할 함수.
> - deep : Object의 nested item들도 관찰할지 유무. `true`일 경우 내부 요소들도 감시함.

---

**todo app 완성 코드**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
    .completed {
        text-decoration: line-through;
        opacity: 0.6;
    }
    </style>
</head>
<body>
    <!-- <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div> -->
    <div id="app">
        <select v-model="status">
            <option value="all" selected>all</option>
            <option value="active">active</option>
            <option value="completed">completed</option>
        </select>
        <li v-for="todo in todosByStatus" v-bind:class="{completed: todo.completed}" v-bind:key="todo.id">
            <input type="checkbox" v-model="todo.completed">
            <span>{{ todo.content }}</span>
        </li>
        <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
        <button @click="addTodo">+</button>
        <footer>
            <button @click="clearCompleted">Clear</button>
        </footer>
        <span>{{ reversedNewTodo }}</span>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const STORAGE_KEY = 'vue-todos'
        const todoStorage = {
            fetch: function () {
                return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
            },
            save: function (todos) {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(todos))
            }
        }

        const app = new Vue({
            el: '#app',
            data: {
                todos: todoStorage.fetch(),
                newTodo: '',
                activeColor: 'red',
                fontSize: 30,
                status: 'all',
            },
            methods: {
                check: function (todo) {
                    todo.completed = !todo.completed
                },
                addTodo: function () {
                    this.todos.push({
                        id: Date.now(),
                        content: this.newTodo,
                        completed: false,
                    })
                    this.newTodo = ''
                },
                clearCompleted: function () {
                    // filter 로 false 애들만 필터해서 todos 에 다시 할당.
                    const notCompletedTodos = this.todos.filter(todo => !todo.completed)
                    this.todos = notCompletedTodos
                },
            },
            computed: {
                todosByStatus: function () {
                    if (this.status === 'active') {
                        return this.todos.filter(todo => !todo.completed)
                    }
                    if (this.status === 'completed') {
                        return this.todos.filter(todo => todo.completed)
                    }
                    return this.todos
                },

                reversedNewTodo: function () {
                    return this.newTodo.split('').reverse().join('')
                },
            },
            watch: {
                todos: {
                    handler: function(todos){
                        todoStorage.save(todos)
                    },
                    deep: true,
                }
            }
        })
    </script>
</body>
</html>
```