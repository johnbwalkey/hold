# NeuralNine - call Py scripts from Excel using VBA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data =pd.read_excel("mydata.xlsx")
print (data)

data.prices.hist()
plt.show()

grouped_data = data.groupby(by="categories").mean()
plt.bar(grouped_data.index, grouped_data.prices)
plt.show()

# comment out selected line by doing ctrl and /

One_category = pd.get_dummies(data.categories)
data  = data.join(One_category)
data.drop(["categories"], axis=1)

sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
plt.show()

