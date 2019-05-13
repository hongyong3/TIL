import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"
for i in range(10):
    conn.request("GET", "/3/movie/now_playing?page="+f"{i+1}"+"&language=ko-kr&api_key=f55decdd8b4533ff751d5e5df47ac372", payload)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))