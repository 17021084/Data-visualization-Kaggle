import pandas as pd 
import matplotlib.pyplot  as plt

dt = pd.read_csv('pokemon.csv' , index_col='abilities')

# # The frequency of Pokemon by type
# dt['type1'].value_counts().plot.bar()
# plt.show()
# print (dt['type1'].describe())

# The frequency of Pokemon by HP stat total:

# print ( "thông tin về HP", dt.hp.describe() )

# chú ý , phải dùng hàm sort_index() để sắp xếp  .
# dt.hp.value_counts().sort_index().plot.line()
# plt.show()



# The frequency of Pokemon by weight

print('thông tin về cân nặng', dt.weight_kg.describe())
dt.weight_kg.sort_index().plot.hist()
plt.show()


