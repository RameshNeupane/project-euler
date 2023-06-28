"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


def get_product_of_special_pythagorean_triplet() -> tuple:
    """
    Returns tuple containing pythagorean triplet and product of triplet where sum of triplet is exactly 1000.
    
    Returns:
    (tuple): ((a, b, c), a * b * c) where a, b, c are the required pythagorean triplet
    """
    a = 3
    while True:
        b = a + 1
        while True:
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            if a + b + c < 1000:
                b += 1
            elif a + b + c == 1000:
                return ((a, b, c), a * b * c)
            else:
                break
        a += 1


result = get_product_of_special_pythagorean_triplet()
print(result)
