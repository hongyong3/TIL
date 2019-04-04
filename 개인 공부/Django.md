# Django

## 0. 준비사항

#### 1. pyenv/python/pyenv-virtualenv 설치 및 설정

- python 3.6.7

  > [설치 및 설정 코드들](https://gist.github.com/edujunho/bee20c196ecacc3e8cdf068b4ec64d9f)

- git

  > ```
  > $ git init
  > $ git remote add origin master 깃 주소
  > $ git config --global user.name
  > $ git config --global user.mail
  > ```

#### 2. 가상환경 생성

```
$ pyenv virtualenv 3.6.7 django-venv
```

#### 3. 프로젝트 폴더 생성 및 이동

#### 4. local 가상환경 활성화

```
$ pyenv local django-venv
```

#### 5. 가상환경 해제

```
$ rm -rf .python-version 
```

#### 6. Django 설치

```
$ pip install django
$ pip install --upgrade pip
```

## 1. Django start

### 1.1 장고 프로젝트

#### 1. 프로젝트 생성

> django, test, class, django-(하이픈 들어가는 것들) 은 프로젝트 이름으로 사용하면 안됩니다.

```
$ django-admin startproject django_intro .
```

#### 2. 서버 실행

> ```
> $ python manage.py runserver $IP:$PORT
> ```
>
> `settings.py` 파일에서 변수 수정
>
> ```
> ALLOWED_HOST = ['*']
> ALLOWED_HOST = ['example-username.c9users.io']
> ```

#### 3. .gitignore 설정

> $touch .gitignore
>
> <https://gitignore.io/> 에 이동해 django/python....검색 후 전체 복사
>
> .gitignore 파일에 붙여넣기

#### 4. TIMEZONE/ LANGUAGE_CODE 설정

> `settings.py` 파일에서 변수 수정
>
> ```
> LANGUAGE_CODE = 'ko-kr'
> TIME_ZONE = 'Asia/Seoul'
> ```

#### 5. 로켓 페이지 한글화 확인

#### 6. 프로젝트 구조

`manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

`프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import할 수 있습니다.

`settings.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장합니다.

`__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일.

`urls.py` : 현재 장고 프로젝트의 URL 선언을 저장. 사이트의 URL과 VIEWS의 연결을 저장.

`wsgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점.

------

### 1.2 장고 어플리케이션(APP)

- 실제로 특정한 역할을 하는 친구가 바로 APP
- 프로젝트는 이러한 어플리케이션의 집합
- 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
- 각각의 어플리케이션은 MTV(Model-Template-View) 패턴으로 구성되어 있다.

#### 1. 어플리케이션 만들기

```
$ python manage.py startapp home
```

#### 2. 어플리케이션 구조

`admin.py` : 관리자용 페이지 커스터마이징 장소

`apps.py` : 앱의 정보가 있는 곳. 우리는 수정할 일이 없습니다.

`models.py` : 앱에서 사용하는 Model을 정의하는 곳

`tests.py` : 테스트 코드를 작성하는 곳

`views.py` : view들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳

#### 3. 어플리케이션 등록

> home > apps.py > class HomeConfig()
>
> `home.apps.HomeConfig` 등록
>
> 혹은 그냥 `home` 이라고 작성 가능. 다만, 후반부 자세한 설정 불가능

우리는 앞으로

1. views
2. urls
3. template 순으로 코드를 작성할 겁니다.
   - `HttpResponse()`로 첫 리턴 값 출력해보기
   - `path(**route**, **views**, name)` 2개의 필수인수와 1개의 선택인수
   - 저녁 메뉴 리턴 실습

#### 4. Template

- 장고에서 사용되는 템플릿은 DTL(Django Template Language)이다.
- Jinja2와 문법이 유사하지만 다르다.

##### 4.1 Template Variable

- render()
  - render(**request, template_name, context=None,** content_type=None, status=None, using=None)

##### 4.2 Variable Routing

```
def hello(request, name):
    return render(request, 'hello.html', {'name' : name})
```

#### 5. Form data(get / post)

request.GET.get('data')

request.POST.get('data')

{% csrf_token %}를 form 안에서 같이 보내줘야 합니다.

> csrf 공격과 같은 보안과 관련된 사항은 `settings.py` 내의 *MIDDLEWARE* 에 되어있다.
>
> 실제로 요청은 *MIDDLEWARE* 설정 사항들은 순차적으로 거친다. 응답은 아래에서 위로 거쳐서 응답이 리턴된다.

#### 5. Template Inheritance

home/templates/base.html 생성

```
베이스 코드 써보세요.
```

------

```
On_delete
```

c참조하는 부모객체가 사라졌을 때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다.

데이터베이스 무결성

1. 개체 무결성 : PK/NOT NULL/UNIQUE
   1. 식별자는 NULL일 수 없고 중복일 수 없다.
2. 참조 무결성 : FK/모든 외래 키의 값은 2가지 상태 가운데 하나에만 속함을 규정
3. 범위/도메인 무결성: 컬럼은 지정된 형식을 반드시 만족해야 된다.(CHAR, TEXT)

on_delete 속성 값

1. CASCADE: 부모객체가 삭제 됐을 때 이를 참조하는 객체도 삭제한다.
2. PROTECT: 참조가 되어있는 경우 삭제 오류 발생.
3. SET_NULL: 부모객체가 삭제 됐을 때 참조하는 모든 값을 NULL로 치환(NOT NULL조건 시 불가능)
4. SET_DEFAULT : 모든 값이 DEFAULT로 치환.
5. SET():특정 함수 호출
6. DO_NOTHING: 아무것도 하지 않음. 다만 SQL에서는 on_delete 직접 설정해줘야함.

게시글이 삭제되면 모든 댓글들의 값을 1로 바꾸겠다.