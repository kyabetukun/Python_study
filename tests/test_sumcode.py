from src import sumcode

def test_sum_numbers():
  result1, result2 = sumcode.sum_numbers(1, 3)
  assert result1 == 4
  assert result2 == 1