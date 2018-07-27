import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json

result_list = list()

with open('per2.json', 'r') as per_results:
    data = json.load(per_results)
    for key, value in data.items():
        value = int(value*100)
        result_list.append(value)

print(result_list)
