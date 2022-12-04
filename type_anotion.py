### タイプアノテーション ###
def total_price_1item(unit_price: int, quantity:int) -> int:
  total = unit_price * quantity
  return total

total_price = total_price_1item(130, 3)
print(total_price)

##Pyright