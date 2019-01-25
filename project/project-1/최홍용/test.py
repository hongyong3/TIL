import requests, os, csv
from datetime import timedelta, datetime
from pprint import pprint

token = os.getenv("test_TOKEN")
time = datetime(2019, 1, 13)
week = time.strftime("%Y%m%d")

with open('boxoffice.csv', 'w', newline = '', encoding = 'utf-8') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    movie_list = []

    for i in range(10):     
        url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={week}&weekGb=0&itemPerPage=10'
        update = requests.get(url).json()
        req = requests.get(url).text
        time = time + timedelta(days =- 7)
        week = time.strftime("%Y%m%d")

        for i in range(10):
            m_list = update["boxOfficeResult"]["weeklyBoxOfficeList"][i]
            if m_list['movieCd'] not in movie_list:
                movie_list.append(m_list['movieCd'])                     
                writer.writerow({'movie_code': m_list['movieCd'], 'title': m_list['movieNm'], 'audience':m_list['audiAcc'], 'recorded_at':f'{week}'})


# 위에가 1번입니다.

# 아래가 2번입니다. 선생님ㅠㅠ



with open('movie.csv', 'w', newline = '', encoding = 'utf-8') as f:
    fieldnames = ('movie_code', 'movieName' 'movieNameEn', 'movieNameOg', 'openDate', 'showTime', 'genreName', 'peopleName', 'watchGradeNm')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    m_list_1 = []

    for i in range(len(m_list)):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={movie_list}'
        update_1 = requests.get(url).json()
        req = requests.get(url).text
        # print(update_1)
        movie_list = update_1["movieInfoResult"]["movieInfo"]
        movieCd_1 = update_1["movieInfoResult"]["movieInfo"]["movieCd"]
        movieNm_1 = update_1["movieInfoResult"]["movieInfo"]["movieNm"]       
        movieNmEn = update_1["movieInfoResult"]["movieInfo"]["movieNmEn"]
        movieNmOg = update_1["movieInfoResult"]["movieInfo"]["movieNmOg"]
        showTm = update_1["movieInfoResult"]["movieInfo"]["showTm"]
        openDt = update_1["movieInfoResult"]["movieInfo"]["openDt"]
        genreNm = update_1["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"]
        peopleNm = update_1["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]
        watchGradeNm = update_1["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]



        # 이것을 불러오면, genreNm = update_1["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"] IndexError: list index out of range 가 나옵니다. 
        # 배우도 하지 못했습니다. 죄송합니다.

# with open('movie.csv', newline='', encoding = 'utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['movieCd_1'], row['movieNm_1'], row['movieNmEn'], row['movieNmOg'], row['showTm'], row['openDt'], row['genreNm'], row['peopleNm'], row['watchGradeNm'])
