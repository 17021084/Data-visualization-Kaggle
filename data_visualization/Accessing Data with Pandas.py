#link :https://www.kaggle.com/sohier/tutorial-accessing-data-with-pandas/
import pandas as pd 


# đọc dữ liệu vào data frame 
df = pd.read_csv('parks.csv', index_col="Park Code" )


# in ra 5 hàng đầu
df2 = df.head(5)
print (df2)

# in ra 5 hàng cuối 
df3 = df.tail(5)
print(df3)

# truy cập vào  hàng thứ 2 , 3 ,4 thông qua 1 tuple

row = df.iloc[ [2,3,4] ]
print (row)
#trả về 1 dictionary
# print ( row [0] )
# print(row.keys()[2])

#------
# một cách tiếp cận khác , tiếp cận qua cái cột đc chọn là index_col
row2= df.loc["BADL"]
print ( row2)

#-----------------------------------------------------
print("--------------------------------------------------------------\n in theo kiểu df[:5]")
print (df[:5])


#---------------------------------------------------------
print ("--------------------------------------------------------------\n truy cập đến cột")

# truy cập đến state và chỉ in 2 giá trị

col1= df["State"][:2]

# cách khác khi cột là tên mà ko có khoản trắng thì ta có thể truy cập như attribute
#  giả sử truy cập Park Code sẽ ko đc vì no có khoảng trắng

# col1 = df.State[:2]
print (col1)


# ---------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------\n truy cập đến tên của toàn bộ cột")

# sửa lại tên cột cho chuẩn:
    # viết thường hết
    # và có _ thay dấu cách
#

df.columns = [col.replace(' ', '_').lower() for col in df.columns]
print(df.columns) # in ra tên tiêu đề các cột

# ---------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------\n truy cập đến cột và hàng")
# truy cập đến nhiều cột và hàng

# acess vào state acres  lấy ra 3 phần tử
# cột  đc chọn là index_col thì auto đc in ra
print(df[['state', 'acres']][:3])


# ---------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------\n truy cập đến giá trị vô hướng")
# truy cập đến giá trị vô hướng


print (df.state.iloc[2])
# nếu truyền vào 1 list  vd [2] thì kết quả sẽ khác
print ('nếu ta truyền vào 1 list thì :-------> sẽ hiện index_col\n',df.state.iloc[  [2] ])


# ---------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------\n lấy 1 data set con")
# chọn 1 data set con thỏa mãn tính chất 
# một số toán tử logic
    # ~ replaces not
    # | replaces or
    # & replaces and
#


# chọn những thằng có state là UT
df_con = df[ (df.state =='UT') ]
print ( df_con)

# chọn  3 thằng những thằng có tọa độ >60 và diện tích 10^6 mẫu anh
print (df[(df.latitude > 60) | (df.acres > 10**6)].head(3))


print ("--------------------------- Dùng Lambda------------------------------ \n")
# dùng lambda 
print (df[df['park_name'].str.split().apply(lambda x: len(x) == 3)])

# str.split ( "kí tự  cắt theo " , số chuỗi con) default là cắt  hết theo khoảng trắng

#hàm apply  chi tiết:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
    # áp dụng 1 hàm  vào dataframe theo trục dọc
    #
#


# ---------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------\n  phương thức isin và isnull" )

# tìm các công viên có  state thỏa wa or ca

print(df[df.state.isin(['WA', 'OR', 'CA'])].head())





