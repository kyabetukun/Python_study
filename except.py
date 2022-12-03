### 例外処理 ###  
x = 1
y = 0
try:
  result = x / y
except Exception as e:
  print('異常です')
  print(e)