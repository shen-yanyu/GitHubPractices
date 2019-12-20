# coding = utf-8
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573895809813&di=e5f47732be16c776979c1c418597f854&imgtype=0&src=http%3A%2F%2Fbpic.ooopic.com%2F16%2F83%2F23%2F16832366-dbcc822b3a9b252fd3842ef183e24813.jpg'
response = requests.get(url)

'''
with open("baidu.jpg", "wb") as f:
    f.write(response.content)
    f.close()
'''
print(response.status_code)
print(response.request.url)
print(response.url)
print(response.headers)
print(response.request.headers)