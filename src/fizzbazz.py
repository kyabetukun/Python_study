import numpy as np #numpyライブラリをインポート
import time #timeライブラリをインポート
i = np.array([1,1,1])  #i[0]が1, i[1]も１, i[2]も１
s = np.array([1,1,1]) #i[0]が1, i[1]も１, i[2]も１
while True:
  #i[0]、i[1],i[2]を表示 
  print(f'{i[0]} | {i[1]} | {i[2]}')  
  
  #普通のリストだと、iは[1,1,1,1,1,1]になる。
  #numpyのarrayで作ったリストだと同じインデックス番号の数値が足されるので[2,2,2]になる 
  i += s 
  
  #i[0]が6になったらiを[1,1,1]に戻す
  #つまりiが[6,6,6]になっている時
  if i[0] == 6:
    i = np.array([1,1,1])
  #0.5秒待機  
  time.sleep(0.5)
  

