import csv
import pandas as pd

PAND = pd.read_csv('../csv/23.csv')

# print(PAND['col2'])
x =[]
for i in PAND['X1']:
    x.append(i)
print(x)


x =[]
for i in PAND['X2']:
    x.append(int(i))
print(x)
x =[]
for i in PAND['X3']:
    x.append(int(i))
print(x)
x =[]
for i in PAND['Y']:
    x.append(int(i))
print(x)