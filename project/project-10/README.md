# 20190419

## Project_10

### Django를 사용한 REST API server 구현



#### 1) 내용

##### 목표

* RESTful API 서버 구축

* Seed Data 반영

  * json 파일을 이용

  * ```
     $ python manage.py loaddata genre.json
     Installed 11 object(s) from 1 fixture(s) 
     $ python manage.py loaddata movie.json 
     Installed 10 object(s) from 1 fixture(s)
    ```

* get_swagger_view을 import하여 docs파일로 보기 편하게 만들기.





#### 2)  트리

```
.
├── boxoffice
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── movies
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── admin.cpython-36.pyc
    │   ├── apps.cpython-36.pyc
    │   ├── models.cpython-36.pyc
    │   ├── serializers.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   └── views.cpython-36.pyc
    ├── admin.py
    ├── apps.py
    ├── fixtures
    │   ├── genre.json
    │   └── movie.json
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-36.pyc
    │       └── __init__.cpython-36.pyc
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py

7 directories, 31 files
```



#### 3) Docs 결과

![docs](https://user-images.githubusercontent.com/45934494/56628145-a2d30c80-6683-11e9-81e1-8dd927b3fe85.PNG)