#replace 文字列を置き換える
x = "あいうえお"
print(x)
y = x.replace('いうえお','んぱんまん')
print(y)

#.join() リスト内の要素同士を指定した文字で結合する
fruit_list = ["トマト","バナナ","レモン"]
mix_fruit_list = " ".join(fruit_list)
print(mix_fruit_list)

#strip() 先頭と末尾の空白を削除
name = "-080-2894-3382-" 
full_name = name.strip("-")
print(full_name)

#zfill 指定した桁数まで０埋めする

id = '4323'.zfill(10)
print(id)

#upper 小文字を大文字にする
#lower 大文字を小文字にする

mini = "FDSFD".lower()
print(mini)