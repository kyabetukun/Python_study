import random

#数当てゲーム

random_number = random.randint(1,9)
print('1~9の中で私の考えてる数字はなんでしょう?')
anther = int(input())

if anther == random_number:
  print('正解!!!')
else:
  print(f'違うよ〜〜、正解は{random_number}')