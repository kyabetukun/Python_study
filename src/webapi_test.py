### WEB API ###
import requests

res = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=6580045')
print(res.status_code)
print(res.text)
res_json = res.json()

results =res_json["results"][0]
addres = results["address1"] + results["address2"] + results["address3"]
print(addres)

#おすすめAPI
#駅すぱあと
#Open Weather Map API
#Speech-to-Text
#aText-to-Speech
#VisionAPI 画像内のテキスト
#ExchangeRatesAPI 為替
