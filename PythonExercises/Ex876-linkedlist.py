# Projeto LeetCode Ex876.

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

number = int(input("Type the number of elements: "))
old_list = []
new_list = []

# Create the list
for i in range (1, number + 1):
    old_list.append(i)

new_list = old_list[round(number/2):]

print(old_list)
print(new_list)
    