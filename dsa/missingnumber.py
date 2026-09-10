arr=list(map(int,input("Enter the numbers:").split()))
n=len(arr)+1
expected_sum=n * (n+1) //2 - sum(arr)
print("The missing number is ",expected_sum)