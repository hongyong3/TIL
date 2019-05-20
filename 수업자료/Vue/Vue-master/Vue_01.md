[TOC]

## Vue_01

**Content**

0. Vue Intro
1. Vue Setting
2. 선언적 렌더링
3. Vue Devtools
4. Vue Instance Methods

> 2019.05.07 Tue

---

### 0. Vue Intro

> [Vue.js 가 무엇인가요?](https://kr.vuejs.org/v2/guide/index.html#Vue-js가-무엇인가요)

**MVVM Pattern 의 ViewModel 에 해당하는 View 단 라이브러리**

- Google에서 AngularJS 를 쓰던 [Evan You](https://twitter.com/youyuxi)가 Angular 의 좋은 점만을 가져와 가벼운 프레임워크를 만들고자 해서 탄생
- React 와 많이 닮아있고 일부 중요한 사항은 Angular 에서 영감을 받았다고 한다.
- 스스로를 진보적인(prograssive) 프레임워크라 칭한다.
- ~~(TMI) Evan You는 비전공자이다. 미술 & 미술사 전공~~
- ~~(TMI) gitlab([lab.ssafy.com](http://lab.ssafy.com))도 Vuejs 사용~~

**SPA (Single Page Application)**

- 서버로부터 완전한 새로운 페이지를 불러오지 않고, 현재의 페이지를 동적으로 다시 작성하는 방식을 사용하는 웹 애플리케이션이나 웹 사이트
- 따라서 페이지 전환이 없는 것이 특징
- JS로 사용자 인터페이스(UI)를 만들고, 로직을 수행하며 웹 서버와 통신까지 함

**MVVM Pattern**

- MVVM이란? 

  - `[M]odel, [V]iew, [V]iew-[M]odel` 의 약자

- MVC 와의 비교

  - MVC
    - django 가 이 패턴을 사용하고 있다.
    - View - `Template(html)`
    - Controller - `views.py`
    - Model - `models.py`

  ![1_W6GRvv3l4_PrnfKFx_8tLA](https://user-images.githubusercontent.com/18046097/57211617-de72bc80-701b-11e9-95b6-18556025d52f.png)

  

  - MVVM
    - Vue는 이러한 구조이다.
    - M : Model (Database)
    - V : View (HTML, DOM)
    - VM : **View-Model** (Vue)

![1_QGGtgBtp9EaYPfRnuu-feg](https://user-images.githubusercontent.com/18046097/57211547-9b184e00-701b-11e9-9b5b-6b860b8ebe22.png)

![view-model](https://user-images.githubusercontent.com/18046097/57211596-c26f1b00-701b-11e9-8341-ef145f5e79c7.png)

---

### 1. Vue Setting

#### 1.1 CDN 을 사용할 경우

```html
<!-- 도움되는 콘솔 경고를 포함한 개발 버전 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

#### 1.2 NPM 을 사용할 경우

> [Use NPM](https://kr.vuejs.org/v2/guide/installation.html#NPM)
>
> 대규모 응용 프로그램을 빌드할 때 권장
>
> Node.js 기반 빌드 도구에 아직 익숙하지 않으면 `vue-cli`로 시작하는 것을 추천하지 **않음**

```BASH
$ npm install vue
```

- 위 명령어를 입력하면 현재 위치에 node_modules 폴더가 생기고 그 안에 vue 폴더가 있다. 여기에 설치된 vue를 head tag 내에서 import 한다.

  ```html
  <script src="node_modules/vue/dist/vue.js"></script>
  ```

---

### 2. 선언적 렌더링

> Vue.js의 핵심은 간단한 템플릿 구문을 사용해 선언적으로 DOM에 데이터를 렌더링하는 것이다.

- id 를 지정한 html element 를 하나 작성한다.

  ```html
  <div id="app">
  </div>
  ```

- element 보다 하단에 script 태그와 `new Vue` 로 시작하는 Vue 인스턴스 하나를 만든다.

  > Vue Instance 생성자
  >
  > ```javascript
  > const app = new Vue({
  >   // options
  > })
  > ```

  - `el: '#app'` 으로 위에서 만든 element 를 지정한다.

  ```html
  <script>
    const app = new Vue({
  	  el: '#app',
  	})
  </script>
  ```

- 이렇게 하면 app을 id로 가진 html element와 Vue 인스턴스가 연결된다.

- 연결되긴 했지만, 가시적으로 확인 가능한 건 아직 없다. Vue 인스턴스에 데이터를 조금 넣어보고, html element에서 그 내용을 확인해 보도록 하자. 

  - `data`: Vue 인스턴스의 속성을 나타낸다. 다양한 정보들이 담길 수 있으며, 인스턴스가 들고 있어야 하는 각종 데이터나 인스턴스의 상태 정보를 담는다.
  - Vue 인스턴스는 data 이외에 *template, el, methods, life cycle callback* 등의 options 을 포함할 수 있다.

  ```html
  <script>
      const app = new Vue({
          el: '#app',
          data: {
              message: 'Hello, Ssafy!'
          }
      })
  </script>
  ```

- 그리고 message 속성을 html element 에서 보이도록 한다.(binding - 바인딩)

  - django 와 똑같은 방식, `{{ }}`을 사용한다.
  - 이렇게 중괄호 두개를 사용한 문자열 표현식을 **인터폴레이션(Interpolation, 보간법)**이라고 한다.

- 결과를 확인해보면, Vue 인스턴스의 message 속성의 값이 html에 렌더링 되서 나오게 된다.

  ```
  Hello, Ssafy!
  ```

- 여기서 Vue에서 중요한 포인트 중 하나는, app을 id로 가진 html element(DOM)와 Vue 인스턴스(데이터)가 연결되어 있기 때문에 Vue 인스턴스의 내용이 변경되면 html element에 렌더링 되는 내용도 즉각 변경된다. 이것이 Vue에서 이야기하는 **반응형**이다.

- 확인해보려면 html 파일을 브라우저에서 열고, 크롬 개발자도구 console 에서 아래와 같이 입력하면 message 내용이 변경된다.

  ```javascript
  app.message = 'Bye, Ssafy!'
  ```

- 위 내용을 통해서 알 수 있는 건, 이제 html은 Vue를 위한 껍데기 역할만 한다는 것이다. 알맹이는 전부 Vue 인스턴스 안에 있다!

---

### 3. Vue Devtools

> https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd
>
> Vue 개발을 편리하게 해주는 Chrome 확장 프로그램인 'Vue Devtools' 설치

- 설치가 되었으면 우측 상단에 Vue 로고가 뜨게 되고, 지금 보고 있는 페이지가 Vue로 작성된 것이라면 활성화가 된다.
- 활성화된 상태에서 개발자 도구를 열면 Vue 탭이 추가로 생겨있으며, Vue 인스턴스의 구조를 한눈에 볼 수 있다.
- (중요)`file://`에서 즉, 로컬에서 사용하려면 Extension Manage Page에서 `Allow access to file URLs` 체크해주어야 한다.

---

### 4. Vue Instance Methods

- 우리가 Vue를 처음 맛보면서 사용했던 `new Vue()` 는 Vue class 의 인스턴스를 만드는 것이고, Vue의 모든 구성은 이 인스턴스로부터 시작된다.
- 먼저 el, data, methods 부터 알아보자.

```javascript
// app Vue instance
var app = new Vue({
	// mount
	el

  // app initial state
  data

	filters

  // watch todos change for localStorage persistence
  watch

  // computed properties
  // http://vuejs.org/guide/computed.html
  computed

  // methods that implement data logic.
  // note there's no DOM manipulation here at all.
  methods
 
  // a custom directive to wait for the DOM to be updated
  // before focusing on the input field.
  // http://vuejs.org/guide/custom-directive.html
  directives
})
```

#### 4.1 el

- Vue 인스턴스와 DOM을 연결(mount - 마운트) 하도록 하는 옵션 
  - id 또는 class로 마운트 가능하다.
  - 마운트 하게 되면 해당 DOM 안에서만 Vue 인스턴스의 속성들을 사용할 수 있다.

#### 4.2 data

- Vue 인스턴스의 데이터 객체, 인스턴스의 `속성` 이라고도 부른다.
  - 데이터 객체는 반드시 기본 객체 `{ }`여야 한다.
  - 객체 내부의 아이템들은 value 로 모든 타입의 객체를 가질 수 있다. (ex. object, string, interger, array, ...)
  - 정의된 속성은 인터폴레이션(`{{ }}`)을 통해 View에서 렌더링 가능하다.
  - script 내에서는 `app.message`로 접근 가능하며, data 객체 자체에 접근하려면 `app.$data`로 접근 가능하다. 실제로는 `app.$data.message`와 `app.message`가 같다.
  - Vue 인스턴스 내에서는 `this.message`로 접근 가능하다.
  - `_` 또는 `$`로 시작하는 속성을 정의할 수는 있지만, 사용할 때 Vue의 내부 속성 및 API 메소드와 충돌할 수 있으므로 `app._property` 처럼 줄여서 사용할 수 없다. 반드시 `app.$data._property`로 접근 해야한다.

#### 4.3 methods

- Vue 인스턴스에 추가할 메소드들을 정의하는 곳이다.

  ```html
  <div id="app">
      {{ message }} - {{ count }}
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
      const app = new Vue({
          el: '#app',
          data: {
              message: 'Hello Ssafy!',
              count: 0,
          },
          methods: {
              plus: function () {
                  this.count++
              },
          },
      })
  </script>
  ```

- (주의) Arrow Function 을 메소드를 정의하는데 사용하면 안된다. Arrow Function은 부모 컨텍스트(Window - 브라우저 최상위 객체)를 바인딩하기 때문에 this는 Vue 인스턴스가 아니게 되며, this.count 가 undefined로 나타나게 된다.

---



