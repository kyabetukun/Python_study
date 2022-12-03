### クラスの継承 ###
class HumanClass:
  def __init__(self):
    print('HUmanClassのinit')
    self.hp = 100

class WizardClass(HumanClass):
  def __init__(self):
    super().__init__()
    self.mp = 50


wizard = WizardClass()

print(f'HP{wizard.hp}MP{wizard.mp}')