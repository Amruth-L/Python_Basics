arr=list(map(int,input("Enter the numbers: ").split()))
index_sum=0
for i in range(len(arr)):
    num=arr[i]
    if num<2:
        continue
    is_prime=True

    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            is_prime=False
            break
    if is_prime:
        index_sum+=i
    print("sum of prime indices:",index_sum)