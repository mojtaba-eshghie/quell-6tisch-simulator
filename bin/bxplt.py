import matplotlib.pyplot as plt
import numpy as np
import json


spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)



result_list = list()
result_list2 = list()

with open('per2.json', 'r') as per_results:
    data = json.load(per_results)
    for key, value in data.items():
        result_list.append(value)

with open('per1.json', 'r') as per_results2:
    data = json.load(per_results2)
    for key, value in data.items():
        result_list2.append(value)


print(result_list)
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
ax.set_xticklabels(['OF0', 'quell'])

ax.boxplot([result_list, result_list2])
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.show()