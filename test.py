import pandas as pd
import numpy as np
import AbnormalDetectionTools

test = pd.read_csv('test.csv')
AbnormalDetectionTools.preprocessing(test)
emaResult = AbnormalDetectionTools.EMA(test, 2)
result =AbnormalDetectionTools.detectAbnormal(emaResult, 2)
print(result)