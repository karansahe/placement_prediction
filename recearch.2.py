import pandas as pd
data =  pd.read_csv(r'C:/Users/hp/Downloads/collegePlace.csv')
print(data)
ix4=[]
x4=data['Stream'].to_list()
for i in range(0,len(x4)):
    if x4[i]=="Computer Science":
        ix4.append(1)
    elif x4[i]=="Information Technology":
        ix4.append(2)
    elif x4[i]=="Electronics And Communication":
        ix4.append(3)
    elif x4[i]=="Electrical":
        ix4.append(4)
    elif x4[i]=="Mechanical":
        ix4.append(5)
    elif x4[i]=="Civil":
        ix4.append(6)
print(ix4)
print(len(ix4))