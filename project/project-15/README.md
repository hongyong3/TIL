# 20200314

## Project

### Project - Diary App - [1]



#### [사전 지식]

* Node.js

  > 자바스크립트 언어를 활용하여 Customer와 Client가 하나로 구동이 가능한 언어.

* npm

  > 자바스크립트 프로그래밍 언어를 위한 패키지 관리자.

* Express.js

  > Node.js를 개발하기 편리하게 도와주는 웹 프레임워크.
  >
  > 사실상 Node.js의 표준 서버 프레임워크로 통하고 있음.

* MongoDB

  > 크로스 플랫폼 도큐먼트 지향 데이터베이스 시스템.
  >
  > JSON과 같은 동적 스키마형 도큐먼트들을 선호.
  >
  > Database의 일환으로 전통적인 테이블 기반의 관계형 Database가 아닌,
  >
  > JSON의 행(Row)으로 구성된 Database.

* Heroku

  > 웹 애플리케이션 배치 모델로 사용되는 여러 프로그래밍 언어(여기서는 Node.js)를 지원하는
  >
  > 클라우드 PaaS(Platform as a Service).



---



#### [준비 - 기본 설치 및 프로그램 셋팅]

##### (1) Node.js, npm, Git 로컬에 설치

* `Node.js`

  > <https://nodejs.org/ko/>

* `Git`

  > <https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98>

  

```bash
$ node -v
v12.13.0
$ npm -v
6.12.0
$ git --version
git version 2.21.0.windows.1
```



##### (2) Sourcetree 설치

* `Sourcetree`

  > *소스 관리하는 툴*
  >
  > <https://www.sourcetreeapp.com/>



##### (3) Heroku

* `Heroku`

  > https://www.heroku.com/	*회원가입*
  >
  > <https://devcenter.heroku.com/articles/heroku-cli#download-and-install>	*Heroku cli 설치*



##### (4) 소스 개발 IDE

* `IntelliJ IDEA Edu`	*Jetbrains*

  > <https://www.jetbrains.com/ko-kr/idea/download/#section=windows>



---



#### [시작]

##### (1) Heroku 로그인

```bash
$ heroku login	# 앱을 구동하기 위한 클라우드 환경인 '히로쿠'를 지금 이 컴퓨터에서 시작한다는 개념.
heroku: Press any key to open up the browser to login or q to exit:	# 아무키나 누르기
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/37a96f57-d45f-4c0e-9c11-fa852a882a98
heroku: Waiting for login...
Logging in... done
Logged in as chy66822495@gmail.com
```



##### (2) Heroku에서 샘플 앱 받기(소스)

```bash
# clone 할 디렉토리로 이동 후
$ git clone https://github.com/heroku/node-js-getting-started.git
$ cd node-js-getting-started	# 디렉토리로 이동
```



* 샘플 소스 트리

![1584267262245](C:\Users\yong_\AppData\Roaming\Typora\typora-user-images\1584267262245.png)



##### (3) heroku 사이트에 앱 만들기

```bash
$ heroku create diary-heroku
Creating diary-heroku... done
https://diary-heroku.herokuapp.com/ | https://git.heroku.com/diary-heroku.git

# 만약, 앱의 첫글자를 대문자, 숫자, -를 사용한다면, 에러 발생
$ heroku create Diary-heroku
Creating Diary-heroku... !
 !    Name must start with a letter, end with a letter or digit and can only
 !    contain lowercase letters, digits, and dashes.

# 만약, 똑같은 이름으로 앱을 만든다면, 에러 발생
$ heroku create diary-heroku
Creating diary-heroku... !
 !    Name diary-heroku is already taken
```



##### (4) 사이트 접속해보기

```bash
$ heroku open
```



---



# 20200315

## Project

### Project - Diary App - [2]



#### [사전 준비]

##### (1) 모듈 설치

```bash
# Mongoose 설치 : Node.js와 MongoDB를 연결해주는 모듈
$ npm install --save --save-exact mongoose

# body-parser 설치 : html 데이터 처리용 모듈
$ npm install body-parser --save
```



##### (2) mLab

* 회원가입 및 생성

  > <https://mlab.com/>
  >
  > -> 새로운 회원에게 `mLab`이 더이상 서비스 하지 않음...
  >
  > -> 학습 후 다시 진행.