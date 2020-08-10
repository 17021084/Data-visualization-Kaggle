import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


dt = pd.read_csv("pokemon_ass.csv")
print ( dt.head(10))

# # value_counts  số lần xuất hiện của các giá trị trong 1 cột
# print ( " value_counts  trả về số lần xuất hiện của các giá tri\n" , dt.Total.value_counts().head(10))
# print ( " descripe cái số lần xuất hiện các giá trị" ,dt.Total.value_counts().describe() )


# dt.plot.scatter ( x= "Attack" , y ="Defense", figsize =(15,10) , title="pokemon attack n defense" )
# # biểu đồ thể hiện mỗi quan hệ cột attack và cột defense
# plt.show()

#Pokemon by Stat Total
# ax = dt.Total.value_counts().plot.hist( color= 'gray',bins=100)
#bins là số cột sẽ đc dùng
# ax.set_title('Pokemon by stat total' , fontsize = 30)

# biểu đồ quan hệ giữa hp và attack

dt.head(30).plot.line( x='HP' , y ='Attack')


plt.show()
