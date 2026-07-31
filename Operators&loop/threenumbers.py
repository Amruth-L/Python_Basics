a=int(input("enter the number 1:"))
b=int(input("enter the nmuber 2"))
c=int(input("enter the number 3"))
if a==b==c:
    print("All the number are equal")
elif a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greated")
elif c>=a and c>=b:
    print("c is greater")