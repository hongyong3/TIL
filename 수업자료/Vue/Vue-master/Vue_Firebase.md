[TOC]

## Firebase

**Content**

0. Todo with Firebase
1. ChatApp with Firebase
2. Deploy Chatapp

> 2019.05.08 Wed

---

### 0. Todo with Firebase

> https://firebase.google.com/?hl=ko

- 프로젝트 만들기

  - 대한민국
  - asia-northeast1

- Database

  ![Untitled](https://user-images.githubusercontent.com/18046097/57495306-859b7080-7308-11e9-9af5-5eaf9140ee17.png)

  ![1](https://user-images.githubusercontent.com/18046097/57495313-8a602480-7308-11e9-97f9-bd27518b57e8.png)

  - `테스트 모드` 로 시작

#### 0.1 Firebase setting

- Import libraries (**cdn 넣는순서 중요** vue ⇒ firebase ⇒ vuefire) (`<head>`)

  ```html
  <!-- Google Firebase -->
  <script src="https://www.gstatic.com/firebasejs/5.8.4/firebase.js"></script>
  <!-- Vue에서 firebase를 쓰기 쉽게 해주는 라이브러리 vuefire -->
  <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
  ```

- Initialize Firebase (`<head>`)

  - firebase app 설정에서 api key 를 가져온다.

  ```html
  <script>
      const config = {
          apiKey: "AIzaSyA8vzdWNElAgFase440TPFPCuwtmGaVvjwM",
          projectId: "djpy2-todo-94f58",
          databaseURL: "https://djpy2-todo-94f58.firebaseio.com/",
      }
      firebase.initializeApp(config)
  </script>
  ```

- Initialize database(`<body>`)

  ```javascript
  const database = firebase.database()
  const app = new Vue({
    	...
  ```

- 이제 data 에서 todos 를 삭제한다.

  ```javascript
  data: {
      newTodo: '',
      status: 'all',
  },
  firebase: {
      todos: database.ref('todos'),
  },
  ```

- data가 변경되면서 바뀌어야 하는 부분들

  - methods 내부에서 data 를 조작하는 모든 포인트
  - todos 를 조작하는 방법이 완전히 바뀌었기 때문 (JS Array → firebase object)

  ```javascript
  methods: {
      check: function (todo) {
          todo.completed = !todo.completed
      },
      addTodo: function () {      // 추가 방법
          if (this.newTodo) {
              this.$firebaseRefs.todos.push({
                  id: Date.now(),
                  content: this.newTodo,
                  completed: false,
              })
          }
          this.newTodo = ''
      },
      clearCompleted: function(){     // 삭제 방법
          const completedTodos = this.todos.filter(todo => todo.completed)
          completedTodos.forEach(todo => {
              this.$firebaseRefs.todos.child(todo['.key']).remove()
          })
      },
      updateTodo: function (todo) 	// v-modle 로 실시간 동기화 불가능 -> item 업데이트 방법
          const newTodo = { ...todo }
          delete newTodo['.key']
          this.$firebaseRefs.todos.child(todo['.key']).set(newTodo)
      },
  },
  ```

- v-model이 로컬 data와는 동기화 되지만, firebase database와는 실시간 동기화가 불가능해져서, 체크박스 값이 변경 될 때마다 `updateTodo` methods 실행해서 직접 firebase에 저장되어 있는 todo를 업데이트 해주어야  한다.

  ```html
  <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)">
  ```

- 완성코드

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  
    <!-- vue -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- firebase -->
    <script src="https://www.gstatic.com/firebasejs/5.8.4/firebase.js"></script>
    <!-- vuefire -->
    <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
    <script>
      const config = {
        apiKey: "AIzaSyA8vzdWNElAgFjl440TPFPCuwtmGaVvjwM",
        projectId: "djpy2-todo-94f58",
        databaseURL: "https://djpy2-todo-94f58.firebaseio.com/",
      }
      firebase.initializeApp(config)
    </script>
  
    <style>
      .completed {
        text-decoration: line-through;
        opacity: 0.6;
      }
    </style>
  </head>
  
  <body>
    <div id="app">
      <select v-model="status">
        <option value="all" selected>all</option>
        <option value="active">active</option>
        <option value="completed">completed</option>
      </select>
      <li v-for="todo in todosByStatus" v-bind:class="{completed: todo.completed}" v-bind:key="todo.id">
        <input type="checkbox" v-model="todo.completed" @change="updateTodo(todo)">
        <span>{{ todo.content }}</span>
      </li>
      <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">
      <button @click="addTodo">+</button>
      <footer>
        <button @click="clearCompleted">Clear</button>
      </footer>
    </div>
  
    <script>
      const database = firebase.database()
      const app = new Vue({
        el: '#app',
        data: {
          newTodo: '',
          status: 'all',
        },
        firebase: {
          todos: database.ref('todos'),
        },
        methods: {
          check: function (todo) {
            todo.completed = !todo.completed
          },
          addTodo: function () {
            if (this.newTodo) {
              this.$firebaseRefs.todos.push({
                id: Date.now(),
                content: this.newTodo,
                completed: false,
              })
            }
            this.newTodo = ''
          },
          clearCompleted: function () {
            const completedTodos = this.todos.filter(todo => todo.completed)
            completedTodos.forEach((todo) => {
              this.$firebaseRefs.todos.child(todo['.key']).remove()
            })
          },
          updateTodo: function (todo) {
            const newTodo = { ...todo }
            delete newTodo['.key']
            this.$firebaseRefs.todos.child(todo['.key']).set(newTodo)
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
        },
        watch: {
          todos: {
            handler: function (todos) {
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

---

### 1. ChatApp with Firebase

- Todo App 처럼 Firebase Database 사용해서 단순 텍스트 저장하도록 사전 구현

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
  	<meta charset="UTF-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  	<meta http-equiv="X-UA-Compatible" content="ie=edge">
  	<title>Document</title>
  	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  	<script src="https://www.gstatic.com/firebasejs/5.8.4/firebase.js"></script>
  	<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
  	<script>
  		// Initialize Firebase
  		var config = {
  			apiKey: "AIzaSyA6dK-btmSA_9fpN9asvm8nWoA1rdLSBm0",
  			databaseURL: "https://djpy2-chat-f5cf4.firebaseio.com/",
  			projectId: "djpy2-chat-f5cf4",
  		}
  		firebase.initializeApp(config);
  	</script>
  </head>
  
  <body>
  	<div id="app">
  		<ul>
  			<li v-for="message in messages">
  				<b>{{ message.content }}</b>
  			</li>
  		</ul>
  		<div>
  			<input type="text" v-model="newMessage" v-on:keyup.enter="createMessage">
  			<button v-on:click="createMessage">></button>
  		</div>
  	</div>
  
  	<script>
  		const database = firebase.database()
  
  		const app = new Vue({
  			el: '#app',
  			data: {
  				newMessage: '',
  			},
  			firebase: {
  				messages: database.ref('messages'),
  			},
  			methods: {
  				createMessage: function () {
  					if (this.newMessage) {
  						this.$firebaseRefs.messages.push({
  							content: this.newMessage,
  						})
  					}
  					this.newMessage = ''
  				},
  			},
  		})
  	</script>
  </body>
  </html>
  ```

#### 1.1 Authentication

> Authentication - 로그인방법 - 이메일/비밀번호 를 활성화 시켜준다.

- 로그인 화면 만들기

  - firebase UI -  https://firebase.google.com/docs/auth/web/firebaseui

    ```html
    <script src="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.js"></script>
    <link type="text/css" rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.css" />
    ```

  - Initialize auth with UI

    ```javascript
    const auth = firebase.auth()
    const ui = new firebaseui.auth.AuthUI(auth)
    ```

- methods

  - `start()` 의 첫번째 파라미터: 어디에다가 로그인 화면 뿌릴건지?

    - 셀렉터 넣으면 된다.

    - 그리고 html element 하나 만들어 준다.

      ```html
      <div v-else>
        <!-- show login & sign up form -->
        <div id="firebaseui-auth-container"></div>
      </div>
      ```

  - `signInOption`: 무슨 방식으로 로그인 할건지?

    - `EmailAuthProvider`: firebase console에서 활성화 한 **이메일** 방식.

  - `signInSuccessWithAuthResult:` 로그인 성공후에 어떻게 할건지?

    - 이 아이는 `return true`일 경우, 다른 페이지로 redirect 시키려고 `signInSuccessUrl`을 찾는다. 그런데 우리는 Vue SPA 이다.
    - `return false` 해놓으면 redirect 하지 않고 로그인 창만 숨긴다.
    - `authResult`: 로그인 관련 정보들이 들어있고, `authResult.user`에 로그인 성공한 유저의 정보가 들어있다. 얘를 가져와서 data 속성을 업데이트 한다.

    ```javascript
    methods: {
    	...
    	},
    	initUi: function () {
    		ui.start('#firebaseui-auth-container', {
    			signInOptions: [
    				firebase.auth.EmailAuthProvider.PROVIDER_ID,
    			],
    			callbacks: {
    				signInSuccessWithAuthResult: (authResult, redirectUrl) => {
    					// User successfully signed in.
    					// Return type determines whether we continue the redirect automatically
    					// or whether we leave that to developer to handle.
    					this.currentUser.uid = authResult.user.uid
    					this.currentUser.email = authResult.user.email
    					this.currentUser.displayName = authResult.user.displayName
    					return false;
    				},
    			},
    		})
    	},
    ```

  - 여기까지 하고 브라우저 콘솔에서 `app.initUi()` 입력하면 화면이 쨔쟌 나온다.

  - 근데 이제 이 코드 `app.initUi()`가 화면이 렌더링 되면서 실행이 되어야 한다. (mount)

#### 1.2 Mounted

- 마운트 됨과 동시에 실행되는 함수

  ```javascript
  mounted: function(){
    this.initUi()
  },
  ```

- 이제 자동으로 로그인 창이 보인다.

- 그 다음에는 로그인이 되어있으면 채팅창, 아니면 로그인창을 나눠서 보여줘보자.

  - 로그인한 유저의 정보를 담을 data 속성 만들기

    ```javascript
    data: {
    	newMessage: '',
    	currentUser: {
    		uid: '',
    		email: '',
    		displayName: '',
    	},
    },
    ```

  - 로그인 유무에 따라 화면 분기

    - currentUser.uid가 있으면 로그인이 된 것이다.

      ```html
      <div v-if="currentUser.uid">
        <!-- if user is authenticated -->
        ...
      </div>
      <div v-else>
        <!-- show login & sign up form -->
        <div id="firebaseui-auth-container"></div>
      </div>
      ```

- 그런데..? 로그인을 하고 나서 새로고침을 하니 무조건 다시 로그인 창이 뜬다?

  - 이유는 `currentUser`에 로그인 정보가 유지되지 않기 때문이다.
  - 따라서 mounted 에서 로그인 정보를 가져와서 data `currentUser`에 넣어줘야 `v-if="currentUser.uid"`가 의미가 있어진다.

- firebase에서 제공하는 로그인 유무 체크 메소드

  - 정확하게는 Auth(로그인) 정보가 변경될 때마다 실행되는 함수를 정의하는 것! (콜백)

    - Auth 정보가 변경되었는데, user 파라미터에 user 정보가 담겨 넘어왔다면 로그인 상태인 것
    - 그게 아니라면 로그인 상태가 아니기 때문에 로그인 창을 보여줄 것

    ```javascript
    mounted: function () {
    	auth.onAuthStateChanged(user => {
    		if (user) {
    			// User is signed in.
    			this.currentUser.uid = user.uid
    			this.currentUser.email = user.email
    			this.currentUser.displayName = user.displayName
    		} else {
    			// No user is signed in.
    			this.initUi()
    		}
    	})
    },
    ```

#### 1.3 Logout

- 로그아웃 버튼 만들기

  ```html
  <header>
    <span>Hi, {{ currentUser.displayName }}</span>
    <button @click="logout">로그아웃</button>
  </header>
  ```

- method 만들기

- 주의 사항.

  - currentUser를 먼저 초기화 하고, `auth.signOut()`호출 할 것. 그래야 `signOut()` 되는 시점에, 로그인 창을 뿌려주는 `div#firebaseui-auth-container`가 존재하게 되어서 오류를 뿜지 않는다.
  - 코드 실행 순서로 인해, 위 오류가 발생하는 이유는 `v-if="currentUser.uid"` 때문이다.

  ```javascript
  logout: function () {
  	this.currentUser = {
  		uid: '',
  		email: '',
  		displayName: '',
  	}
  	auth.signOut()
    // after logout
  		.then(() => {})
  		.catch(error => console.log(error))
  }
  ```

#### 1.4 채팅 작성자 추가

```html
<li v-for="message in messages">
  <b>{{ message.username }}</b>: {{ message.content }}
</li>
```

```javascript
createMessage: function () {
	if (this.newMessage) {
		this.$firebaseRefs.messages.push({
			username: this.currentUser.displayName,		// 코드 추가
			content: this.newMessage,
		})
	}
	this.newMessage = ''
},
```

---

### 2. Deply ChatApp

> [firebase cli](https://firebase.google.com/docs/cli/?hl=ko)
>
> [firebase 호스팅](https://firebase.google.com/docs/hosting/?hl=ko)
>
> 윈도우는 git bash 가 아닌 기본 cmd 로 진행해야 한다.

- firebase cli 설치

  ```bash
  $ npm install -g firebase-tools
  ```

- firebase cli login

  ```bash
  $ firebase login 
  # 윈도우에서는 firebase login --interactive 로 입력
  ```

- firebase init

  ```bash
  $ firebase init
  ```

- Database, Hosting 선택 (스페이스바로 선택 후 엔터키로 이동)

<img width="776" alt="Screen Shot 2019-05-10 at 11 24 11 AM" src="https://user-images.githubusercontent.com/18046097/57498319-5855bf00-7316-11e9-8a3c-ee18cd7e0822.png">

- 프로젝트 선택

<img width="776" alt="Screen Shot 2019-05-10 at 11 37 31 AM" src="https://user-images.githubusercontent.com/18046097/57498768-2cd3d400-7318-11e9-8a1f-61ae5cc66748.png">

- Database & Hosting
- Hosting 설정 
  - static 파일(index.html 등)의 위치 → public
  - SPA로 설정할건지? → Yes

<img width="776" alt="Screen Shot 2019-05-10 at 11 24 29 AM" src="https://user-images.githubusercontent.com/18046097/57498388-a5d22c00-7316-11e9-8f63-f457e70a90a1.png">

- 설정 완료 후, 자동으로 생성된 public 폴더에 작업한 html 파일을 넣고 index.html 로 이름을 변경한다.

- firebase deploy

  ```bash
  $ firebase deploy
  ```

<img width="776" alt="Screen Shot 2019-05-10 at 11 38 31 AM" src="https://user-images.githubusercontent.com/18046097/57498771-2e050100-7318-11e9-8192-2847d5552927.png">

- 해당 Hosting URL 로 접근하면 끝.

---

**ChatApp 완성코드**

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
	<script src="https://www.gstatic.com/firebasejs/5.8.4/firebase.js"></script>
	<script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
	<script src="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.js"></script>
	<link type="text/css" rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.css" />
	<script>
		// Initialize Firebase
		var config = {
			apiKey: "AIzaSyA6dK-btmSA_9fpN9zbvm8nWoA1rdLSBm0",
			databaseURL: "https://djpy2-chat-f5cf4.firebaseio.com/",
			projectId: "djpy2-chat-f5cf4",
			authDomain: "djpy2-chat-f5cf4.firebaseapp.com",
		};
		firebase.initializeApp(config)
	</script>

</head>

<body>
	<div id="app">
		<div v-if="currentUser.uid">
			<header>
				<span>Hello, {{ currentUser.displayName }}</span>
				<button @click="logout">LOGOUT</button>
			</header>
			<ul>
				<li v-for="message in messages">
					<b>{{ message.username }}</b> - {{ message.content }}
				</li>
			</ul>
			<div>
				<input type="text" v-model="newMessage" v-on:keyup.enter="createMessage">
				<button v-on:click="createMessage">></button>
			</div>
		</div>
		<div v-else>
			<div id="firebaseui-auth-container"></div>
		</div>
	</div>

	<script>
		const database = firebase.database()
		const auth = firebase.auth()
		const ui = new firebaseui.auth.AuthUI(auth)

		const app = new Vue({
			el: '#app',
			data: {
				newMessage: '',
				currentUser: {
					uid: '',
					email: '',
					displayName: '',
				},
			},
			firebase: {
				messages: database.ref('messages'),
			},
			mounted: function () {
				auth.onAuthStateChanged(user => {
					if (user) {
						// User is signed in.
						this.currentUser.uid = user.uid
						this.currentUser.email = user.email
						this.currentUser.displayName = user.displayName
					} else {
						// No user is signed in.
						this.initUi()
					}
				})
			},
			methods: {
				createMessage: function () {
					if (this.newMessage) {
						this.$firebaseRefs.messages.push({
							username: this.currentUser.displayName,
							content: this.newMessage,
						})
					}
					this.newMessage = ''
				},
				initUi: function () {
					ui.start('#firebaseui-auth-container', {
						signInOptions: [
							firebase.auth.EmailAuthProvider.PROVIDER_ID,
						],
						callbacks: {
							signInSuccessWithAuthResult: (authResult, redirectUrl) => {
								// User successfully signed in.
								// Return type determines whether we continue the redirect automatically
								// or whether we leave that to developer to handle.
								this.currentUser.uid = authResult.user.uid
								this.currentUser.email = authResult.user.email
								this.currentUser.displayName = authResult.user.displayName
								return false;
							},
						},
					})
				},
				logout: function () {
					this.currentUser = {
						uid: '',
						email: '',
						displayName: '',
					}
					auth.signOut()
						// after logout
						.then(() => {})
						.catch(error => console.log(error))
				}
			},
		})
	</script>
</body>

</html>

```

---



