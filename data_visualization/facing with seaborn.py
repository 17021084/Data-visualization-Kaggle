import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("max_columns",None)
df = pd.read_csv("CompleteDataset.csv" , index_col=0)

# chi tiết về grid :https://seaborn.pydata.org/tutorial/axis_grids.html


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

# Trong seaborn có 2 loại 
# Facet Grid : Tốt cho dữ liệu với ít nhất hai biến phân loại.
# Pair Plot:Tốt để khám phá hầu hết các loại dữ liệu


# df = footballers[footballers['Position'].isin(['ST', 'GK'])]  #data frame

# g = sns.FacetGrid(df, col="Position")    # lưới để tạo nhiều đồ thị con (grid obj)

# g.map(sns.kdeplot, "Overall")   # dùng map obj đề đưa các plot vào lưới tương ứng

# df = footballers

# g = sns.FacetGrid(df ,col="Position" , col_wrap=6 )  
# # col_wrap : para lưới có tối đa 6 cột 

# g.map(sns.kdeplot,"Overall")
#  mình sẽ vẽ biểu đồ tần xuất f theo kiểu kde với trục hoành là  overall



# bây giờ mình muốn so sánh the Position , club và overall

#thao tác lọc ra những thằng st và gk
# df = footballers[ footballers['Position'].isin(['ST', 'GK'])]
# df = df[ df['Club'].isin(['Real Madrid CF', 'FC Barcelona', 'Atlético Madrid']) ]

# # tạo g object phần init
# g = sns.FacetGrid( df , row="Position", col="Club",
#                     # Phần ccài đặt các cột hàng của grid thứ tự sẽ là như nào .( phần này có cũng đc , ko quan trọng)
#                     row_order=['GK', 'ST'],                      
#                     col_order=['Atlético Madrid', 'FC Barcelona', 'Real Madrid CF']
# )

# theo grid 
# row : phân biệt các position theo hàng , tức là cùng hàng sẽ giống vị chí
# col : phân biệt các Club theo cột , tức là cùng 1 cột là cùng 1 club, khác cột khác club
# hue : phân biệt theo màu sắc



# g.map(sns.violinplot,"Overall")
# phần hiển thị đồ thị
#kiểu đồ thị, 
# đồ thị phân bố của overall với trục hoành là over all
# ngoài ra ta có thể thêm cột nữa trong data set , nó sẽ là đồ thị thể hiện quan hệ của overall với cái cột thêm đo 

#Pair plot
sns.pairplot(footballers[['Overall', 'Potential', 'Value']])

plt.show()