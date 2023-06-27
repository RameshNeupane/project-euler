"""
2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (i.e. divisible with no remainder)
by all of the numbers from 1 to 20?
"""

from typing import List

def mul_arr_elems(arr: List[int]) -> int:
    """
    Returns a number after multiplying all elements from array 'arr'.
    
    Parameters:
    arr (List(int)): input array, list of integers
    
    Retuns:
        result (int): number after multiplying all elements from arr
    """
    result = 1
    for elem in arr:
        result *= elem
    return result


def get_prime_list(num: int) -> List[int]:
    """
    Returns list of prime numbers (can be repeated) and by multiplying numbers from 
    list to make numbers less than or equal to 'num'.
    
    Parameters:
    num (int): input number
    
    Returns:
    prime_list (List(int)): sorted list of prime numbers
    """
    prime_list = [2]
    for i in range(3, num+1):
        temp = i
        for prime in prime_list:
            if temp % prime == 0:
                temp //= prime
        prime_list.append(temp)
    prime_list = [elem for elem in prime_list if elem != 1]
    prime_list = sorted(prime_list)
    return prime_list

def get_evenly_divisible(num: int) -> int:
    """
    The smallest positive number that is evenly divisible (i.e. divisible with no remainder)
    by all of the numbers from 1 to 'num'
    
    Parameters:
    num (int): input number
    
    Returns:
    (int): output number
    """
    prime_list = get_prime_list(num)
    return mul_arr_elems(prime_list)

result = get_evenly_divisible(20)
print(result)

