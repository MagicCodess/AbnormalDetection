import pandas as pd
import numpy as np


###Preprocessing
def preprocessing(test):
    if list(test.columns.values) != ["timestamp", "value"]:
        test.columns = ["timestamp", "value"]


###Calculate EMA
def EMA(bdp, n):
    emaResult = []
    j = 1
    sma = bdp[:n].value.sum()/n
    alpha = 2 / float(1 + n)
    for i in range(0, n):
        emaResult.append(sma)
    emaResult.append(((bdp.value[n] - sma) * alpha) + sma)
    for i in bdp.value[n+1:]:
        tmp = ((i - emaResult[j]) * alpha) + emaResult[j]
        j = j + 1
        emaResult.append(tmp)
    ema = pd.DataFrame({'timestamp' : bdp.timestamp, 'value' : bdp.value, 'ema' : emaResult})
    return ema


###detection
def detectAbnormal(emaResult, threshold):
    result =[]
    if np.abs(emaResult.value[0]-np.mean(emaResult.value[0:2]))>threshold:
        result.append('×')
    else:
        result.append('√')
    for i in range(1,len(emaResult)-1):
        if np.abs(emaResult.value[i]-emaResult.value[i-1])>threshold and np.abs(emaResult.value[i]-emaResult.value[i+1])>threshold and np.abs(emaResult.value[i-1]-emaResult.value[i+1])<threshold:
            print(np.abs(emaResult.value[i-1]-emaResult.value[i+1]) < threshold)
            result.append('×')
        else:
            result.append('√')
    if np.abs(emaResult.value[len(emaResult)-1]-np.mean(emaResult.value[-2:])) > threshold:
        result.append('×')
    else:
        result.append('√')
    detection = pd.DataFrame({'timestamp': emaResult.timestamp, 'value': emaResult.value, 'Normal' : result})
    return detection

