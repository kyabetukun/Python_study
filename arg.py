### 可変長引数 ###
def func(*args,x):
  result = ' '.join(args)
  print(f'{result}{x}')
  
func('こんにちは','佐藤さん',x='こんばんは')

def func_dic(**kwargs):
  print(kwargs)

func_dic(subject="国語",score=80)