### リスト内包表記  ###
study_list = []

#普通のfor文
for i in range(5):
  study_list.append(i)
  print(study_list) 

#内包表記
study_list = [i for i in range(5)]
print(study_list)


#普通のfor文
study_list_2 = []
for i in range(10):
    if i % 2 == 1:
        study_list_2.append(i)
#print(z_list)


#内包表記
study_list_3 = [i for i in range(10) if i % 2 ==1]
print(study_list_3)