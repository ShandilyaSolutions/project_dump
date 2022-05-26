#COLLATZ's Conjecture
hailstone_numbers = []
stopping_time = 0
loop = [4,2,1]
num = int(input("Enter the number here :    "))
n = num
while num > 4:
    hailstone_numbers.append(num)
    stopping_time = stopping_time + 1
    if num % 2 == 1:
        num = (num*3)+1
    elif num % 2 == 0:
        num = num / 2 
if num == 4:
    hailstone_numbers.append(loop)
    stopping_time = stopping_time + 3

print(" For the number ", n," :")
print("Total Stopping time is   :  ", stopping_time)
print("List of Hailstone number is  :   ",hailstone_numbers)
