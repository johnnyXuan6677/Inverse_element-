# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=101
p=4620
X=[]
Y=[]
Z=[]
X.insert(0,p//a)
Y.insert(0,p%a)
X.insert(1,a//Y[0])
Y.insert(1,a%Y[0])

for i in range(p):
    if Y[i-1]==1 or Y[i-1]==0:
        break
    else:   
        X.insert(i,Y[i-2]//Y[i-1])
        Y.insert(i,Y[i-2]%Y[i-1])
        if Y[i]==1:
            break
X.insert(0,p//a)
Y.insert(0,p%a)
X.insert(1,a//Y[0])
Y.insert(1,a%Y[0]) 
numX=len(X)
numY=len(Y)
if Y[1]==1:
    Z.insert(0,X[numX-3]*X[numX-4]+1)    #Z[0]=1*X[numX-4]+1
else:
    Z.insert(0,X[numX-3]*X[numX-4]+1)    #Z[0]=1*X[numX-4]+1
    Z.insert(1,Z[0]*X[numX-5]+Y[numX-3]) #Z[1]=Z[0]*X[numX-5]+Y[numY-3]
    for i in range(numY-5):
        Z.insert(i+2,Z[i+1]*X[numX-(i+6)]+Z[i])
    
    
print(Z)

print('此數值的反元數',Z[-1])
print("結束")
