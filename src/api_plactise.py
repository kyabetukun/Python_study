import json
import requests

#APIとは
API_KEY = "**********"#APIを使うにはAPIキーというものを発行する


lat = 34.69894488811009
lng = 135.19316833478882

res = requests.get(f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={API_KEY}&lat={lat}&lng={lng}&keyword=&range=2&order=1&format=json")
data = res.json()
print(data)