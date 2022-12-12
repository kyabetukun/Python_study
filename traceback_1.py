###　トレースバック ###
import traceback
try:
  
  x = 1 / 0
  x += 1
  print(x)
except:
  traceback.print_exc()