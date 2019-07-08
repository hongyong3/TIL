[TOC]

## Vue_with_Django

**Content**

0. Vue Client
1. Music list
2. Comment Set
3. Comment Create
4. Comment Delete

> 2019.05.09 Thu

---

### 0. Vue Client

> Django_13_REST_API(music) 수업 에서 구현했었던 프로젝트를 그대로 복사해서 복사본으로 진행한다.
>
> django 는 c9 에서, vue 는 로컬에서 진행한다.

- `vue-client.html` 파일을 만들고 mounted 를 추가해서 화면이 렌더링 될 때마다 axios 로 요청을 보내보자.

- 요청을 보내는 중에는 django 서버가 켜져 있어야한다.

  - 요청이 실패했을 때, 최대한 에러 메시지를 많이 봐서 디버깅 할 수 있도록 `.catch` 를 항상 붙이자.

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
  	</div>
  	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  	<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  	<script>
  		const app = new Vue({
  			el: '#app',
  			data: {
  				musics: [],
  			},
  			mounted: function () {
  				axios.get('https://materials-capollux.c9users.io/api/v1/musics/')
  					.then(response => console.log(response.data))
  					.catch(error => console.log(error))
  			}
  		})
  	</script>
  </body>
  </html>
  ```

- 그런데 콘솔을 보면 아래와 같은 에러가 난다.

<img width="687" alt="Screen Shot 2019-05-09 at 5 04 22 PM" src="https://user-images.githubusercontent.com/18046097/57437375-9bfbea80-727c-11e9-9fbd-690376181137.png">

- CORS 정책 때문에 막혔다고 한다.

> **CORS**
>
> - Cross-Origin Resource Sharing
>   - https://developer.mozilla.org/ko/docs/Web/HTTP/Access_control_CORS)
>   - HTTP 요청은 기본적으로 Cross-Site HTTP Requests 가 가능하다.
>     다시 말하면, `<img>` 태그로 다른 도메인의 이미지 파일을 가져오거나, `<link>` 태그로 다른 도메인의 CSS를 가져오거나, `<script>` 태그로 다른 도메인의 JavaScript 라이브러리를 가져오는 것이 모두 가능하다.
>   - 하지만 `<script></script>`로 둘러싸여 있는 **스크립트**에서 생성된 Cross-Site HTTP Requests는 **[Same Origin Policy](https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy)**를 적용 받기 때문에 Cross-Site HTTP Requests가 불가능하다.
>   - AJAX가 널리 사용되면서 `<script></script>`로 둘러싸여 있는 스크립트에서 생성되는 `XMLHttpRequest`에 대해서도 Cross-Site HTTP Requests가 가능해야 한다는 요구가 늘어나자 W3C에서 CORS라는 이름의 권고안이 나오게 되었다.
> - django는 C9, Vue는 local로 서로 다른 도메인에서 돌아가고 있기 때문에 서로 데이터를 주고 받으려면 CORS 설정을 해주어야 한다.

#### 0.1 CORS setting

> https://github.com/ottoyiu/django-cors-headers/

- install

  ```bash
  $ pip install django-cors-headers
  ```

- settings

  ```python
  INSTALLED_APPS = (
      ...
      'corsheaders',
      ...
  )
  
  MIDDLEWARE = [
      ...
      'corsheaders.middleware.CorsMiddleware', # 위치 중요!
      'django.middleware.common.CommonMiddleware', # 얘 바로 위에 넣을 것!
      ...
  ]
  
  CORS_ORIGIN_ALLOW_ALL = True
  
  # Set Whitelist
  CORS_ORIGIN_WHITELIST = (
      'google.com',
      'hostname.example.com',
      'localhost:8000',
      '127.0.0.1:9000'
  )
  ```

---

### 1. Music List

- axios로 요청 보낸거 받아서 data musics 에 잘 할당해보자.

  ```html
  <div id="app">
  	<ul>
  		<li v-for="music in musics">
  			{{ music.artist }} - {{ music.title }}
  		</li>
  	</ul>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
  	const app = new Vue({
  		el: '#app',
  		data: {
  			musics: [],
  		},
  		methods: {
  			getMusics: function () {
  				axios.get('https://django-intro-wnsgh6315.c9users.io/api/v1/musics/')
  					.then(response => response.data)
  					.then(musics => {
  						this.musics = musics
  					})
  					.catch(error => console.log(error))
  			}
  		},
  		mounted: function () {
  			this.getMusics()
  		}
  	})
  </script>
  ```

- 데이터 응답을 잘 받아서 출력되지만 django에서 artist 를 숫자로 보내주고 있다.

- django 에서 숫자가 아닌 이름으로 보내줄 수 있도록 Serializer 를 수정해야한다.

  ```python
  # musics/serializers.py
  class MusicSerializer(serializers.ModelSerializer):
      artist_name = serializers.CharField(source='artist.name')
      class Meta:
          model = Music
          fields = ('id', 'title', 'artist_name',)
  ```

  ```html
  <div id="app">
  	<ul>
  		<li v-for="music in musics">
  			{{ music.artist_name }} - {{ music.title }}
  		</li>
  	</ul>
  </div>
  ```

---

### 2. Comment Set

- Music 에 달린 댓글도 같이 출력해보자.

  ```python
  # musics/serializers.py
  class MusicSerializer(serializers.ModelSerializer):
      artist_name = serializers.CharField(source='artist.name')
      comment_set = CommentSerializer(many=True)
      class Meta:
          model = Music
          fields = ('id', 'title', 'artist_name', 'comment_set',)
  ```

  > CommentSerializer 선언이 하단에 있기 때문에 MusicSerializer 보다 상단으로 옮겨야 한다.

- **(Vue devtools 또는 console.log로 넘어 오는 값을 중간중간 확인 할 것!)**
  ```html
  <div id="app">
  	<ul>
  		<li v-for="music in musics">
  			<div>
  				{{ music.artist_name }} - {{ music.title }}
  			</div>
  			<ul>
  				<li v-for="comment in music.comment_set">
  					{{ comment.content }}
  				</li>
  			</ul>
  		</li>
  	</ul>
  </div>
  ```

---

### 3. Comment Create

> [Array.prototype.map()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

- v-model로 양방향 데이터 바인딩 만들어야 하는데 form 이 여러개인 상황이다.

- 개수가 n개인데 다 직접 만들 수 없다! 따라서 music object에 ~~꼽사리~~ 끼자.

  ```javascript
  getMusics: function () {
  	axios.get('https://django-intro-wnsgh6315.c9users.io/api/v1/musics/')
  		.then(response => response.data)
  		.then(musics => {
  			this.musics = musics.map(music => {
  				return { ...music, newComment:'' }
  			})
  		})
  		.catch(error => console.log(error))
  }
  ```

- v-model 설정

  ```html
  <div id="app">
  	<ul>
  		<li v-for="music in musics">
  			<div>
  				{{ music.artist_name }} - {{ music.title }}
  			</div>
  			<ul>
  				<li v-for="comment in music.comment_set">
  					{{ comment.content }}
  				</li>
  			</ul>
  			<div>
  				<input type="text" v-model="music.newComment" @keyup.enter="addComment(music)">
  			</div>
  		</li>
  	</ul>
  </div>
  ```

- vue devtools 로 input 에 작성하는 값이 newComment 에 실시간 바인딩되는지 확인해야한다.

- 이제 댓글 작성 함수를 만들어보자.

  ```javascript
  addComment: function (music) {
  	axios.post(`https://django-intro-wnsgh6315.c9users.io/api/v1/musics/${music.id}/comments/`, {content: music.newComment})
  		.then(response => response.data)
  		.then(addedComment => {
  			music.comment_set.push(addedComment)
  			music.newComment = ''
  		})
  		.catch(error => console.log(error))
  },
  ```

  - 요청 보내는 주소에 music id가 필요함으로, 함수 호출시 넘겨주자.
  - musics array에서 우리가 댓글을 다는 music object 를 찾아와야 한다. 
  - 왜? 거기에 newComment 가 내부에 끼워져 있기 때문에, 값을 가져오기 위해서!

- 이제 댓글을 작성해서 실시간으로 업데이트 되는지 확인해보자.

---

### 4. Comment Delete

- 삭제 버튼을 먼저 만든다.

  ```html
  <li v-for="comment in music.comment_set">
  	{{ comment.content }} <button @click="deleteComment(music, comment)"> x </button>
  </li>
  ```

- 이어서 삭제하는 함수를 만든다.

  - 삭제는 music id 와 더불어 comment id 도 필요하다. 함수 호출 시 가져와야한다.

  - JS는 Array에서 특정 item 삭제가 다이렉트로 안되기 때문에, 삭제된 comment의 id 값을 가진 object 를 제외한 **새로운 array를 만들어서 재할당** 한다.

    ```javascript
    music.comment_set = music.comment_set.filter(c => {
      return c.id !== comment.id
    })
    ```

  ```javascript
  deleteComment: function (music, comment) {
  	axios.delete(`https://django-intro-wnsgh6315.c9users.io/api/v1/musics/${music.id}/comments/${comment.id}/`)
  		.then(response => {
  			music.comment_set = music.comment_set.filter(c => c.id !== comment.id)
  		})
  		.catch(error => console.log(error))
  }
  ```

---

**최종 코드**

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
	<ul>
		<li v-for="music in musics">
			<div>
				{{ music.artist_name }} - {{ music.title }}
			</div>
			<ul>
				<li v-for="comment in music.comment_set">
					{{ comment.content }} <button @click="deleteComment(music, comment)"> x </button>
				</li>
			</ul>
			<div>
				<input type="text" v-model="music.newComment" @keyup.enter="addComment(music)">
			</div>
		</li>
	</ul>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
	const app = new Vue({
		el: '#app',
		data: {
			musics: [],
		},
		methods: {
			getMusics: function () {
				axios.get('https://django-intro-wnsgh6315.c9users.io/api/v1/musics/')
					.then(response => response.data)
					.then(musics => {
						this.musics = musics.map(music => {
							return { ...music, newComment:'' }
						})
					})
					.catch(error => console.log(error))
			},
			addComment: function (music) {
				axios.post(`https://django-intro-wnsgh6315.c9users.io/api/v1/musics/${music.id}/comments/`, {content: music.newComment})
					.then(response => response.data)
					.then(addedComment => {
						music.comment_set.push(addedComment)
						music.newComment = ''
					})
					.catch(error => console.log(error))
			},
			deleteComment: function (music, comment) {
				axios.delete(`https://django-intro-wnsgh6315.c9users.io/api/v1/musics/${music.id}/comments/${comment.id}/`)
					.then(response => {
						music.comment_set = music.comment_set.filter(c => c.id !== comment.id)
					})
					.catch(error => console.log(error))
			}
		},
		mounted: function () {
			this.getMusics()
		}
	})
</script>
</body>

</html>
```



