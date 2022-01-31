import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# C:\Users\willh\codes\kaggle\predict_future_sales
cwd = os.getcwd()
print(cwd)

# for dirname, _, filenames in os.walk("C:/users/willh/codes/kaggle/predict_future_sales/data"):
for dirname, _, filenames in os.walk("./data"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv('./data/sales_train.csv')
data.head()

data.info()

data.corr()

# corretion map
f, ax = plt.subplots(figsize=(18,18))
sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()

data.head(10)
data.columns

# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.item_price.plot(kind = 'line', color = 'g', label = 'item_price', linewidth=1, alpha = 0.5, grid = True, linestyle=':')
data.item_cnt_day.plot(color = 'r', label = 'item_cnt_day', linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()


# Scatter Plot 
# x = attack, y = defense
data.plot(kind='scatter', x='item_cnt_day', y='item_price',alpha = 0.5,color = 'red')
plt.xlabel('item_cnt_day')              # label = name of label
plt.ylabel('item_price')
plt.title('item_cnt_day item_price Scatter Plot')            # title = title of plot

# Histogram
# bins = number of bar in figure
data.shop_id.plot(kind = 'hist', bins = 50, figsize = (12,12))
plt.show()

# clf() = cleans it up again you can start a fresh
data.item_price.plot(kind = 'hist',bins = 50)
# plt.clf()
# We cannot see plot due to clf()

# create dictionary and look view the keys and values
dictionary = {'spain':'madrid','usa':'vegas'}
print(dictionary.keys())
print(dictionary.values())

# Keys have to be immutable objects like string, boolean, float, integer or tubles
# List is not immutable
# Keys are unique
dictionary['spain'] = 'barcelona'   #update existing entry
print(dictionary)
dictionary['france'] = 'paris'      # Add new entry
print(dictionary)
del dictionary['spain']             # remove entry with key 'spain'
print(dictionary)
print('france' in dictionary)       #check include or not
dictionary.clear()
print(dictionary)

# In order to run all code you need to comment this line
#del dictionary                     # delete entire dictionary
print(dictionary)                   # it gives error because dictionary is deleted

### PANDAS

data = pd.read_csv('./data/sales_train.csv')
data.head()

series = data['item_id']            # series
print(type(series))
data_frame = data[['item_id']]      # data frame
print(type(data_frame))


x = data['item_id']>22000           # there are only 28190