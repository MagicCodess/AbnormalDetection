import pandas as pd
import numpy as np
import AbnormalDetectionTools
import matplotlib.pyplot as plt
import sys


test = pd.read_csv('test.csv')
AbnormalDetectionTools.preprocessing(test)
emaResult = AbnormalDetectionTools.EMA(test, 2)
result = AbnormalDetectionTools.detectAbnormal(emaResult, 2)
print(result)
y = result['value'].T.values
x = result['timestamp'].map(lambda x : x[-8:])
result0 = result[result['Normal']=='√']
result1 = result[result['Normal']=='×']
y0 = result0['value'].T.values
x0 = result0['timestamp'].map(lambda x: x[-8:])
y1 = result1['value'].T.values
x1 = result1['timestamp'].map(lambda x: x[-8:])
plt.figure(figsize=(10, 6))
plt.plot(x, y, '')
plt.scatter(x0, y0, marker='o')
plt.scatter(x1, y1, marker='X')
plt.xticks(np.arange(len(y)), x)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('TimeSeries')
plt.show()

