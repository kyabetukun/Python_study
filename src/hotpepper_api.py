import requests
import json
from geopy.geocoders import Nominatim

#ホットペッパーAPIのキー
API_KEY = "72e4542a18c60943"

#緯度経度を取得
geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
data = requests.get(geo_request_url).json()

def location(name):
    geo = Nominatim(user_agent="myapp")
    location = geo.geocode(name)
    print((location.latitude, location.longitude))

#緯度経度
lat = 34.69894488811009
lng = 135.19316833478882

#緯度経度を計算
lat_lng_math = "http://vldb.gsi.go.jp/sokuchi/surveycalc/patchjgd/patchjgd.php?sokuchi=0&chiiki=tokachi2003.par&Place=0&latitude=42.55303010&longitude=143.14591010&outputType=xml"
#ホットペッパーAPI
res = requests.get(f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={API_KEY}&lat={lat}&lng={lng}&keyword=&range=2&order=1&format=json")
data = res.json()

#飲食店を表示
shop = data["results"]["shop"]
print("近くのお店を表示します")

for i,shop_content in enumerate(shop):
    print(f'{shop_content["name"]}があります')
    try: #緯度経度が取れた場合,距離を計算
        print(location(shop_content["name"]))
    except: #取れない場合、駅からの経路を提示
        print(f'経路：{shop_content["access"]}')
        