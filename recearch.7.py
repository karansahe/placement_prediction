import pandas
from sklearn import linear_model


df = pandas.read_csv(r"C:\Users\hp\Downloads\college placement 05.csv")

X = df[['Internships', 'CGPA', 'HistoryOfBacklogs','Hostel']]
y = df['PlacedOrNot']
# y0 = df['PlacedOrNot'].to_list()

a=[] #300 differents
aa=[] #299 differents
for i in range(0,2700,300):
    n=i+1
    a.append(n)

for i in range(300,2702,300):
    n=i
    aa.append(n)



regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)

t1 = df['Internships'].to_list()
t2 = df['CGPA'].to_list()
t3 = df['HistoryOfBacklogs'].to_list()
t4 = df['Hostel'].to_list()

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
predicted1 = []
predicted2 = []
predicted3 = []
predicted4 = []
predicted5 = []
predicted6 = []
predicted7 = []
predicted8 = []
predicted9 = []
predicted10 = []

n=0
for i in range(0,len(a)):
    a1=a[i]
    a2=aa[i]
    n=n+1
    # print(n)
    # print(a1,a2)
    for i in range(a1, a2):
        if n==1:
            y1.append(y[i])
        elif n==2:
            y2.append(y[i])
        elif n==3:
            y3.append(y[i])
        elif n==4:
            y4.append(y[i])
        elif n==5:
            y5.append(y[i])
        elif n==6:
            y6.append(y[i])
        elif n==7:
            y7.append(y[i])
        elif n==8:
            y8.append(y[i])
        elif n==9:
            y9.append(y[i])
        z1 = t1[i]
        z2 = t2[i]
        z3 = t3[i]
        z4 = t4[i]
        x1 = regr.predict([[z1, z2, z3,z4]])
        if n==1:
            predicted1.append(x1.tolist())
        if n==2:
            predicted2.append(x1.tolist())
        if n==3:
            predicted3.append(x1.tolist())
        if n==4:
            predicted4.append(x1.tolist())
        if n==5:
            predicted5.append(x1.tolist())
        if n==6:
            predicted6.append(x1.tolist())
        if n==7:
            predicted7.append(x1.tolist())
        if n==8:
            predicted8.append(x1.tolist())
        if n==9:
            predicted9.append(x1.tolist())


for i in range(2702,2965):
    y10.append(y[i])
    z1 = t1[i]
    z2 = t2[i]
    z3 = t3[i]
    z4 = t4[i]
    x1 = regr.predict([[z1, z2, z3,z4]])
    predicted10.append(x1.tolist())
        
prediction1 = [item for sublist in predicted1 for item in sublist]
prediction2 = [item for sublist in predicted2 for item in sublist]
prediction3 = [item for sublist in predicted3 for item in sublist]
prediction4 = [item for sublist in predicted4 for item in sublist]
prediction5 = [item for sublist in predicted5 for item in sublist]
prediction6 = [item for sublist in predicted6 for item in sublist]
prediction7 = [item for sublist in predicted7 for item in sublist]
prediction8 = [item for sublist in predicted8 for item in sublist]
prediction9 = [item for sublist in predicted9 for item in sublist]
prediction10 = [item for sublist in predicted10 for item in sublist]
print(len(prediction1))
print(len(prediction2))
print(len(prediction3))
print(len(prediction4))
print(len(prediction5))
print(len(prediction6))
print(len(prediction7))
print(len(prediction8))
print(len(prediction9))

final=[]
fy1=[]
fy2=[]
fy3=[]
fy4=[]
fy5=[]
fy6=[]
fy7=[]
fy8=[]
fy9=[]
fy10=[]
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
d9 = 0
d10 = 0
for i in range(0,len(prediction1)):      # Starting functioning 
    fy_1=(2.71**prediction1[i])
    fy_2=fy_1/(1+fy_1)
    fy1.append(fy_2)

for i in range(0,len(prediction2)):
    fy_1=(2.71**prediction2[i])
    fy_2=fy_1/(1+fy_1)
    fy2.append(fy_2)

for i in range(0,len(prediction3)):
    fy_1=(2.71**prediction3[i])
    fy_2=fy_1/(1+fy_1)
    fy3.append(fy_2)

for i in range(0,len(prediction4)):
    fy_1=(2.71**prediction4[i])
    fy_2=fy_1/(1+fy_1)
    fy4.append(fy_2)

for i in range(0,len(prediction5)):
    fy_1=(2.71**prediction5[i])
    fy_2=fy_1/(1+fy_1)
    fy5.append(fy_2)

for i in range(0,len(prediction6)):
    fy_1=(2.71**prediction6[i])
    fy_2=fy_1/(1+fy_1)
    fy6.append(fy_2)

for i in range(0,len(prediction7)):
    fy_1=(2.71**prediction7[i])
    fy_2=fy_1/(1+fy_1)
    fy7.append(fy_2)

for i in range(0,len(prediction8)):
    fy_1=(2.71**prediction8[i])
    fy_2=fy_1/(1+fy_1)
    fy8.append(fy_2)

for i in range(0,len(prediction9)):
    fy_1=(2.71**prediction9[i])
    fy_2=fy_1/(1+fy_1)
    fy9.append(fy_2)

for i in range(0,len(prediction10)):
    fy_1=(2.71**prediction10[i])
    fy_2=fy_1/(1+fy_1)
    fy10.append(fy_2)

for n in range(0,len(prediction1)):    # Starting comparing
    if (y1[n]-fy1[n]) <=.4:
        d1 = d1+1
final.append(d1)

for n in range(0,len(prediction2)):
    if (y2[n]-fy2[n]) <=.4:
        d2 = d2+1
final.append(d2)

for n in range(0,len(prediction3)):
    if (y3[n]-fy3[n]) <=.4:
        d3 = d3+1
final.append(d3)

for n in range(0,len(prediction4)):
    if (y4[n]-fy4[n]) <=.4:
        d4 = d4+1
final.append(d4)

for n in range(0,len(prediction5)):
    if (y5[n]-fy5[n]) <=.4:
        d5 = d5+1
final.append(d5)

for n in range(0,len(prediction6)):
    if (y6[n]-fy6[n]) <=.4:
        d6 = d6+1
final.append(d6)

for n in range(0,len(prediction7)):
    if (y7[n]-fy7[n]) <=.4:
        d7 = d7+1
final.append(d7)

for n in range(0,len(prediction8)):
    if (y8[n]-fy8[n]) <=.4:
        d8 = d8+1
final.append(d8)

for n in range(0,len(prediction9)):
    if (y9[n]-fy9[n]) <=.4:
        d9 = d9+1
final.append(d9)

for n in range(0,len(prediction10)):
    if (y9[n]-fy10[n]) <=.4:
        d10 = d10+1
final.append(d10)

print(final)
print(a)
print(aa)
print(len(final))

fin_acc=[]

for i in range(0, 9):
    m=(final[i]/299)*100
    fin_acc.append(m)

print(len(predicted10))
print(len(final))

h=(final[9]/263)*100
fin_acc.append(h)


print(fin_acc)

print(sum(fin_acc)/len(fin_acc))

g=len(prediction)
m=d1
er=(g-m)/g
print("Error rate is",er*100)
print("accuracy rate is",100-(er*100))