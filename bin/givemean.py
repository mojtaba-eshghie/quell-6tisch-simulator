import json

result_list = list()

with open('per_results.json', 'r') as per_results:
    data = json.load(per_results)
    for key, value in data.items():
        result_list.append(value)


sum = 0
for i in range(0, 100):
    sum += result_list[i]


mean = sum / 100
print(mean)
