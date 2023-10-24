import requests
import json
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
resp=requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8240106&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',headers=headers)
content=resp.text
rest=content.replace('fetchJSON_comment98(','').replace(');','')
json_data=json.loads(rest)
comments=json_data['comments']
for item in comments:
    Color=item['productColor']
    Size=item['productSize']
    print(Color)
    print(Size)
