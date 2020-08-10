import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import re 
from pandas.plotting import parallel_coordinates

# link:https://www.kaggle.com/residentmario/multivariate-plotting/notebook

pd.set_option("max_columns",None)
df = pd.read_csv("CompleteDataset.csv" , index_col=0)

footballers = df.copy() #fp 

#config ko quan tâm
footballers['Unit'] = df['Value'].str[-1]
footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0, 
                                    footballers['Value'].str[1:-1].replace(r'[a-zA-Z]','')) 
                                    #thay thế chuỗi real các kí tự từ az AZ bằng ''
                                    # where( điều kiện , x ,y )

footballers['Value (M)'] = footballers['Value (M)'].astype(float)
footballers['Value (M)'] = np.where(footballers['Unit'] == 'M', 
                                    footballers['Value (M)'], 
                                    footballers['Value (M)']/1000)
footballers = footballers.assign(Value=footballers['Value (M)'],
                                 Position=footballers['Preferred Positions'].str.split().str[0])

# -------------------------------------------------------------------------------------------------


# sns.lmplot(x='Value', y='Overall', hue='Position', 
#            data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])], 
#            fit_reg=True)

#fit_reg : fit regession   estimate và fit theo mô hình hồi quy

# biểu diễn nhiều biến , với x ,y lần lượt là value và Overall 
# ngoài ra màu để phân biệt Position
# plt.show()



# Heatmap
# biểu đồ thể hiện HỆ SỐ  TƯƠNG QUAN các biến với nhau , dạng ma trận , đường chéo chính =1
#  ,mối tương quan giữa mọi cặp giá trị trong tập dữ liệu và vẽ kết quả bằng màu.

# f = (
#     footballers.loc[:, ['Acceleration', 'Aggression', 'Agility', 'Balance', 'Ball control']]
#         .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
#         .dropna() #bỏ đi những giá trị ko xác định
# ).corr()
# # tiền sử lý 
# sns.heatmap(f, annot=True)

# plt.show()


# ----------------------------------------------------------------------------------------------------

# Parallel Coordinates : đồ thị song song
# cung cấp một cách khác để trực quan hóa dữ liệu qua nhiều biến.
#là tuyệt vời để xác định cách các lớp khác nhau có thể phân biệt được trong dữ liệu

f = (
    footballers.iloc[:, 12:17]
        .loc[footballers['Position'].isin(['ST', 'GK'])]
        .applymap(lambda v: int(v) if str.isdecimal(v) else np.nan)
        .dropna()
        # str.isdecimal () trả vể true nếu string là decimal
        #dropna xóa đi  giá trị na
        #apply ( hàm hoặc hàm nạp danh)
)

f['Position'] = footballers['Position']
f = f.sample(200) # lấy 200 mẫu
parallel_coordinates (f,'Position' )

plt.show()