nums=list(map(int,input("Enter the numbers : ").split(",")))
target=int(input("enter the target number : "))
def twosum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
print (twosum(nums,target))