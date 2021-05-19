import csv
import math

with open("data.csv",newline="")as f:
    fileData=csv.reader(f)
    DataList=list(fileData)
    print(DataList)
     
newList=DataList[0]

total=0

for i in newList:
    total=total+int(i)

number = len(newList)
mean = total / number
print(mean)  

n = number-1
squareList=[]
for num in newList:
    sub =int(num)-mean
    sub = sub **2
    squareList.append(sub)

print(squareList)
sum=0
for s in squareList:
    sum=sum+s
    
result = sum / n
standardDaviation=math.sqrt(result)
print(" standardDaviation " + str(standardDaviation))
