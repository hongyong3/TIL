# 1. settings.py

- template의 os.path.join(BASE_DIR, 'practice', 'template') 제거 (난이도 - 상)

  현재 모든 앱의 template에서 상속받는 `base.html`은 프로젝트 폴더 내부의 templates에 존재한다. 단, 프로젝트 폴더는 명시적으로 지정하지 않으면 장고에서 접근하지 못한다. 따라서 `settings.py`의 `DIR`에 다음과 같이 명시하여야한다. 

  ```
  'DIRS': [os.path.join(BASE_DIR, 'practice', 'templates')],
  ```

  

- accounts 앱 등록 제거 (난이도 - 하)

  accounts 앱이 등록되어있지 않으면 장고에서 접근할 수 없다.

  `INSTALLED_APPS`에 다음과 같이 `accounts`앱을 등록하여야한다.

  ```'accounts.apps.AccountsConfig'```

# 2. boards app

- redirect import 제거 (난이도 - 하)

- CommentForm에서 fields를 field로 변경 (난이도 - 중)

  CommentForm에서 field를 fields로 변경

  원래 fields로 등록해야한다.

- form.html에서 {% load bootstrap4 %} 제거 (난이도 - 상)

  현재 bootstrap_form을 사용하고 있으므로 반드시 {% load bootstrap4 %}를 해주어야 에러없이 사용할 수 있다.

- list.html에서 boards 목록 제거 (난이도 - 중)

  list.html 템플릿에서 boards를 보여주는 코드 작성 필요

  ```html
  {% for board in boards %}
  <div class="board">
      <h1><a href="{% url 'boards:detail' board.id %}">{{ board.title }}</a></h1>
      <p>{{ board.content }}</p>
  </div>
  {% endfor %}
  ```

  

- create에서 context로 넘기는 'form' 이름 변경 (난이도 - 중)

  form과 관련된 모든 view는 form.html에 렌더링된다. 이 때, form.html에서는 `form`이라는 이름으로 form을 받고 있기 때문에 create 뷰함수의 `create_form`을 `form`으로 바꿔주어야한다.

- comment 생성시 user와 board 등록 제거 (난이도 - 상)

  comment는 user와 board를 foreign key로 가지므로 save전에 반드시 두 정보를 등록한후 save()해야한다.

  ```python
  board = get_object_or_404(Board, pk=board_pk)
  ...
  if comment_form.is_valid():
  	comment = comment_form.save()
      comment.user = request.user
      comment.board = board
      comment.save()
  ...
  ```

- url variable과 view에서 받는 variable 이름이 다른 경우 (detail path의 board_pk를 pk로 변경) (난이도 - 상)

  url variable과 view 파라미터 이름을 맞춰주어야한다.

# 3. accounts app

- urls.py의 urlpatterns 를 urlpattern으로 이름 오타 (난이도 - 상)

  django에서 request를 탐색할 때 urls.py를 탐색하여 매칭되는 path에 해당하는 view함수에 요청을 보내게 되는데 이때 `urlpatterns`에 해당하는 변수에 있는 path를 검사한다. 때문에 `urlpatterns`가 없다면 순환 참조 오류가 나타나게된다. (`아마도`)

- 로그아웃이 안되는 문제 (난이도 - 하)

  logout 함수에 `auth_logout(request)`코드를 의도적으로 빠트려 로그아웃이 안되도록 만듬



> - 난이도는 지극히 주관적입니다.

> - 해설을 달아놨지만 제가 공부한 내용에서 달아놓은 해설이기 때문에 잘못된 정보일 수도 있습니다. 만약 잘못된 정보라면 알려주세요 ^^7
> - 모두들 화이팅 ~.~