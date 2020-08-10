import pandas as pd 
import matplotlib.pyplot as plt 

dt = pd.read_csv("winemag-data_first150k.csv", index_col=0)
print(dt.head(3))

#subplots(số hàng, số cột, figsize là cỡ biểu đồ con)
# fig, axarr = plt.subplots(2, 1, figsize=(12, 8))  
# subplots trả về 2 thứ :
# fig : figure hình ảnh
# axarr : axis array mảng trục

# để setting cái nào plot trước phải via qua parameter ax = axarr[]
# dt.points.value_counts().plot.bar(
#     ax= axarr[0] , # đầu tiên trên cạnh (axis)
#     title="Points"
# )
# dt.province.value_counts().head(20).plot.bar(
#     ax= axarr[1], # vị chí 1 trên axis
#     title="Province" 
# )

# plot 4 biểu đồ
fig , axarr = plt.subplots( 2, 2 , figsize=(8,8))

dt.points.value_counts().plot.bar(
    ax= axarr[0][0] , # đầu tiên trên cạnh (axis)
    fontsize=12
)
axarr[0][0].set_title("Points" , fontsize =12)

dt['variety'].value_counts().head(20).plot.bar(
    ax=axarr[1][0], fontsize=12, color='mediumvioletred'
)
axarr[1][0].set_title("Wine Varieties", fontsize=12)

dt['price'].value_counts().plot.hist(
    ax=axarr[0][1], fontsize=12, color='mediumvioletred'
)
axarr[0][1].set_title("Wine Prices", fontsize=12)


dt.province.value_counts().head(20).plot.bar(
    ax= axarr[1][1], # vị chí 1 ,1 trên axis
    fontsize=12
)
axarr[1][1].set_title("province" , fontsize =12)

plt.subplots_adjust(hspace=.5 , wspace=.5) # điều chỉnh khoảng cách của 2 đồ thị h vv , height và width

plt.show()
