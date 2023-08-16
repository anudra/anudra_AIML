import pandas as pd

data=pd.read_csv("C:/Users/SPTINT-05/Desktop/dataset/iris.csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data["PetalWidthCm"])
print(data.info())
print("\n",data.count())
print("\n",data.dtypes)
