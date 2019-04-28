# Flask

## flask 실행

```
student@DESKTOP MINGW64 ~/Desktop/ssafy/Flask
$ code app.py
```

*flask.py 실행 금지*

**고정 픽!**

```
from flask import Flask
app = Flask(__name__)
```

## rendering html

- import render_template
- py파일 동일 위치에 templates폴더 생성
- templates폴더 내에 html파일 생성

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!!'

@app.route('/html')
def html():
    return render_template('chicken.html')
```

## 진자 조건문

```
@app.route("/dictionary/<string:word>")
def dictionary(word):
    word_dict = {'apple':'사과', 'banana':'바나나', 'orange':'오렌지', 'grape':'포도'}
    return render_template('dict.html', word = word, word_dict = word_dict)
```

-> html 파일에서

```
{% if word in word_dict %}
    <h1> {{word}}은(는) {{word_dict[word]}}!</h1>
{% else %}
    <h1> {{word}}은(는) 없는 단어입니다.</h1>
{% endif %}
```

## fake google(가짜 검색창 만들기)

- [https://www.google.com/search?q=iu로](https://www.google.com/search?q=iu%EB%A1%9C) 이동시 iu가 검색됨.
- text 입력 창을 q로 받아 action으로

```
<form action="https://www.google.com/search" method="get"> 
    <!--기본은 항상 get방식 없어도 무관.-->
	<input id="q" type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>
```

## Ping Pong

- ping에서 보낸 입력값을 pong에서 출력하기

### GET방식

```
from flask import Flask, render_template, request

@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
   # print(request.args)  >>>   ImmutableMultiDict([('p', 'ad')])
    p = request.args.get('p') #dict처럼 가져와서 get으로 value값을 가져옴.
    return render_template('pong.html',p=p)
```

ping.html

```
<form action="/pong">
        <input type="text" name="p"/>
        <input type="submit" value="Submit"/>
    </form>
```

pong.html

```
 <h1>{{p}}</h1>
```

### POST방식

- 받아온 값들이 주소창에 보여지지 않게.

```
@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')
    
@app.route("/pong_new", methods=['POST'])
def pong_new():
    #name = request.form['name']
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)
```

ping_new.html

```
<form action="/pong_new" method="POST">
        <input type="text" name="name"/>
        <input type="text" name="msg"/>
        <input type="submit" value="Submit"/>
 </form>
```

pong_new.html

```
 <h2>{{name}}이 {{msg}}를 보냈습니다.</h2>
```