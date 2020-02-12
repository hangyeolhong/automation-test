import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

res = requests.get("http://dev.de2o.com:8889/authLogin")
print("login page status code is ***", res.status_code)

# params = {
#     'userId' : 'admin',
#     'password' : '1234'
# }
#
# res = requests.post("http://dev.de2o.com:8889/login", data=params, verify=False)

    # 쿠키와 헤더에 포함된 302 Location 값을 가져온다.
    # 이때, 헤더에 설정된 쿠키와 함께 Location으로 Get Request 를 보내면 된다.
    # redirect_cookie = res.headers['Set-Cookie']
    # redirect_url = res.headers['Location']
    # headers = {"Cookie": redirect_cookie}

    # # Location 주소로 Get Request 호출
    # s.get(redirect_url, headers=headers)
# ids = {
#     'userId' : 'admin',
#     'password' : '1234'
# }
# res2 = requests.post("http://dev.de2o.com:8889/login",data=ids)
# print(res2.status_code)
# print("*** session 인증 시작 ***")
# session = requests.session()
# session.auth = ("admin" , "1234")
#
# r = session.get("http://dev.de2o.com:8889/salesOptntList")
# print("r.content: " ,r.content)
html = urlopen("http://dev.de2o.com:8889/salesOptntList")
bsObj = BeautifulSoup(html,"html.parser")

for link in bsObj.findAll("a"):
    print(link)
# for title in bsObj.find("table",{"id":"tbSalesOptntList"}).findAll("a"):
#     if 'href' in title.attrs :
#         print(title.attrs['href'])