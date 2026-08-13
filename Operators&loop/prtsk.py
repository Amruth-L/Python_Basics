1. Print number form 1 to 20
for i in range(1,21):
    print(i)

2. print odd number from 1 to 50 
for i in range (1,50):
    if i%2!=0:
        print(i)

3.print multiplication table of a number enterd by the user 
num=5
for i in range(1,11):
    print(f"The multiplication of {num}*{i}=",num*i)

4.find the sum of numbers from 1 to 100
total=0
for i in range(1,101):
    total=total + i
    print(total)

5. Find how many numbers between 1 and 100 are divisible by 3

for i in range(1,101):
        if i%3==0:
            print(i)

#6. Print the squared number
for i in range(1,11):
    sq=i**2
    print(sq)