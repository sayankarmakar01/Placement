import math
n=int(input("Enter the number: "))

count=0
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        count+=1
if count>0:
    print("Not Prime")
else:
    print("Prime")