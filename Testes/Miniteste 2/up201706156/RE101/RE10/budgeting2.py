# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:42:43 2018

@author: joao

5)
In RE09, the budget was not enough to pay for entire wishlist and the proposed algorithm was
to remove the cheapest items first until cost ≤ budget. This, however, wasn't the optimal
solution. Imagine that my budget is 1000 and I want to buy 2 laptops (each costs 2000) and 3
jeans (50). The previous algorithm would decide not to buy anything, not even the jeans,
because it would end up removing everything from the wishlist.
We may use another approach: the knapsack problem (problema da mochila) is a famous
problem from computer science. We have a fixed budget and we want to buy as much as we
can to fit the budget. In this version of the knapsack problem, there is a benefit proportional to
the cost as long as the product is in the wishlist.
Write a Python function budgeting2(budget, products, wishlist) that receives an
integer indicating the budget, a products dictionary showing the price of each item, and a
wishlist dictionary indicating how much quantity we want of each product. Your goal is to
spend as much of your budget as you can, without going over the budget.
Save the program in a file called budgeting2.py
For example:
● budgeting2(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,
'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1})
returns the dictionary: {‘pc’: 1, 'smartphone': 1}
● budgeting2(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,
'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1,
'xbox': 1}) returns the dictionary: {'xbox': 1, 'pc': 1, 'jeans': 2,
'glasses': 3}
● budgeting2(1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2,
'jeans': 3}) returns the dictionary: {'jeans': 3}
"""
def budgeting2(budget, products, wishlist):
    
    def buy(budget, n):
        print(n)
        if n == 0 or budget == 0:
            result = budget
        elif price[n] > budget:
            result = buy(budget,n-1)
        else:
            yes = buy(budget-price[n],n-1)
            no = buy(budget-price[n],n-1)
            result = min(yes,no)
#            if result is yes:
#                print('yes')
            bought.append(n)
#             result = bought
            print(bought)
#                print(budget - price[n])
        return result

    result = {}
    price = [0]
    prod = [0]
    for item,i in wishlist.items():
        times_price = [products[item]] * i        
        times_prod = [item] * i        
        price += times_price
        prod += times_prod
    print(price)
    print(prod)
    n = len(price) - 1
    bought = []
    buy(budget,n)
    new_bought = []
    for i in bought:
        for j in bought:
            if j in new_bought:
                continue
            new_bought.append(j)
    for n in new_bought:
        result[prod[n]] = result.get(prod[n],0) + 1 
    return result
    
#print(budgeting2(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
#print(budgeting2(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1,'xbox': 1}))
print(budgeting2(1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2,'jeans': 3}))
