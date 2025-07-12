a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if (a==b==c):
    print("All the numbers are same")
else:
    if (a>b and a>c):
       print("The Gretest number is: ",a) 
    elif(b>a and b>c):
        print("The Gretest number is: ",b)
    else:
        print("The Gretest number is: ",c) 

pos=0
neg=0
if(a>0 or b>0 or c>0):
    pos+=1
if(a<0 or b<0 or c<0):
    neg+=1
if(pos>0 and neg>0):
    print("The combination of both")  
elif(pos>0):
    print("All positive") 
elif(neg>0):
    print("All negetive") 