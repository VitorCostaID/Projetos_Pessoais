# Projeto LeetCode Ex1342.

# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

number = int(input("Type a number: "))
counter = 0

while number != 0:
    counter += 1 
    if number % 2 == 0:
        number = number / 2
        print(f"Step {counter}: {number}")
    else:
        number -= 1
        print(f"Step {counter}: {number}")

print(f"Total of steps: {counter}")