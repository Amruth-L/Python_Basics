arr=list(map(int,input("Enter the numbers:").split()))
seen={}
for num in arr:
    if num in seen:
        print("duplicated number :",num)
        break
    else:
        seen[num]=1
else:
    print("no duplicate")