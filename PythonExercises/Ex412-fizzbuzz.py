# Projeto LeetCode Ex412.

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

fizzbuzz = "Fizz Buzz"
number = int(input("Type an number: "))
fizz_list = []

for i in range (1, number+1):
    if i % 3 == 0 and i % 5 == 0:
        fizz_list.append(fizzbuzz)
    elif i % 3 == 0:
        fizz_list.append(fizzbuzz[:4])
    elif i % 5 == 0:
        fizz_list.append(fizzbuzz[-4:])
    else:
        fizz_list.append(i)

print(fizz_list)

