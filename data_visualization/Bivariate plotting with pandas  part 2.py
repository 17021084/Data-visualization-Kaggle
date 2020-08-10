

import pandas as pd 
import matplotlib.pyplot as plt

dt =pd.read_csv('top-five-wine-score-counts.csv',index_col=0)
                          
print ( dt.head())


# Stacked plots : biểu đồ cột chồng
# thể hiện mỗi quan hệ của các biến là các tên loại vang và số điểm của nó 

# dt.plot.bar(stacked=True)

# cái area cũng gần giống cột chồng, nó đc dùng cho giá trị liên tục
# dt.plot.area()
# plt.show()



# Bivariate line chart
# biểu đồ đường biểu diễn cho nhiều biến
# điểm khác nhau giwuax line và area :
# area trồng nhau, nên ta khó có thể so sánh rượu ở đâu  có  số người vote cùng điểm số
# line giúp ta làm việc này



dt.plot.line()
plt.show()

