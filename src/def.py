scores = {'国語': 50, '数学': 50, '英語': 50, '社会': 53, '理科': 43}

def average_score(scores):
  total_score = 0
  for key, value in scores.items():
    if key in ['国語', '数学', '英語']:
      total_score += value
  return total_score / 3

result = average_score(scores)
print(result)

three_subject_score = list(map(lambda key: scores[key],['国語','数学','英語']))#['国語','数学','英語']をkeyに入れてscoresから三教科取り出してリスト化する
print(sum(three_subject_score)/len(three_subject_score))