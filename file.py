### ファイル操作 ###
x_list = ['apple', 'orange', 'banana']
s = '\n'.join(x_list)
with open('text/string.txt','a') as f:
    f.write(s)