[TOC]

## Deploy with Heroku

> https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Deployment
>
> https://devcenter.heroku.com/articles/django-app-configuration
>
> https://devcenter.heroku.com/articles/python-gunicorn
>
> https://dgkim5360.tistory.com/entry/deploy-django-project-on-heroku

---

### 1. 사전 준비

> [배포 전 체크리스트](https://docs.djangoproject.com/ko/2.1/howto/deployment/checklist/)

#### 1.1 github 레퍼지토리 생성

- Heroku는 **git** 형상관리 시스템과 밀접하게 통합되어있는데, git을 이용하여 활성화된 시스템에 수정사항의 업로드 및 동기화를 수행한다.
- git push 까지 진행한다.

`.gitignore` **주의사항**

- **반드시 목록에서 `db.sqlite3` 를 삭제 해야한다.**

#### 1.2 보안 설정

> 환경변수에 보안정보를 등록해서 로딩하도록 한다.

- `DEBUG`

  - `~/.bashrc` (c9 기준) 에 다음과 같이 추가한다.

    ```bash
    export DJANGO_DEBUG=''
    ```

  - `settings.py`

    ```python
    # SECURITY WARNING: don't run with debug turned on in production!
    # DEBUG = True
    DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
    ```

- `SECRET_KEY`

  > [django-secret-key-generator](https://www.miniwebtool.com/django-secret-key-generator/)

  - `~/.bashrc` (c9 기준) 에 다음과 같이 추가한다.

    ```bash
    export DJANGO_SECRET_KEY='%idjsksn....qwqi{s2]as'
    ```

  - `settings.py`

    ```python
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
    ```
    
    ```bash
    $ source ~/.bashrc
    ```

- 배포 전 체크리스트 확인

  ```bash
  $ python manage.py check --deploy
  ```

  > 여러 이슈가 출력되겠지만 현재까지의 설정으로도 충분하다. 자세한건 [배포 전 체크리스트](https://docs.djangoproject.com/ko/2.1/howto/deployment/checklist/) 를 참고한다.

---

### 2. Settings for Staticfiles

> https://docs.djangoproject.com/ko/2.1/howto/static-files/
>
> https://devcenter.heroku.com/articles/django-assets
>
> [정적 파일 배포하기](https://docs.djangoproject.com/ko/2.1/howto/static-files/deployment/)

- `STATIC_ROOT`
  - Django의 "collectstatic" 도구로 템플릿에서 참조하는 모든 정적 파일을 모집하는 디렉토리로 가는 절대 경로이다. 일단 수집되면, 이것들은 파일이 어떤곳에서 호스팅되든지 단체로 업로드 될 수 있다.
  - Django 웹 어플리케이션으로부터 분리하여 정적파일을 쉽게 호스팅하기 위해, Django는 개발용 정적 파일을 수집하는 collectstatic 도구를 제공한다.
  - heroku에서 정적 파일은 django와는 독립적으로 gunicorn 을 통해서 제공할 것이기 때문에 django 프로젝트 폴더가 아닌, settings.py와 wsgi 파일이 있는 폴더에서 정적 파일 폴더를 다룬다. 

```python
# settings.py

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# (각자 프로젝트에 따라 추가 선택사항)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

---

### 3. django_heroku

> `django-heroku` automatically configures our Django application to work on Heroku

```bash
$ pip install django-heroku
```

- PostgreSQL (Mac OS)

  ```bash
  $ brew install postgresql
  ```

```python
# settings.py
import django_heroku

...

# Activate Django-Heroku.
django_heroku.settings(locals())
```

---

### 4. Create Heroku related files

> - **runtime.txt**: 프로그래밍 언어와 사용 버전.
> - **requirements.txt**: Django를 포함한 파이썬 관련 라이브러리 의존성.
> - **Procfile**: 웹 어플리케이션을 구동하기 위해 실행되어야 하는 프로세스의 목록. 장고의 예를 들자면, Gunicorn 웹 어플리케이션 서버( .wsgi 스크립트와 함께) 가 될것이다.  
> - **wsgi.py**: Heroku 환경에서 Django 어플리케이션을 호출 하기 위한 [WSGI](http://wsgi.readthedocs.io/en/latest/what.html) 설정.

#### 4.1 Procfile

- `Procfile` 생성(확장자 없이) 후 아래 내용 작성

  ```
  web: gunicorn [현재 장고 프로젝트 이름].wsgi
  ```

#### 4.2 Gunicorn

>  Django와 함께 사용되는 용도로 Heroku에서 추천되는 HTTP server 

```bash
$ pip install gunicorn
```

#### 4.3 Requirements

> Heroku는 환경을 재구성할 때 requirements.txt 에 패키지들을 자동적으로 설치한다.

```bash
$ pip freeze > requirements.txt
```

#### 4.4 Runtime

> 현재 프로젝트가 사용중인 python 버전을 입력한다.

- runtime.txt

```bash
python-3.6.8
```

- github 에 변경사항을 저장(push)

---

### 5. Deploy

- login

  ```bash
  $ heroku login
  ```

- create app

  > app_name 을 입력하지 않을 경우 랜덤으로 만들어 준다.

  ```bash
  $ heroku create [app_name]
  ```

- push to heroku

  ```bash
  $ git add .
  $ git commit -m ".."
  $ git push heroku master
  ```

  > 여기서, `heroku does not appear to be a git repository` 에러가 발생한다면 현재 프로젝트가 github 에 올라가 있지 않아서이다. github 에 올리지 않은 상태로 진행하고 싶다면 아래 명령어를 입력 후 다시 진행한다.
  >
  > ```bash
  > $ heroku git:remote -a [your_app_name]
  > ```

- migrate

  ```bash
  $ heroku run python manage.py migrate
  ```

- loaddata json

  ```bash
  # loaddata 가 필요한 경우 진행
  $ heroku run python manage.py loaddata example.json
  ```

- admin

  ```bash
  $ heroku run python manage.py createsuperuser
  ```

- open

  ```bash
  $ heroku open
  ```

---

### 6. static(optional)

```python
# 프로젝트/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---
