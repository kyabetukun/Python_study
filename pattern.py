###　正規表現 ###
import re

# 正規表現パターンをコンパイル
pattern = re.compile(r'[0-9]{3}-[0-9]{4}-[0-9]{4}')

# 正規表現による検索
result = pattern.search('080-2894-3382')

# 検索結果を表示
print(result.group())

