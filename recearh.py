import pandas as pd
data =  pd.read_csv(r'C:/Users/hp/Downloads/collegePlace.csv')
# print(data)
y=data['PlacedOrNot'].to_list()
# print(y)
x1=data['CGPA'].to_list()
# print(x1)
x2=data