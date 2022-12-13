#イミュータブル
from re import X


x = 10 
print(id(x))
x += 20
print(id(x)) #新しいオブジェクト
#イミュータブル値を変更できない int,float,bool,文字列,タプル
#ミュータブル 値を変更できる リスト、辞書、集合

x = [1,2,3]
y = x
y.append(4)
#どちらも4が追加されてしまう
print(x)
print(y)
