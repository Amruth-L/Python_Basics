arr = list(map(int, input("Enter numbers: ").split()))

left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1

print("Array after moving zeros:", arr)