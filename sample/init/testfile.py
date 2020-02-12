import requests

params={
    'username' : 'admin',
    'password' : '1234'
}

session_requests = requests.session()
result = session_requests.post("http://dev.de2o.com:8889/login",data=params)
print(result.status_code)
# r = requests.post("http://dev.de2o.com:8889/login",data=params,verify=False)
r = session_requests.get("http://dev.de2o.com:8889/salesOptntList")
print(r.status_code)
print(r.content)