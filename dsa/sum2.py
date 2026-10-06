arr=list(int(input("Enter the numbers:")).split())
target=int(input("enter the target : "))
seen={}
for num in arr:
    complement=target-num
    if complement in seen:
        print("Pair:",complement,num)
        break

    seen[num]=1
else:
    print("No pair found")