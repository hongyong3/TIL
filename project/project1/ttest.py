import requests
import os
import csv
from datetime import timedelta, datetime
from pprint import pprint

token = os.getenv("test_TOKEN")
time = datetime(2019, 1, 13)
timebyweek = time.strftime("%Y%m%d")

with open('movie.csv', 'w', newline = '', encoding = 'utf-8') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    movie_list = []

    for i in range(2):     
        url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={timebyweek}&weekGb=0&itemPerPage=10'
        update = requests.get(url).json()
        req = requests.get(url).text
        for i in range(10):
            if m_info['movieCd'] not in movie_list:
                movie_list.append(m_info['movieCd'])
                m_info = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]
                # movieCd = update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"]
                # movieNm = update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieNm"]
                # audiAcc = update["boxOfficeResult"]["weeklyBoxOfficeList"][i]["audiAcc"]             
                writer.writerow({'movie_code': m_info['movieCd'], 'title': m_info['movieNm'], 'audience':m_info['audiAcc'], 'recorded_at':f'{timebyweek}'})
        time = time + timedelta(days=- 7)