import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


dt = pd.read_csv("winemag-data_first150k.csv", index_col=0)

# một số đồ thị
# countplot()
# kdeplot
# joint
# violin

# print ( dt.points.value_counts().sort_index().describe())
# # biểu đồ hiển thị số lượng người vote cho các điểm
# sns.countplot( dt.points)
# plt.show()


# kde plot  (kernel density estimate)
# pp loại nhiễu, nó sẽ bỏ đi những giá trị giữa để làm cho đường đồ thị mượt nhất ,
#  so sánh 2 đồ thị trên sẽ thaấy kết quả

# sns.kdeplot(dt.query('price < 200').price)
# plt.show()

# dt[dt.price<200].price.value_counts().sort_index().plot.line()
# plt.show()

# sử dụng cho 2 hướng
# sns.kdeplot(dt[dt['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))
# print ( dt[dt['price'] < 200].loc[:, ['price', 'points']])
# loc [ ] trả về các hàng trong cột price và point
# dropna() loại bỏ cặp giá trị ko xác định
# plt.show()



# Distplot giống hist
# sns.distplot(dt['points'], bins=10, kde=False)
# plt.show()


#joint plot 
# Scatterplot and hexplot

#vẽ đồ thị quan hệ của price so vs points , với data là các hàng có price <100
# kiết hợp với đồ thị kiểu bar
# sns.jointplot(x='price', y='points', data=dt[dt['price'] < 100])
# plt.show()
#kiết hợp giữa hex và bar
# sns.jointplot(x='price', y='points', data=dt[dt['price'] < 100], kind='hex', gridsize=20)
# plt.show()



# Boxplot and violin plot
# thông tin chi tiết về biểu đồ này :http://diagrammm.com/violin_plot

#boxplot

df = dt[dt.variety.isin(dt.variety.value_counts().head(5).index)] # data frame
# sns.boxplot(
#     x="variety",
#     y="points",
#     data=df # lấy data từ df 
# )

# cái hộp kia  là trung tâm của phân phối, đường ở giữa là median




# plt.show()



#violin plot

sns.violinplot(
    x="variety",
    y="points",
    data=df
)

plt.show()