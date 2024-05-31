def remove_max_and_min(d):
    for key in d:
        max_score = max(d[key])
        min_score = min(d[key])
        d[key].remove(max_score)
        d[key].remove(min_score)
    return d


def get_avg(d):
    for key in d:
        avg = sum(d[key]) / len(d[key])
        d[key] = avg
    return d


score = {"001": [90, 94, 97, 86, 85, 89, 88, 85],
         "002": [91, 91, 92, 98, 90, 96, 90, 95],
         "003": [96, 86, 97, 96, 87, 86, 86, 96],
         "004": [95, 95, 94, 93, 97, 98, 99, 95],
         "005": [95, 87, 94, 94, 93, 99, 96, 97],
         "006": [89, 97, 91, 95, 89, 94, 97, 92]}

remove_max_and_min(score)
get_avg(score)

ls = sorted(score.items(), key=lambda x: x[1], reverse=True)
print("选手编号和最后得分：")
for i in ls:
    print(i[0], i[1])