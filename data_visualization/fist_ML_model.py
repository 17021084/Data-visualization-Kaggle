import pandas as pd 
# from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor


# melbourn_file
mf = pd.read_csv('melb_data.csv')

# chọn cột price làm mô hình dự đoán
col_price = mf.Price
print(col_price.head(5))
print (mf.Price.tail(5))

# features sẽ làm 
features = [ 'Rooms','Bathroom' ,'Landsize' , 'Lattitude', 'Longtitude']
x= mf [ features]
# print(x.describe())
print(x.head(5))

model = DecisionTreeRegressor (random_state=1)
model.fit(x,col_price)
print( "Predict : " ,model.predict(x.tail(5) ))

