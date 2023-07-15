import pandas as pd
data = pd.read_csv(r"C:\Users\hp\Downloads\college placement 05.csv" )
y = data['PlacedOrNot'].to_list()
x1 = data['Internships'].to_list()
x2 = data['CGPA'].to_list()
x3 = data['HistoryOfBacklogs'].to_list()
x4 = data['Hostel'].to_list()

x1tr = x1[:2076]
x2tr = x2[:2076]
x3tr = x3[:2076]
x4tr = y[:2076]
ytr = y[:2076]


x1tr_mean = (sum(x1tr)/len(x1tr))
# print(x1tr_mean)
x2tr_mean = (sum(x2tr)/len(x2tr))
# print(x2tr_mean)
x3tr_mean = (sum(x3tr)/len(x3tr))
# print(x3tr_mean)
x4tr_mean = (sum(x4tr)/len(x4tr))
# print(x4tr_mean)
ytr_mean = (sum(ytr)/len(ytr))
# print(ytr_mean)


x1te = x1[2076:]
x2te = x2[2076:]
x3te = x3[2076:]
x4te = x4[2076:]
yte = y[2076:]


s1 = []
s2 = []

for i in range(0, 2076):
    sum1 = ((x1tr[i] - x1tr_mean) * (ytr[i] - ytr_mean))
    s1.append(sum1)


for i in range(0, 2076):
    sum2 = (x1tr[i] - x1tr_mean)**2
    s2.append(sum2)


b1 = sum(s1)/sum(s2)
# print(b1)

s3 = []
s4 = []

for i in range(0, 2076):
    sum3 = ((x2tr[i] - x2tr_mean) * (ytr[i] - ytr_mean))
    s3.append(sum3)


for i in range(0, 2076):
    sum4 = (x2tr[i] - x2tr_mean)**2
    s4.append(sum4)

b2 = sum(s3)/sum(s4)




s5 = []
s6 = []

for i in range(0, 2076):
    sum5 = ((x3tr[i] - x3tr_mean) * (ytr[i] - ytr_mean))
    s5.append(sum5)


for i in range(0, 2076):
    sum6 = (x3tr[i] - x3tr_mean)**2
    s6.append(sum6)

b3 = sum(s5)/sum(s6)


s7 = []
s8 = []

for i in range(0, 2076):
    sum7 = ((x4tr[i] - x4tr_mean) * (ytr[i] - ytr_mean))
    s7.append(sum7)

for i in range(0, 2076):
    sum8 = (x4tr[i] - x4tr_mean)**2
    s8.append(sum8)

b4 = sum(s7)/sum(s8)

yl = []

for i in range(0, 519):
    y1 = (b1)+(b2*x2te[i])+(b3*x3te[i])+(b4*x4te[i])
    yl.append(y1)

print(yl)

fy=[]
for i in range(0,len(yl)):
    fy1=(2.71**yl[i])
    fy2=fy1/(1+fy1)
    fy.append(fy2)

print(len(fy))

d1 = 0
for n in range(0,len(yl)):
    if (y[n]-yl[n]) >=.5:
        d1 = d1+1
print(len(yl))
print(d1)