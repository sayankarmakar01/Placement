a=int(input("Enter 1st angle"))
b=int(input("Enter 2ns angle"))
c=int(input("Enter 3rd angle"))

total=a+b+c
if(total==180):
    if(a<90 and b<90 and c<90):
        print("Acute-Angled Triangle")
    elif(a==90 or b==90 or c==90):
        print("Right-Angled Triangle")
    elif((a>90 and a<180) or (b>90 and b<180) or (c>90 and c<180)):
        print("Obtuse-Angled Triangle")
else:
    print("Triangle is Not Possible")