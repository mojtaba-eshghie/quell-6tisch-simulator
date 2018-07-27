import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json

result_list = list()

with open('per2.json', 'r') as per_results:
    data = json.load(per_results)
    for key, value in data.items():
        result_list.append(value)


plt.xlabel('PER (Rx / Tx Ratio)')
plt.ylabel('occurences')

n, bins, patches = plt.hist(result_list, 10, normed=True, facecolor='green', alpha=0.75)

sum = 0
for i in range(0, 100):
    sum += result_list[i]

mean = sum / 100


plt.title('OF0 PER distribution, with mean: {0}'.format(str(mean)))
plt.show()