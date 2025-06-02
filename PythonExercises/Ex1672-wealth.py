# Projeto LeetCode Ex1672.

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

accounts = [[1, 4, 6], [7, 1, 3], [9, 1, 1]]

wealthiest = 0

for i in range(0, len(accounts)):
    wealth = 0

    for j in range(len(accounts[i])):
        wealth += accounts[i][j]
        if wealth > wealthiest:
            wealthiest = wealth
    
print(wealthiest)