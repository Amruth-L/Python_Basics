arr = list(map(int, input("Enter numbers: ").split()))

freq = {}

# Count frequency
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Find first number with frequency
for num in arr:
    if freq[num] == 1:
        print("First non-repeating number:", num)
        break
else:
    print("No non-repeating number")