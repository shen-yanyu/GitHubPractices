import requests
import re
import urllib.response
num = 1
while True:
    url =  ['http://www.win4000.com/meinvtag4_{}.html'.format(num)]
    num += 1
    if num > 6:
        break
    #print(url)
    for urls in url:
        response = requests.get(url=urls)
        print(response)
        html = response.text
        imgs = re.findall(r'<li>.*?data-original="(.*?)" alt=', html, re.S)
        print(imgs)
'''
        for index,img_url in enumerate(imgs):
            response = requests.get(img_url)
            with open('%.%s'%(index, img_url.split('.')[-1]), 'wb') as f:
                f.write(response.content)
                f.close()
'''

