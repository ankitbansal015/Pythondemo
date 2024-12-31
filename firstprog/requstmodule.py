import requests

# r=requests.get("https://docs.python-requests.org/en/master/")
# print(r.text)
#print(r.status_code)

url="www,hgjh.com"
data={
    "p1":4,
    "p2":8,
}
r2=requests.post(url=url,data=data)
