### クラス ### 
# オブジェクトの設計図
class Test_Score():
  def __init__(self,student_name, jp_score, math_score, en_score):
    self.student_name = student_name
    self.jp_score = jp_score
    self.math_score = math_score
    self.en_score = en_score
  
  def average(self):
    self.sum_score = (self.jp_score 
                + self.math_score 
                + self.en_score)
    
    average_score = round(self.sum_score / 3)
    return average_score


student_1 = Test_Score('太郎',90,70,80)
print(f'{student_1.student_name}さんの平均点:{student_1.average()}')

student_2 = Test_Score('蒼太',60,55,85)
print(f'{student_2.student_name}さんの平均点:{student_2.average()}')
print(student_2.sum_score)