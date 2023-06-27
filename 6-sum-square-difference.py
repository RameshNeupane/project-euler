"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""


def sum_of_n_natural_nums(n: int) -> int:
    """
    Returns sum of n natural numbers.
    1 + 2 + 3 + ......... + n-1 + n = n * (n+1) / 2
    
    Parameters:
    n (int): total number of natural numbers
    
    Returns:
    (int): total sum
    """
    return n * (n+1) // 2


def sum_of_squared_n_natural_nums(n: int) -> int:
    """
    Returns sum of squares of n natural numbers 
    1^2 + 2^2 + 3^2 + ......... + (n-1)^2 + n ^2 = n * (n+1) * (2*n+1) / 6
    
    Parameters:
    n (int): total number of natural numbers
    
    Returns:
    (int): total sum
    """
    return n * (n+1) * (2*n+1) // 6

def sum_square_difference(num: int) -> int:
    """
    Returns difference between square of sum of n natural numbers and sum of square of n natural numbers.
    
    Parameters:
    num (int): total number of natural numbers
    
    Returns:
    (int): result
    """
    return sum_of_n_natural_nums(num)**2 - sum_of_squared_n_natural_nums(num)

result = sum_square_difference(100)
print(result)