### ラムダ式 ###

# defの場合
def study(z):
  print(z + "!")
  
# lambda 引数 : 処理
func = lambda x, y: print(f'{x}は{y}点です')
func("国語",80)

# map関数
names = ["鈴木", "斉藤", "田中"]
result = list(map(lambda x: x + "さん", names))
print(result)

# filter関数

numbers = [1,3,4,10,22,30]
result = list(filter(lambda x: x>=10, numbers))
print(result)