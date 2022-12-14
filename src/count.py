import time
a = 0
while True:
  print(f'{a} | {a} | {a}')
  a += 1
  if a == 6:
    a = 0
  time.sleep(0.5)