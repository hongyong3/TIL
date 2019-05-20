[TOC]

## Vue_computed_and_watch

> [computed와 watch](https://kr.vuejs.org/v2/guide/computed.html)

**Content**

0. computed
1. computed vs method
2. watch
3. computed vs watch

---

### 0. computed

- vue의 템플릿에서도 자바스크립트의 표현식을 쓸 수 있습니다. 데이터 바인딩 방법중 하나인 `{{ }}` 안에 자바스크립트 표현식을 넣으면 됩니다. 하지만 간단한 연산일 때만 이용하는 것이 좋습니다. 너무 많은 연산을 템플릿 안에서 하면 코드가 비대해지고 유지보수가 어렵습니다. 아래의 예를 봅시다.

- 자바스크립트 표현식에서 주의할 점 

  - 자바스크립트의 선언문과 분기구문은 사용할 수 없습니다.
  - 복잡한 연산은 인스턴스 안에서 처리하고 화면에는 간단한 결과만 표시해야 합니다.

  ```html
  <div id="app">
      <!-- 선언문은 사용 불가능 (X) -->
      {{ let a = 10 }} 
      <!-- 분기 구문은 사용 불가능 (X) -->
      {{ if (true) {return 10} }}
      <!-- 삼항연산자 표현가능 (O) -->
      {{ true ? 10 : 0 }}
  
      <!-- 가능하지만 복잡한 연산은 인스턴스 안에서 수행 (X) -->
      {{ message.split('').reverse().join('') }}
      <!-- 스크립트에서 computed 속성으로 계산한 후 최종 값만 표현 (O) -->
      {{reverseMessage}}
  </div>
  ```

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
      <div id="app">
          <p>원본 메시지: "{{ message }}"</p>
  				<p>수정 메시지: "{{ message + "!!!!" }}"</p>
          <p>역순으로 표시한 메시지: "{{ message.split('').reverse().join('') }}"</p>
      </div>
  
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
          const app = new Vue({
              el:"#app",
              data:{
                  message:"가나다라마바사"
              }
          })
      </script>
  </body>
  </html>
  ```

- 이 템플릿은 간단하고 명료하지 않습니다. `message`를 역순으로 표시한다는 것을 알려면 찬찬히 살펴봐야 하겠죠. 템플릿에 메시지를 역순으로 표시할 일이 더 있으면 문제는 더 악화될 것입니다.

- 복잡한 로직이라면 반드시 **computed 속성** 을 사용해야 하는 이유입니다.

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
      <div id="app">
          <p>원본 메시지: "{{ message }}"</p>
          <p>역순으로 표시한 메시지: "{{ reversedMessage }}"</p>
      </div>
  
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
          const app = new Vue({
              el:"#app",
              data:{
                  message:"가나다라마바사"
              },
              computed: {
                  // 계산된 getter
                  reversedMessage: function () {
                      // `this` 는 app 인스턴스를 가리킵니다.
                      return this.message.split('').reverse().join('')
                  }
              }
          })
      </script>
  </body>
  </html>
  ```

- 이 예제에서는 computed 속성인 reversedMessage를 선언했습니다. 우리가 작성한 함수는 app.reversedMessage속성에 대한 getter 함수로 사용됩니다.

  ```javascript
  console.log(app.reversedMessage) // => '요세하녕안'
  vm.message = 'Goodbye'
  console.log(app.reversedMessage) // => 'eybdooG'
  ```

- 콘솔에서 이 예제를 직접 해볼 수 있습니다. `app.reversedMessage`의 값은 항상 `app.message`의 값에 의존합니다.

- 일반 속성처럼 computed 속성에도 템플릿에서 데이터 바인딩 할 수 있습니다. Vue는 `app.reversedMessage`가 `app.message`에 의존하는 것을 알고 있기 때문에 `app.message`가 바뀔 때 `app.reversedMessage`에 의존하는 바인딩을 모두 업데이트할 것입니다. 그리고 가장 중요한 것은 우리가 선언적으로(역자 주: 선언형 프로그래밍 방식에 따라서(아래 computed와 watch 비교에 추가 설명)) 의존 관계를 만들었다는 것입니다. computed 속성의 getter 함수는 사이드 이펙트가 없어 코드를 테스트하거나 이해하기 쉽습니다.

---

### 1. computed vs method

- 표현식에서 메소드를 호출하여 같은 결과를 얻을 수도 있습니다.

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
      <div id="app">
          <p>원본 메시지: "{{ message }}"</p>
          <p>역순으로 표시한 메시지: "{{ reversedMessage() }}"</p>
      </div>
  
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
          const app = new Vue({
              el:"#app",
              data:{
                  message:"가나다라마바사"
              },
              methods: {
                  reversedMessage: function () {
                      return this.message.split('').reverse().join('')
                  }
              }
          })
      </script>
  </body>
  </html>
  ```

- computed 속성 대신 메소드와 같은 함수를 정의할 수도 있습니다. 최종 결과에 대해 두 가지 접근 방식은 서로 동일합니다.

- 차이점은 computed 속성은 종속 대상을 따라 **저장(캐싱)**된다는 것 입니다. computed 속성은 해당 속성이 종속된 대상이 변경될 때만 함수를 실행합니다. 즉 message가 변경되지 않는 한, computed 속성인 reversedMessage를 여러 번 요청해도 계산을 다시 하지 않고 계산되어 있던 결과를 즉시 반환합니다.

- 또한 Date.now()처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않는다는 뜻입니다.

- 아래와 같이 코드를 작성하고 확인해봅시다.

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
      <div id="app">
          <p>{{dateMethod()}}</p>
          <p>{{dateComputed}}</p>
      </div>
  
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
          const app = new Vue({
              el:"#app",
              data:{
                  message:"가나다라마바사",
                  d: Date.now()
              },
              methods:{
                  dateMethod: function () {
                          return Date.now()
                      }
              },
              computed: {
                  dateComputed: function () {
                          return Date.now()
                      }
              }
          })
      </script>
  </body>
  </html>
  ```

- 콘솔창에서 다음을 입력하고 차이를 확인해봅시다.

  ```javascript
  app.dateComputed // computed는 값이기때문에 괄호 없이 호출 => 값 안변함 캐싱
  app.dateMethod() // 메소드 이기때문에 괄호로 호출 => 값 변함 계속해서 연산
  ```

---

### 2. watch

- 대부분의 경우 computed 속성이 더 적합하지만 사용자가 만든 감시자가 필요한 경우가 있습니다. 그래서 Vue는 watch 옵션을 통해 데이터 변경에 반응하는 보다 일반적인 방법을 제공합니다. 이는 데이터 변경에 대한 응답으로 비동기식 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 가장 유용합니다.

- 아래의 코드는 question값이 바뀔 때 마다 실행하는 함수 정의

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
      <div id="app">
          <p>{{title}}</p>
          <input v-model="question">
          <p>{{answer}}</p>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  
      <script>
          const app = new Vue({
              el:"#app",
              data:{
                  title:"질문을 입력해주세요",
  					      answer:'',
  					      question:''
              },
              watch:{
                  question:function(){
                      console.log(this.question)
                  }
              }
          })
      </script>
  </body>
  </html>
  ```

#### 2.1 watch 실습 (yes or no)

> [https://yesno.wtf](https://yesno.wtf/)

```javascript
const app = new Vue({
            el:"#app",
            data:{
                title:"질문을 입력해주세요",
					      answer:'',
					      question:''
            },
            watch:{
                question:function(){
                    console.log(this.question)
                    axios.get('https://yesno.wtf/api')
                    .then((response)=>{console.log(response)})
                }
            }

        })
```

- 복잡하니 method 로 빼자

```javascript
const app = new Vue({
    el:"#app",
    data:{
        title:"질문을 입력해주세요",
				answer:'',
				question:''
    },
    watch:{
        question:function(){
            console.log(this.question)
            this.getAnswer()
        }
    },
    methods:{
        getAnswer:function(){
            axios.get('https://yesno.wtf/api')
            .then((response)=>{console.log(response)})
        }
    }

})
```

- 입력할때마다 계속 요청을 보내니 마지막에 물음표로 끝날때만 요청보내보기

```javascript
const app = new Vue({
  el: '#app',
  data: {
    title: "질문을 입력해주세요.",
    answer: '',
    question: '',
  },
  watch: {
    question: function() {
      console.log(this.question)
      this.getAnswer()
    }
  },
  methods: {
    getAnswer: function() {
      if (this.question[this.question.length - 1] === '?') {
        console.log('마지막을 물음표로 끝내야 요청 보내준다.')
        axios.get('https://yesno.wtf/api')
          .then(response => {
            console.log(response)
          })
      }
    }
  }
})
```

- 콘솔에 찍히는 것 보다 사용자가 볼 수 있도록 변경, 요청에 대한 응답을 사용자에게 보여주자

```javascript
const app = new Vue({
  el: '#app',
  data: {
    title: "질문을 입력해주세요.",
    answer: '',
    question: '',
  },
  watch: {
    question: function() {
      console.log(this.question)
      this.getAnswer()
    }
  },
  methods: {
    getAnswer: function() {
      if (this.question[this.question.length - 1] === '?') {
        console.log('마지막을 물음표로 끝내야 요청 보내준다.')
        axios.get('https://yesno.wtf/api')
          .then(response => {
            console.log(response)
            this.answer = response.data.answer
          })
      }
    }
  }
})
```

- 최종코드 ( + 이미지 )

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>methods vs computed</title>
</head>

<body>
<div id="app">
  <p>{{ title }}</p>
  <input type="text" v-model="question">
  <p>{{ answer }}</p>
  <img v-bind:src="image">
</div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      title: "질문을 입력해주세요.",
      answer: '',
      question: '',
      image: '',;
    },
    watch: {
      question: function() {
        console.log(this.question)
        this.getAnswer()
      }
    },
    methods: {
      getAnswer: function() {
        if (this.question[this.question.length - 1] === '?') {
          console.log('마지막을 물음표로 끝내야 요청 보내준다.')
          axios.get('https://yesno.wtf/api')
            .then(response => {
              console.log(response)
              this.image = response.data.image
              this.answer = response.data.answer
            })
        }
      }
    }
  })
</script>
</body>
</html>
```

---

### 3. computed vs watch

> 명령적인 `watch` 콜백보다 계산된 속성을 사용하는 것이 더 좋다고 함.
>
> 일반적으로 선언형 프로그래밍이 명령형 프로그래밍보다 코드 반복이 적은 등 우수하다고 평가하는 경향이 있음.

- Vue는 Vue 인스턴스의 데이터 변경을 관찰하고 이에 반응하는 보다 일반적인 watch 속성을 제공합니다. 다른 데이터 기반으로 변경할 필요가 있는 데이터가 있는 경우,  사용하는 것이 더 좋습니다.
- watch : 명령형 ⇒ 프로그래밍의 상태와 상태를 변경시키는 구문의 관점에서 연산을 설명, 뭐뭐를 어떻게 해라
- computed : 선언형 ⇒ 계산해야 하는 목표 데이터를 정의하는 방식, 뭐뭐는 뭐다