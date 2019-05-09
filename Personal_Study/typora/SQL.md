# SQL

### c9 sqlite 켜기(bash)

```
$ sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
```

### CREATE

- AUTOINCREMENT 는 INTEGER에서만 사용 가능. ( INT도 안됨! )

### ALTER TABLE

1. Rename Table

```
ALTER TABLE friends 
RENAME TO new_table_name;
```

1. Add new column to Table

```
ALTER TABLE friends ADD COLUMN married INTEGER;
```

# ORM

- Object-Relational Mapping

- 번역기라고 생각하면 된다.

- 프로그래밍 언어와 데이터베이스 사이에서 통역기능을 한다.

- 장점:

  - 객체지향적인 코드로 인해 직관적이고 비즈니스로직에 더 집중할 수 있게 한다.
  - 재사용과 유지보수가 편리해진다.
  - DB에 대한 종속성이 줄어든다.

- 단점:

  - 오로지 ORM으로만은 거대한 서비스를 구현하기 어렵다.
  - 어느정도의 속도 저하가 있다.

  ## 실습

  - 모듈 설치 하기

    pip install flask_sqlalchemy

    pip install flask_migrate

**객체화를 위해 파일을 두개로 쪼개기**

> app.py

```
# pip install flask_sqlalchemy
# pip install flask_migrate

from flask import Flask
from flask_migrate import Migrate
from models import db, User


app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정, 
# 'SQLALCHEMY_DATABASE_URI'는 고정값,  'sqlite:///db_flask.sqlite3'는 달라도 됨.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3' 
# True가 기본값, True일 경우 sqlalchemy 데이터베이스 객체 수정 및 신호방출 등을 추적.
# ---> 과도한 메모리를 사용.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)
```

> models.py

```
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#table 만들기
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>" 
    
# CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     username TEXT,
#     email TEXT
# );
```

**flask에서 작업하기**

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

​	--> 폴더 내에 migrations폴더와 db_flask.sqlite3 파일이 생성됨.

### CREATE

```
INSERT INTO users()
(flask-venv) sshyeri:~/workspace/orm $ python
Python 3.6.7 (default, Jan 30 2019, 06:16:48) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import *
>>> user = User(username='junho', email='example@gmail.com')
>>> db.session.add(user)
>>> db.session.commit()
>>> user.username
'junho'
>>> user.email
'example@gmail.com'
```

### READ

```
SELECT * FROM users;
SELECT * FROM users WHERE username = 'junho';
SELECT * FROM users WHERE username = 'junho' LIMIT 1;
>>> users = User.query.all()
>>> users = User.query.filter_by(username='junho').all()
>>> users = User.query.filter_by(username='junho').first()
```

### None

```
>>> miss = User.query.filter_by(username='ssafy').first()
```

### Get one by id

- PK만 GET으로 가져올 수 있음.

```
SELECT * FROM users WHERE id=1;
>>> user = user.query.get(1)
```

### LIKE

```
>>> users = User.query.filter(User.email.like('%exam%')).all()
>>> users = User.query.limit(1).offset(2).all()
```

### UPDATE

```
>>> user = User.query.get(1)
>>> user.username = 'ssafy'
>>> db.session.commit()
>>> user.username
'ssafy'
```

### DELETE

```
>>> user = User.query.get(1)
>>> db.session.delete(user)
>>> db.session.commit()
```