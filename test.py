#国語は80点です
#数学は60点です
#理科は90点です

y_dic = {'国語':80, '数学':60, "理科":90}  #keys,values,items
for x, y in y_dic.items():#辞書でxにキーを入れてyに値を入れる
  print(f'{x}は{y}点です')#xはy点ですと出力
