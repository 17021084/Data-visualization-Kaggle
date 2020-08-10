import pandas as pd 
from sklearn.tree import DecisionTreeRegressor


# # tạo dataframe
# df = pd.DataFrame(  { 'outlook':['sunny','sunny','overcast','rain','rain','rain','overcast','sunny','sunny','rain','sunny','overcast','overcast','rain' ] , 'temperature':[85,80,83,70,68,65,64,72,69,75,75,72,81,71] , 'hummidty':[85,90,78,96,80,70,65,95,70,80,70,90,75,80] , 'windy':[0,1,0,0,0,1,1,0,0,0,1,1,0,1] , 'play':[0,0,1,1,1,0,1,0,1,1,1,1,1,0] })

# # xuất ra file
# # df.to_csv('weather_forcast.csv')

# for i in  range ( len(df.play)) :
#     if df.play[i] == 1 : 
#         df.play[i]= True
#     if df.play[i] == 0:
#         df.play[i]= False

# for i in  range ( len(df.windy)) :
#     if df.windy[i] == 1 : 
#         df.windy[i]= True
#     if df.windy[i] == 0:
#         df.windy[i]= False

# # xuất ra file
# df.to_csv('weather_forcast.csv')
# print (df.play)
# -------------------------------------------------------------------------------------------------------------

dt = pd.read_csv('weather_forcast.csv' , index_col='stt')
print (dt)

feature = [ 'temperature'  ]

train = dt.temperature
test = dt.temperature 

# tập mục tiêu 
target = dt.hummidty

# print(dt.describe())

# tạo model
model = DecisionTreeRegressor(random_state=1)

# fit model
model.fit(train,target)
print ( " dự đoán : " , model.predict(test) )







