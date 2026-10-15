
arr = [10, 5, 20, 8, 20, 15]

largest = arr[0]

# Step 1: Find the largest element
for num in arr:
    if num > largest:
        largest = num

second = None

# Step 2: Find the largest element smaller than largest
for num in arr:
    if num < largest:
        if second is None or num > second:
            second = num

if second is None:
    print("No second-largest distinct element")
else:
    print(second)
