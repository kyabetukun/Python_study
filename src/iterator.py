three_subject_scores = {"国語": 84.0, "数学": 66.0, "英語": 72.0}
total_score = 0

for subject, score in three_subject_scores.items():
    print(f'{subject}は{score}点です')
    total_score += score

average_score = total_score / 3
print(f'合計点:{total_score}')
print(f'平均点:{average_score}')