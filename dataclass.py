### データクラス ###
from dataclasses import dataclass

@dataclass
class Person:
  name:str
  age: int 
  gender: str
  
student_1 = Person('たかし',14,'man')
print(student_1.name)

