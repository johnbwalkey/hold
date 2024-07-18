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


