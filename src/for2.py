### for文便利な関数  ###
#tqdm関数
from tqdm import tqdm

for tqdm_time in tqdm(range(1)):
  pass

#zip関数
sales_2022 = [100,200,300,50]
sales_2021 = [300,200,200,100]

for this_year, last_year in zip(sales_2022,sales_2021):
  result = (this_year + last_year) / 2
  print(f"平均売上{result}")
  
#enumerate関数
names = ['佐藤','鈴木','田中']
for i, name in enumerate(names,start=1):
  print(f"{i}位 {name}")