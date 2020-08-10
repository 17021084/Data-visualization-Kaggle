import pandas as pd 
import matplotlib.pyplot as plt


dat = pd.read_csv('fifa2019.csv')

print (dat.head(5))


# dat['Overall'].value_counts().sort_index().plot.line()
# print (dat['Overall'].describe() )


print (dat['Club'].describe() )

plt.show()


