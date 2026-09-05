def binary_search(nums,target):
    nums.sort()
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
my_list=[1,5,4,2,3]
print(binary_search(my_list,5))