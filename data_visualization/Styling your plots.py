import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

dt = pd.read_csv("winemag-data_first150k.csv", index_col=0)


ax = dt.points.value_counts().sort_index().plot.bar( 
figsize=(16,12), 
title = "Rankings Given by Wine Magazine",
fontsize=16,
)
ax.set_title("Title được căn chỉnh lại", fontsize=20)


# một số parameter
#figsize = (width, height)  kích cỡ của đồ thị 
#color =  red . màu của cột . mặc định thì nó sẽ để màu cho mỗi bar là auto
#fontsize =  :  cỡ chữ
# title =  : tiêu đề của cột . pandas ko hỗ trợ format cái title
# tuy nhiên có thể căn chỉnh title bằng cách khác


sns.despine(bottom=True, left=True) # tắt cái viền ( xóa trục tung hoành) bằng seaborn



plt.show()
