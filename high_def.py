### 高階関数 ###
#引数か戻り値に関数が指定されている関数

from stringprep import map_table_b2


def apple():
  print('これはりんごです') #関数自体がオブジェクト
  
def run_twice(func):
  func()
  func()
run_twice(apple)#関数を引数にしている

#map関数
x = [0, -20, 9.1, 7]
def twice(num):
  return num * 2

map_obj = list(map(twice, x))
print(map_obj)
#ラムダ式を使うと
result = list(map(lambda num: num*2, x))
print(result)