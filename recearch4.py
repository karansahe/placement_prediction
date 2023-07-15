import pandas
from sklearn import linear_model

df= pandas.read_csv(r"C:\Users\hp\Downloads\college placement 05.csv" )
print(df)


X = df[['Internships', 'CGPA', 'HistoryOfBacklogs']]
y = df['PlacedOrNot']
# print(y)
y1 = []
#len1 = int((len(y))/3)15
a=int(input("enter the value:"))
for i in range(000, a):
    y1.append(y[i])
# print(y1,end = '')

regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = []

t1 = df['Internships'].to_list()
t2 = df['CGPA'].to_list()
t3 = df['HistoryOfBacklogs'].to_list()

for i in range(1, a):
    z1 = t1[i]
    z2 = t2[i]
    z3 = t3[i]
    x1 = regr.predict([[z1, z2, z3]])
    predictedCO2.append(x1.tolist())
    d1=0
    for n in range(0,len(yl)):
        if (y[n])-yl[n])>=.5:
            d1=d1+1

print(d1)  