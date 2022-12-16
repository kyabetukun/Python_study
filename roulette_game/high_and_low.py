import random

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]#トランプの1~13

you_number = random.choice(numbers) 
print(f"あなたの数字は{you_number}")

anther = input('highかlowを選んでください:')

dealer_number = random.choice(numbers)
#引き分けの場合はもう一回めくる
if you_number == dealer_number:
  numbers.remove(dealer_number)
  dealer_number = random.choice(numbers)
  
print(f"数字は{dealer_number}")

if anther == 'high':
  if you_number <= dealer_number:
    print(f"ディーラーは{dealer_number}")
    print('あなたの勝ちです')
    
  else:
    print(f"ディーラーは{dealer_number}")
    print('あなたの負けです')
    
if anther == 'low':
  if you_number <= dealer_number:
    print(f"ディーラーは{dealer_number}")
    print('あなたの負けです')
    
  else:
    print(f"ディーラーは{dealer_number}")
    print('あなたの勝ちです')