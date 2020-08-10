import pandas as pd 
import matplotlib.pyplot as plt 

# Bivariate plotting with pandas
# 4 biểu đồ chính 
# Scatter Plot : phân mảnh dữ liệu
# Hex Plot :
# Stacked Bar Chart : biểu đồ cột chồng
# Bivariate Line Chart : biểu đồ đường

dt =pd.read_csv("winemag-data_first150k.csv", index_col=0)

# print (dt.columns)
#vẽ biểu đồ thể hiện quan hệ giữa points và price với price <100

# dùng scatter plot
# dt[dt.price <100 ].sample(300).plot.scatter( y='points', x='price')

#sample () là số mẫu sẽ đc plot

# scatter : phù hợp với tập data set nhỏ, và có số lượng lớn các giá trị duy nhất
# plt.show()


# hex plot
# nó sẽ thể hiện các điểm bên trong hình lục giác, độ đậm nhạt của hình lục giác sẽ dựa vào biến thứ 2

dt[dt.price <100 ].plot.hexbin( y='points', x='price' , gridsize=30)
# gridsize càng to thì diện tích hình lục giác càng bé

plt.show()