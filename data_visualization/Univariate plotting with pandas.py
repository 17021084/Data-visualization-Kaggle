import pandas as pd 
import matplotlib.pyplot as plt


# 4 loại biểu đồ cơ bản trong pandas
    #  bar char
    #  line char
    #  area char 
    # histogram
#


dt = pd.read_csv('winemag-data_first150k.csv' , index_col=0)
# print (dt.head(10))


# vẽ cột province với bar char
# dt['province'].value_counts().head(50).plot.bar()

# để muốn nhìn thấy đồi thị phải import plt
# plt.show( block =True)

# dt['points'].value_counts().sort_index().plot.bar()
# plt.show( block =True)

# biểu đồ line
dt['points'].value_counts().sort_index().plot.line()
plt.show()

#biểu đồ area 
dt['points'].value_counts().sort_index().plot.area()
plt.show()

# biểu đồ histogram
dt['points'].plot.hist()
plt.show()

