"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def get_sum_of_multiple_of_3_or_5(range_num: int)-> int:
    """
    Returns sum of multiples of 3 or 5 below input 'range_num'.
    
    Parameters:
    range_num (int): input number for upper range to calculate get multiples of 3 or 5
    
    Returns:
    (int): output i.e. sum of multiples of 3 or 5
    """
    if range_num < 3:
        return 0
    else:
        return sum([num for num in range(3, range_num) if num % 3 == 0 or num % 5 == 0])

result = get_sum_of_multiple_of_3_or_5(1000)
print(result)