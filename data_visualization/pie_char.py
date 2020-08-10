import pandas as pd 
import matplotlib.pyplot as plt


dt = pd.read_csv("winemag-data_first150k.csv", index_col=0)
# biều đồ hình tròn giúp ta biết cơ cấu của 1 đối tượng,
dt.province.value_counts().head(10).plot.pie()
plt.gca().set_aspect('equal')
plt.show()

