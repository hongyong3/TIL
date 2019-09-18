# Final_Project

## Django_01

**Content**

[1. 목표](#1-목표)

[1. Django start](#1-django-start)

[2. MTV](#2-mtv)

[3. views-urls](#3-views-urls)

[4. Template](#4-template)

[5. Form](#5-form)

[6. Template Inheritance](#6-template-inheritance)



## 1. 목표

[TOC]



* 영화 추천 서비스 구현
* HTML/CSS, Javascript(Vue.js/Vanilla JS, etc), Django, Database 등을 활용한 실제 서비스 설계 
* Git을 통한 소스코드 버전 관리 및 협업 
* 서비스 배포 



## 2. 요구 사항

#### 1) *서비스 개요

* 본 프로젝트는 영화를 주제로 한 서비스를 구현하는 것으로, 영화 데이터베이스를 필수적으로 가지고 있어야 한다. (최소 등록된 영화 레코드 50개 이상) 
* 모바일 대응을 한 반응형 웹, Django REST API 서버 및 프론트엔드 프레임워크(Vue) 분리 등의 상세 구현 방식은 자유롭게 구성하되 프로젝트 README 상단에 구조도 혹은 설명을 명시한다. 
* 모든 프로젝트의 과정은 git을 통한 소스코드버전관리를 진행하며, Gitlab을 통하여 팀원 간 프로젝트 소스코드를 관리한다. 
* 다양한 기준으로 영화를 추천할 수 있는 기능은 반드시 구현하여야 하며, 부가적인 영화 커뮤니티에 필요한 기능 등을 자유롭게 추가할 수 있다.  (예 - 채팅 서비스, 커뮤니티 서비스, 화 관련 정보 아카이빙 서비스, 현재 박스오피스 정보 제공 등)
* 추천의 방식은 자유롭게 구성 가능하되 반드시 영화를 추천 받을 수 있어야 한다. 
* 사용자를 위한 최소한의 HTML/CSS를 통한 웹 사이트 디자인을 하여야 한다. 
* 완성된 서비스를 배포하고, 테스트 및 유지 보수를 진행한다. 

  4. 서비스 아키텍처  본 모델링은 최소한의 기준의 예시이며, 추가적인 필드 선언 및 모델링은 가능하다. 다만, 변경시 사전에 데이터베이스 모델링을 미리 팀원들과 협의하여 정한다. 



#### 2) *필수 기능 

* 관리자 권한의 유저만 영화 등록 및 수정 / 삭제 권한을 가진다.  (별도의 관리자 권한의 뷰가 구성돼야 한다.)
* 관리자 권한의 유저는 유저 관리 (수정 / 삭제 권한)을 가진다. (별도의 관리자 권한의 뷰가 구성돼야 한다.) 
* 모든 로그인 된 유저는 영화에 대한 평점을 등록 / 수정 / 삭제 등을 할 수 있어야 한다. 
* 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 한다. 
* 데이터베이스에 기록되는 모든 정보는 유효성 검사를 진행해야 하며, 필요에 따라 해당하는 정보를 클라이언트 화면에 띄워줄 수 있어야 한다. 
* HTTP method와 상태 코드는 적절하게 반환되어야 하며, 필요에 따라 해당하는 에러 페이지도 구성을 할 수 있다.  
* 이외 추가적인 기능은 자유롭게 구성 가능. 



## 3. 팀원정보 및 업무분담

### 1) *프로젝트 구상

* ##### 구현 서비스 계획

* ##### 모델 설계

* ##### 데이터 크롤링

* ##### 데이터 로드

* ##### 서버 로직 및 URL 생성

* ##### 템플릿 설계

* ##### 디버깅



### 2) *팀원정보 및 업무분담

#### 1) 대전_2반 강혜리 

#### - 업무분담

* 모델링

  > 모델 설계

* 백엔드

  > accounts 및 movies app 로직 설계

* 프론트엔드

  > 템플릿 테마 선정, html파일 작성

* PPT 작성



#### 2) 대전_2반 최홍용

#### - 업무분담

* 데이터 크롤링

* 모델링

  > 모델 수정

* 프론트엔드 보조

  > html 파일 작성 보조

* README 작성



---

## 4. 목표 서비스 구현 및 실제 구현 정도

### 1) *목표 서비스



##### 									<img width="953" alt="목표서비스" src="https://user-images.githubusercontent.com/45934494/57837969-ce6a9200-77fe-11e9-9b6d-6481c0a4cedb.png">

##### 

### 2) *실제 구현 정도





## 5. 데이터베이스 모델링



#### 1) *데이터베이스 모델링

---

##### 1-1) *movies

##### *Movie

| 필드명       | 자료형  | 설명                          |
| ------------ | ------- | ----------------------------- |
| id           | Integer | Primary Key                   |
| title        | Text    | 영화명                        |
| poster_path  | Text    | 포스터 이미지 URL             |
| genres       | Integer | Genre의 Primary Key(id 값)    |
| overview     | Text    | 영화 소개                     |
| release_data | Text    | 영화 개봉일                   |
| directors    | Integer | Director의 Primary Key(id 값) |
| actors       | Integer | Actor의 Primary Key(id 값)    |



##### *Genre

| 필드명 | 자료형  | 설명        |
| ------ | ------- | ----------- |
| id     | Integer | Primary Key |
| name   | Text    | 장르 구분   |

 

##### *Actor

| 필드명 | 자료형  | 설명                   |
| ------ | ------- | ---------------------- |
| id     | Integer | Primary Key            |
| name   | Text    | 배우 이름              |
| img    | Text    | 배우 프로필 이미지 URL |



##### *Director

| 필드명  | 자료형  | 설명                   |
| ------- | ------- | ---------------------- |
| id      | Integer | 평점                   |
| content | Text    | 한줄평                 |
| movie   | Integer | 배우 프로필 이미지 URL |



##### *Review

| 필드명      | 자료형  | 설명                       |
| ----------- | ------- | -------------------------- |
| id          | Integer | Primary Key                |
| score       | Integer | 평점                       |
| poster_path | Text    | 포스터 이미지 URL          |
| genres      | Integer | Movie의 Primary Key(id 값) |



##### 1-2) *테이블 관계

- Movie : Director = `M : N` 관계
- Movie : Actor = `M : N` 관계
- Movie : Genre = `M : N` 관계
- Movie : Review = `1 : N` 관계



##### 1-3) *모델링



<img width="517" alt="models_movie" src="https://user-images.githubusercontent.com/45934494/57770619-ae2dcb00-774b-11e9-93b3-6a632230a56f.PNG">



------



##### 2-1) *accounts

##### *Profile

| 필드명       | 자료형  | 설명                      |
| ------------ | ------- | ------------------------- |
| id           | Integer | Primary Key               |
| user         | Integer | User의 Primary Key(id 값) |
| nickname     | String  | 닉네임                    |
| introduction | Text    | 자기소개                  |



##### *User

| 필드명 | 자료형  | 설명        |
| ------ | ------- | ----------- |
| id     | Integer | Primary Key |
| name   | Text    | User의 이름 |



##### 2-2) *테이블 관계

- User : Profile = `1 : 1` 관계
- User : User= `M : N` 관계
- User : Director= `M : N` 관계
- User : Actor= `M : N` 관계
- User : Review= `1 : N` 관계



##### 2-3) *모델링



<img width="571" alt="models_accounts" src="https://user-images.githubusercontent.com/45934494/57770620-aec66180-774b-11e9-89d8-9160115127ee.PNG">



---



#### 2) *ERD 관계도



<img width="1031" alt="ERD" src="https://user-images.githubusercontent.com/45934494/57823310-f5f73580-77d1-11e9-90d3-5b904386d049.PNG">



------



## 6. 핵심 기능

### 1) *Crawling

#### 1-1) *크롤링 사전 작업

* API 키 발급

  > The movie db(TMDB)의 api를 이용할 예정`api.themoviedb.org`
  >
  > TMDB 회원가입 후 `<https://www.themoviedb.org/settings/api>`에서 API 키를 발급

* `<https://developers.themoviedb.org/3/movies/get-movie-details>`로 이동

* 인기 상영작을 크롤링하기 위해서 `popular`로 이동

* `https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=ko-kr&page=1`

  > * API키
  > * language : ko-kr
  > * page 수 설정

* jupyter notebook을 사용

  > `pip install jupyter`



#### 1-2) *크롤링

##### 1-2-1) *`genre.json`

#####  *코드

```python
#  genres.json

conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
dataObject = []
conn.request("GET", "/3/genre/movie/list?language=ko-kr&api_key=<<api_key>>", payload)
res = conn.getresponse()
data = json.loads(res.read())
for j in range(len(data['genres'])):
    dataDetail = {}
    dataDetail['pk'] = data['genres'][j]['id']
    dataDetail['model'] = 'movies.Genre'
    dataDetail['fields'] = {
        'name': data['genres'][j]['name']
    }
    dataObject.append(dataDetail)

with open('genre.json', 'w', encoding='utf-8') as f:
    json.dump(dataObject, f, ensure_ascii=False, indent=4)
```



##### *완성된 `genre.json`



<img width="263" alt="genre" src="https://user-images.githubusercontent.com/45934494/57683953-b6b0d380-766f-11e9-9506-b6b0b36ff609.PNG">



- pk : genre id 값
- model : movies의 Genre 모델
- name : 장르 이름



------



##### 1-2-2) *`movies.json`

##### *코드

```python
#  movie.json

conn = http.client.HTTPSConnection("api.themoviedb.org")
dataObject = []
k = 0
payload = "{}"
for i in range(1):
    conn.request("GET", "/3/movie/popular?page="+f"{i+1}"+"&language=ko-kr&api_key=<<api_key>>", payload)
    res = conn.getresponse()
    data = json.loads(res.read())
    for j in range(len(data['results'])):
        k += 1
        dataDetail = {}
        dataDetail['model'] = 'movies.Movie'
        dataDetail['pk'] = k
        dataDetail['fields'] = {
            'movie_id': data['results'][j]['id'],
            'title': data['results'][j]['title'],
            'poster_path': data['results'][j]['poster_path'],
            'overview': data['results'][j]['overview'],
            'release_date': data['results'][j]['release_date'],
            'genres': data['results'][j]['genre_ids'],
            'directors': [],
            'actors': [],
        }
        dataObject.append(dataDetail)
    
with open('movie.json', 'w', encoding='utf-8') as f:
        json.dump(dataObject, f, ensure_ascii=False, indent=4)
```



##### *완성된 `movie.json`



<img width="1037" alt="movie_json" src="https://user-images.githubusercontent.com/45934494/57769144-1f6b7f00-7748-11e9-8a91-c2b0eb96e894.PNG">





- model : django의 movies의 Movie 모델

- pk : 영화의 번호(1~400)

- fields

  > movie_id : 영화 ID 값
  >
  > title : 영화명
  >
  > poster_path : 포스터 이미지 URL
  >
  > overview : 영화 소개
  >
  > release_date :  영화 개봉일
  >
  > genres : genre의 ID 값
  >
  > directors : Director의 ID 값
  >
  > actors : Director의 ID 값



------



##### 1-2-3) *`actor.json`

##### *사전 작업

- movie의 ID 값을 가져오기

  > 배우의 데이터를 크롤링하기 위해선 
  >
  > `https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>` 에
  >
  > send request를  보내야 한다. 이를 위해서  `movie_id`를 집어 넣기 위해 for문을 사용했다.

```python
movie_id = []
for i in range(len(dataObject)):
    movie_id.append(dataObject[i]['fields']['movie_id'])
```

- 3명의 배우를 뽑기

```python
for j in range(min(3, len(data['cast']))):
    # min을 통해 for 문이 3번(배우가 3명) or 배우가 3명 이하면 그 수만큼 동작
```



##### *코드

```python
#  actor.json

conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
dataObject = []

for i in movie_id:
    conn.request("GET", "/3/movie/"+f"{i}"+"/credits?api_key=<<api_key>>", payload)
    res = conn.getresponse()
    data = json.loads(res.read())
    for j in range(min(3, len(data['cast']))):
        dataDetail = {}
        dataDetail['pk'] = data['cast'][j]['id']
        dataDetail['model'] = 'movies.Actor'
        dataDetail['fields'] = {
            'name': data['cast'][j]['name'],
            'img': data['cast'][j]['profile_path'],
        }
        dataObject.append(dataDetail)

    with open('actor.json', 'w', encoding='utf-8') as f:
        json.dump(dataObject, f, ensure_ascii=False, indent=4)
```



##### *완성된 `actor.json`



<img width="326" alt="actor_json" src="https://user-images.githubusercontent.com/45934494/57770016-4d51c300-774a-11e9-9d8e-32170bab6d66.PNG">

- pk : 배우의 pk 값

- model : movies의 Actor 모델

- field

  > name : 배우 이름
  >
  > img : 배우 이미지





------



##### 1-2-4) * `director.json`

##### * 사전 작업

- movie의 ID 값을 가져오기

  > 감독의 데이터를 크롤링하기 위해선 
  >
  > `https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>` 에
  >
  > send request를  보내야 한다. 이를 위해서  `movie_id`를 집어 넣기 위해 for문을 사용했다.

```python
movie_id = []
for i in range(len(dataObject)):
    movie_id.append(dataObject[i]['fields']['movie_id'])
```



##### * 코드

- director는 data의 'crew' 라는 리스트에서 `job == Director`를 통해서 접근.

```python
#  director.json

conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
dataObject = []


for i in movie_id:
    conn.request("GET", "/3/movie/"+f"{i}"+"/credits?api_key=<<api_key>>", payload)
    res = conn.getresponse()
    data = json.loads(res.read())
    
    if 'crew' in data:
        for j in range(len(data['crew'])):
            if data['crew'][j]['job'] == 'Director':
                dataDetail = {}
                dataDetail['pk'] = data['crew'][j]['id']
                dataDetail['model'] = 'movies.Director'
                dataDetail['fields'] = {
                    'name': data['crew'][j]['name'],
                    'img': data['crew'][j]['profile_path'],
                }
                dataObject.append(dataDetail)
    else:
        continue
            
    with open('director.json', 'w', encoding='utf-8') as f:
        json.dump(dataObject, f, ensure_ascii=False, indent=4)
```



##### * 완성된 `director.json`



<img width="335" alt="director_json" src="https://user-images.githubusercontent.com/45934494/57770014-4d51c300-774a-11e9-90d6-ac9cfc70a313.PNG">



- pk : 감독의 pk 값

- model : movies의 Director 모델

- field

  > name : 감독 이름
  >
  > img : 감독 이미지



##### 1-2-5) * movie.json에 actor_id 값 // director_id 값 넣기

##### *코드

```javascript
let actors = require('./actor1441.json');
let movies = require('./movie2.json');
let directors = require('./director1441.json');

for (let i =0; i < movies.length; i++) {
    let movie =  movies[i];
    let movie_id = movie.fields.movie_id
    actors.forEach(function(actor, index) {
         let actormovie_id = actor.fields.movies
         if (actormovie_id === movie_id) {
             movie.fields.actors.push(actor.pk);
         }
    })
}
for (let i =0; i < movies.length; i++) {
    let movie =  movies[i];
    let movie_id = movie.fields.movie_id
    directors.forEach(function(actor, index) {
         let actormovie_id = actor.fields.movies
         if (actormovie_id === movie_id) {
             movie.fields.directors.push(actor.pk);
         }
    })
}
movies.forEach(function(movie) {
    delete movie.fields.movie_id;
})
const fs = require('fs');

let data = JSON.stringify(movies);
fs.writeFileSync('movieresult.json', data);
```



##### * 최종 완성된 movie.json



<img width="503" alt="movie_final_json" src="https://user-images.githubusercontent.com/45934494/57770395-2d6ecf00-774b-11e9-9455-22f145d3b007.PNG">





#### 1-2-6) *Django에 loaddata - Json 파일 넣기

* `movie.json`, `actor.json`, `director.json`, `genre.json`을 `movies/fixtures/ `디렉토리로 옮긴다. 

  ```
  $ python manage.py loaddata genre.json
  Installed 19 object(s) from 1 fixture(s)
  $ python manage.py loaddata actor.json
  Installed 854 object(s) from 1 fixture(s)
  $ python manage.py loaddata director.json
  Installed 342 object(s) from 1 fixture(s)
  $ python manage.py loaddata actor.json
  Installed 400 object(s) from 1 fixture(s)
  ```



* admin.py`에 `Genre`, `Movie`, `Actor`, `Director`클래스를 등록한 후, `/admin`을 통해 실제로 데이터베이스에 반영되었는지 확인.



##### * movie.json

<img width="833" alt="movies" src="https://user-images.githubusercontent.com/45934494/57792461-0380d100-777a-11e9-848f-a509e52267df.PNG">



---



##### * actor.json

<img width="719" alt="actors" src="https://user-images.githubusercontent.com/45934494/57792462-0380d100-777a-11e9-94fd-4e0468e06126.PNG">



---



##### * director.json

<img width="751" alt="directors" src="https://user-images.githubusercontent.com/45934494/57792463-0380d100-777a-11e9-8ff2-14925c35ff4e.PNG">



---



##### * genre.json

<img width="835" alt="genres" src="https://user-images.githubusercontent.com/45934494/57792464-04196780-777a-11e9-995f-f780ef43ec25.PNG">



---

### 2) * static



## 7. 느낀점

### 대전_2반 강혜리 

* ##### 이번 프로젝트를 진행하면서 사전에 프로젝트를 어떻게 진행할 것인가, 어떤방식을 사용하여 프로젝트를 구상할 것인가와 같은 사전 계획을 세우는게 중요하다고 느꼈다.

* ##### 어떻게 보면 첫 팀프로젝트인데 잘해야겠다는 책임감을 많이 느꼈고, 협업을 통해 프로젝트를 진행하기 때문에 커뮤니케이션이 많이 중요하다는 것을 알게 됐다.



### 대전_2반 최홍용

* ##### 혼자가 아닌 둘이 하는 프로젝트를 진행하면서 책임감을 많이 가져 팀원에게 폐가 되지 않도록 열심히 노력했다. 

* ##### 프로젝트의 명세에 나와있듯이 협업과 의사소통의 중요성을 다시 한번 느낄 수 있었고, 나 자신의 장단점을 알아볼 수 있었다. 이번 프로젝트를 계기로 앞으로 2학기에 진행 할 프로젝트에서 더욱 발전된 모습을 보이도록 하겠다.