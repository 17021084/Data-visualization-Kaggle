import pandas as pd 
import matplotlib as plot

# load data frame từ csv,
df = pd.read_csv('melb_data.csv' )

#xuất df ra file csv
# df.to_csv('đương dẫn')


df.columns = [ col.replace(' ','_').lower() for col in  df.columns ]

print (df.columns)

# in 5 hàng đầu trong  price

print(df.price.head(5))

# chọn nhiều cột . vd chọn 2 cột address và rooms
#df là một mảng , mỗi phần tử mảng đó  là cột, có độ dài bằng số hàng


mul_col = df[ ['landsize','buildingarea'] ]

print (mul_col.head(5) , " \ntype : " ,type(mul_col))


#------------------------------------------------------------------------------
print ("-------------------------------------------------------------\n MỘT SỐ THÔNG TIN CỦA DF")

#in ra  số dòng của df
print ( 'Số dòng = ' , len(df))    

# in tên của các cột trong df
print ( 'Tên các cột là : ' , df.columns )

#in số hàng
print ( ' Hàng  từ' , df.index)

print ( ' shape của df' , df.shape)

#in thông tin của df
print ( " thông tin " , df.info())


# in ra các thông tin của cột dùng describe
print (mul_col.describe() )   
#
 # count : số phần tử 
 # mean  : Trung vị
 #  std :standart devitaion ĐỘ lệch chuẩn
 # max , min : in ra giá trị lớn nhất nhỏ nhất
 #
 # có cách truy cập thẳng vào đó là df.thuộc tính
 # vd df.count  tính tổng
# 

# --------------------------------------------------------------------------
print ("----------------------------------------------------------------------------\n My Task")

# 1 print list of columns

print ( 'list of columns :' , df.columns)


df['landsize'].plot(kind='bar')

