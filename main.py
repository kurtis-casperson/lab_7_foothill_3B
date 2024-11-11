
# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

# Order Number    Book Title and Author              Quantity     Price per Item
# 34587           Learning Python, Mark Lutz             4          40.95
# 98762           Programming Python, Mark Lutz          5          56.80
# 77226           Head First Python, Paul Barry          3          32.95
# 88112           Einführung in Python3, Bernd Klein     3          24.99

# Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and 
# the product of the price per item and the quantity. The product should be increased by $10 if the value of 
# the order is smaller than $100,00. Your Python program must use lambda and map.


orders = [
    (1, 30, 2),  
    (2, 25, 5),  
    (3, 15, 5)  
]


result = list(map(lambda order: (order[0], (order[1] * order[2]) + 10 if order[1] * order[2] < 100 else order[1] * order[2]), orders))

"""
I used the slice method to create 2 tuples in the list. Otherwise I had a hard time trying figure out how to 
use lambda and map to have two tuples in the list
"""

print(result[:2])
