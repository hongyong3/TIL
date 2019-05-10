# 20190510

## Project_11

### Vue.js 를 통한 Single Page Application 구축.



#### 1) 내용

##### 1-1) 목표

* 데이터 요청
  * Django Rest Framework로 개발한 Django API 서버에서 RESTful 하게 요청을 보내고 JSON 응답
     받기.
  * API 에서 반드시 제공받아야 하는 정보는 장르정보, 영화정보, 리뷰정보.
  * 추가로 다른 데이터를 제공.

- RESTful API 서버 구축
- Seed Data 반영

  - 이전 프로젝트(Project-10)의 파일을 이용
-  mounted 를 추가해서 화면이 렌더링 될 때마다 axios 로 요청



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
├── movies
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── serializers.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures
│   │   ├── genre.json
│   │   └── movie.json
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt

7 directories, 32 files
```



#### 3) Vue 결과

##### 3-1) 영화 목록을 조회할 수 있는 UI

* 영화 제목
* 누적 관객
* 포스터 이미지 url
* 장르

![1](https://user-images.githubusercontent.com/45934494/57508122-a03b0d00-733b-11e9-87cd-c0d26602a8e4.png)



##### 3-2) 영화 상세 정보

* 설명
* 리뷰
  * 리뷰 데이터 갱신
* 평점
  * 평균 평점 갱신

![2](https://user-images.githubusercontent.com/45934494/57508123-a03b0d00-733b-11e9-8f31-8c0d30195cf5.png)

