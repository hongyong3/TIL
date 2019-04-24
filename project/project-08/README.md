# 20190322

## Project_08

### json data seed를 이용한 Django 1:N 모델 관계 구현 + Form class 사용

------



#### 1) 내용

##### 목표)

- ##### 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작

- ##### Seed Data를 활용한 DB 설계

- ##### Django Form을 통해 입력받은 데이터 유효성 검증

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

##### 모델)

* ##### 모델관계

  * Genre
    * 필 드 명 : id           	//	자 료 형 : Integer	// 설 명 : Primary Key
    * 필 드 명 : nane             //        자 료 형 : String          // 설 명 : 장르 구분

  

  * Movie

    * 필 드 명 : id	          //	자 료 형 : Integer	// 설 명 : Primary Key
    * 필 드 명 : title              //        자 료 형 : String          // 설 명 : 영화명
    * 필 드 명 : audience    //        자 료 형 : Integer        // 설 명 : 누적 관객수
    * 필 드 명 : poster_url  //        자 료 형 : String          // 설 명 : 포스터 이미지 URL
    * 필 드 명 : description//        자 료 형 : Text             // 설 명 : 영화 소개
    * 필 드 명 : genre_id    //         자 료 형 : Integer        // 설 명 : Genre의 Primary Key(id 값)

    

  * - Score
      - 필 드 명 : id	          //	자 료 형 : Integer	// 설 명 : Primary Key
      - 필 드 명 : content       //        자 료 형 : String          // 설 명 : 한줄평(평가 내용)
      - 필 드 명 : score           //        자 료 형 : Integer        // 설 명 : 평점
      - 필 드 명 : genre_id    //         자 료 형 : Integer        // 설 명 : Movie의 Primary Key(id 값)	



------

#### 2) 트리

```
.
├── db.sqlite3
├── manage.py
├── movies
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures
│   │   ├── genre.json
│   │   └── movie.json
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── templates
│   │   └── movies
│   │       ├── base.html
│   │       ├── detail.html
│   │       ├── form.html
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── project_08
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── settings.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   └── wsgi.cpython-36.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

9 directories, 35 files
```



------

##### movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()

##### score 테이블의 score 컬럼(score__score)의 평균(Avg)을 score_avg라는 새로운 컬럼으로 추가적으로 붙여서 (annotate) 모든 데이터의 결과를 받아 보겠다.

##### 종합평점을 {{ movie.score_avg|floatformat }}을 이용하여 소수점 첫째자리까지 출력