### json ###
import json

obj = {'サプー': 'apple', 'price': 120}

json_text = json.dumps(obj, ensure_ascii=False)
print(json_text)
print(type(json_text))

#jsonはアプリ間のデータの受け渡しに必要
