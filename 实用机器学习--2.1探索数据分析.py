# 2.1探索数据分析：https://c.d2l.ai/stanford-cs329p/_static/notebooks/cs329p_notebook_eda.slides.html#/13
# !pip install seaborn pandas matplotlib numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display
display.set_matplotlib_formats('svg')
# Alternative to set svg for newer versions
# import matplotlib_inline
# matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# 1获取数据
data = pd.read_csv('house_sales.zip')
# 数据的大小
data.shape
#展示前5行数据
data.head()
#将没列数据缺失值多于30%d的特征去掉
#null_sum = data.isnull().sum()  #t统计每行缺失值的总量
data.columns[null_sum < len(data) * 0.3]  # columns will keep
data.drop(columns=data.columns[null_sum > len(data) * 0.3], inplace=True)#inplace表示永久删除

# 数据清洗：展示每列的数据是否合理，比如身份证号是否为字符型
data.dtypes

#Convert currency from string format such as $1,000,000 to float.
currency = ['Sold Price', 'Listed Price', 'Tax assessed value', 'Annual tax amount']
for c in currency:
    data[c] = data[c].replace(
        r'[$,-]', '', regex=True).replace(
        r'^\s*$', np.nan, regex=True).astype(float)

#Convert currency from string format such as $1,000,000 to float.
areas = ['Total interior livable area', 'Lot size']
for c in areas:
    acres = data[c].str.contains('Acres') == True
    col = data[c].replace(r'\b sqft\b|\b Acres\b|\b,\b','', regex=True).astype(float)
    col[acres] *= 43560
    data[c] = col
#Now we can check values of the numerical columns. You could see the min and max values for several columns do not make sense.
#查看数据是否合理：比如可居住面积非常大，不符合实际，或者出现负值，这些不符合实际的是噪音
data.describe()

#We filter out houses whose living areas are too small or too hard to simplify the visualization later.
#下面做些简单处理：将放在的大小小于10或者大于10000的数据去掉
abnormal = (data[areas[1]] < 10) | (data[areas[1]] > 1e4)
data = data[~abnormal]
sum(abnormal)
#Let's check the histogram of the 'Sold Price', which is the target we want to predict.
ax = sns.histplot(np.log10(data['Sold Price']))
ax.set_xlim([3, 8])
ax.set_xticks(range(3, 9))
ax.set_xticklabels(['%.0e'%a for a in 10**ax.get_xticks()]);
#可以在最左边的数据房屋价格较小，可能是出租的价格所以我们可以将这种数据去掉

#A house has different types. Here are the top types:
#将不重复数据的个数显示每列
data['Type'].value_counts()[0:20]

#Price density for different house types.
types = data['Type'].isin(['SingleFamily', 'Condo', 'MultiFamily', 'Townhouse'])
sns.displot(pd.DataFrame({'Sold Price':np.log10(data[types]['Sold Price']),
                          'Type':data[types]['Type']}),
            x='Sold Price', hue='Type', kind='kde');

#Another important measurement is the sale price per living sqft. Let's check the differences between different house types.
#单位面积的价格
data['Price per living sqft'] = data['Sold Price'] / data['Total interior livable area']
ax = sns.boxplot(x='Type', y='Price per living sqft', data=data[types], fliersize=0)
ax.set_ylim([0, 2000]);
#中位数，25分位数，75%分位数，用来表示不同分布的对比

#We know the location affect the price. Let's check the price for the top 20 zip codes.
d = data[data['Zip'].isin(data['Zip'].value_counts()[:20].keys())]
ax = sns.boxplot(x='Zip', y='Price per living sqft', data=d, fliersize=0)
ax.set_ylim([0, 2000])
ax.set_xticklabels(ax.get_xticklabels(), rotation=90);
# 地域对房屋价格产生较大影响

#两列数据之间的关联图，数据是关联系数
#可以看出房屋价格于annual tax amount之间有较大的练习
#Last, we visualize the correlation matrix of several columns.
_, ax = plt.subplots(figsize=(6,6))
columns = ['Sold Price', 'Listed Price', 'Annual tax amount', 'Price per living sqft', 'Elementary School Score', 'High School Score']
sns.heatmap(data[columns].corr(),annot=True,cmap='RdYlGn', ax=ax);

'''
Summary
This notebook demonstrates the basic technologies for EDA, including

Understanding column data types, values, and distributions
Understanding the interactions between columns
We only explored a small aspect of the data. You are welcome to dive deep into more details.
'''
