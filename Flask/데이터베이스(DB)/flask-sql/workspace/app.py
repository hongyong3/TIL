from flask import Flask, render_template, request, redirect
import datetime
import os
import requests
import csv
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'
    

    
    
# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')
def dday():
    date_1 = datetime.datetime(2019, 5, 20)
    date_2 = datetime.datetime.now()
    td = date_1 - date_2
    return f'{td} 일 남았습니다.'
    

        
# variable routing
@app.route('/hi/<string:name>')
def hi(name):
    # return f'안녕, {name}'
    # greeting.html로 위처러 안녕 누구누구를 출력해주세요.
    return render_template("greeting.html", html_name=name)
    
    
    
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number} 의 세제곱은 : {number**3}'
    
    
# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)
    

# fake google
@app.route('/google/')
def google():
    return render_template('google.html')  # ping은 바로 pong으로 넘어가기 때문에 따로 parameter가 필요 없다.
    
#ping pong

@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    pingpong = request.args('ping') # 이것을 써도 되지만 에러를 확인하고 싶어서 아랫줄처럼 사용한다.
    pingpong = request.args.get('ping')  # flask에서는 .get('')로 dictionary처럼 받지만, list나 dict은 아니다.
    msg = request.args.get('msg')
    return render_template('pong.html', pingpong = pingpong, msg=msg)
    


@app.route('/ping_new')
def ping_new():
    return render_template('ping_new')


# @app.route('/pong_new', methods=['POST']) # methods=['POST']로 받는다.
# def ping_new():
#     pingpong = request.form.get('ping')
#     msg = request.form.get('msg')
#     return render_template('pong_new.html', pingpong=pingpong, msg=msg)
    
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)


# CSV
@app.route('/timeline')
def timeline():
    # username / message
    # 지금까지 기록되어있는 방명록들을 보여주자!
    # DictReader
    with open('timeline.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        um_dict = dict()
        for row in reader:
            um_dict.update({row['username'] : row['message']})
        return render_template('timeline.html', um_dict=um_dict)
        
        
        # 선생님 풀이 
        #timelines = []
        #with open('timeline.csv', 'r', newline='') as csvfile:
        #for row in reader:
            #timelines.append(row)
        #return render_template('timeline.html',timelines=timelines )

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    with open('timeline.csv', 'a', newline='') as f:        # 'w'mode는 새로운 내용이 입력되면 덮어쓰기를 한다. 'a'mode는 이어쓰기를 해준다.
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer = sv.DictWriter(f, fieldnames=['username', 'message']) # 이렇게 써도 된다.
        writer.writerow({'username': request.args.get('username'), 'message': request.args.get('message')})
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)
        




















if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
    