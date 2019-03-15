# 20190315

## Project_07

### csv 를 이용한 Django 1:N 모델 관계 구현

------



#### 1) 내용

##### 목표)

- ##### 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작

- ##### 데이터베이스 테이블간 관계 설정 (1:N)

##### 구현)

- ##### 데이터베이스 설계

  - APP
  - 영화목록
  - 영화 정보 조회
  - 영화 정보 삭제
  - 평점 생성
  - 평점 목록
  - 평점 삭제



------

#### 2) 트리

.
├── crud
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── genre.csv
├── manage.py
├── movie.csv
└── movies
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── admin.cpython-36.pyc
    │   ├── apps.cpython-36.pyc
    │   ├── models.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   └── views.cpython-36.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-36.pyc
    │       └── __init__.cpython-36.pyc
    ├── models.py
    ├── templates
    │   └── movies
    │       ├── base.html
    │       ├── detail.html
    │       └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py

8 directories, 32 files



------

##### movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()

##### score 테이블의 score 컬럼(score__score)의 평균(Avg)을 score_avg라는 새로운 컬럼으로 추가적으로 붙여서 (annotate) 모든 데이터의 결과를 받아 보겠다.