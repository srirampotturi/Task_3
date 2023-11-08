class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
cal=Calculator()
while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    ch=int(input("Enter your choice :"))
    a=float(input("Enter First number:"))
    b=float(input("Enter Second Number:"))
    if ch==1:
        x=cal.add(a,b)
        print(x)
    elif ch==2:
        print(cal.sub(a,b))
    elif ch==3:
        print(cal.mul(a,b))
    elif ch==4:
        x=cal.div(a,b)
        print(format(x,".2f"))
    else:
        print("Invalid choice")
    c=input("Do you want continue?(Yes/No): ")
    if c=="yes" or c=='yes':
        continue
    else:
        print("Thanks for using!")