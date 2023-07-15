import pandas
from sklearn import linear_model


df = pandas.read_csv(r"C:\Users\hp\Downloads\college placement 05.csv")

X = df[['Internships', 'CGPA', 'HistoryOfBacklogs','Hostel']]
y = df['PlacedOrNot']
y0 = df['PlacedOrNot'].to_list()
x1=X['Internships'].to_list()
print(len(y))
# a=int(input("Enter strting Value: "))
# aa=int(input("Enter ending Value: "))
y1 = []
# len1 = int((len(y))/3)
for a in range(0,2967,300):
    for aa in range(301,2967,300):
        for i in range(a, aa):
            y1.append(y[i])
 print(y1,end = '')
print(y1)
print(len(y1))

regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = []

t1 = df['Internships'].to_list()
t2 = df['CGPA'].to_list()
t3 = df['HistoryOfBacklogs'].to_list()
t4 = df['Hostel'].to_list()

for i in range(a, aa):
    z1 = t1[i]
    z2 = t2[i]
    z3 = t3[i]
    z4 = t4[i]
    x1 = regr.predict([[z1, z2, z3,z4]])
    predictedCO2.append(x1.tolist())

 print(predictedCO2)
prediction = [item for sublist in predictedCO2 for item in sublist]
print(prediction)
print(len(prediction))

fy=[]
for i in range(0,len(prediction)):
    fy1=(2.71**prediction[i])
    fy2=fy1/(1+fy1)
    fy.append(fy2)
print(fy)
print(y0[0])


d1 = 0
print(fy[0])
for n in range(0,len(prediction)):
    if (y0[n]-fy[n]) <=.4:
        d1 = d1+1

print(d1)

g=len(prediction)
m=d1
er=(g-m)/g
print("Error rate is",er*100)
print("accuracy rate is",100-(er*100))
