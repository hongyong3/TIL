# Django 월말평가 가이드 

준호쌤과 타키쌤 청문회를 통해 수집한 빅데이터를 기반으로 추측한 내용입니다.



## 🙆🏻‍♀️나옵니다

- 건드려야할 파일
  - views.py, templates, forms.py, (불확실 : admin.py)
- accounts
  - 회원가입, 로그인, 로그아웃
  - 유저의 상태 (로그인 or 로그아웃) 에 따라 분기
- posts
  - CRUD
  - post.user == user 비교 (글 쓴 사람만 삭제 가능)
  - 좋아요 구현 ( + {{ post.like_users.count }} 명이 좋아합니다, 이 글을 좋아요한 유저 목록 for문 )
- 기타
  - 데코레이터
  - from ~ import ~



## 🙅🏻‍♀️안나와요

- 건드리지 말아야 할 파일
  - urls.py, models.py, settings.py 를 비롯한 기타 모든 파일
- 회원수정, 탈퇴, 비밀번호변경
- 이미지 업로드
- 유저 확장
- 팔로우



