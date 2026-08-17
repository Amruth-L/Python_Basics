# nums=list(map(int,input("Enter the numbers : ").split(",")))
# target=int(input("enter the target number : "))
# def twosum(nums,target):
#     n=len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# print (twosum(nums,target))
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
nums=[2,7,11,15]
target=9
result=twosum(nums,target)
print(result)
