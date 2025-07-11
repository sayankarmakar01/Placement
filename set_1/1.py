import math
l=int(input("Enter Length: "))
b=int(input("Enter Breadth: "))

area=l*b
perimeter=2*(l+b)
diagonal=math.sqrt(l**2+b**2)
print("The Area of Rectangle is: ",area,"\nThe Perimeter of Rectangle is: ",perimeter,"\nThe Diagonal of Rectangle is: ",diagonal)