import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# C:\Users\willh\codes\kaggle\predict_future_sales
cwd = os.getcwd()
print(cwd)
import os
# for dirname, _, filenames in os.walk("C:/users/willh/codes/kaggle/predict_future_sales/data"):
for dirname, _, filenames in os.walk("./data"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv('./data/sales_train.csv')
data.head()