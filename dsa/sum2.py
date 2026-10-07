arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for num in arr:
    complement = target - num

    if complement in seen:
        print("Pair:", complement, num)
        break

    seen[num] = 1

else:
    print("No pair found")