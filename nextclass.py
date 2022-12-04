### クラス ###
class HumanClass: #設計図
  def __init__(self):
    print('HumanClassのinit')
    self.hp = 0
    self.mp = 0
  
  def buf(self):
    self.hp += 50
    self.mp += 10

yuusya = HumanClass()
yuusya.hp = 100
yuusya.mp = 10
yuusya.buf()

sensi = HumanClass()

print(f'勇者のHPは{yuusya.hp}、MPは{yuusya.mp}です')
print(f'戦士のHPは{sensi.hp}、MPは{sensi.mp}です')
yuusya.buf()
print(f'勇者のHPは{yuusya.hp}、MPは{yuusya.mp}です')

yuusya_hp = 10
yuusya_mp = 10

sensi_hp = 10
#python 基礎編
#print 文字列フォーマット
#数値計算 %
#リスト 怪しい
#辞書 結構怪しい
#if文 怪しい
#for文 怪しい
#関数 結構怪しい

#クラス 結構怪しい 就職後