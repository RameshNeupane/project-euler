"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

def is_prime_number(num: int) -> bool:
    """
    Returns True if input 'num' is prime number else False.
    
    Parameter:
    num (int): input number
    
    Returns:
    (bool): True or False
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nth_prime_number(position: int) -> int:
    """
    Returns prime number at the position input 'position'.
    
    Parameters:
    position (int): input position for the prime number
    
    Returns:
    (int): prime number at the input 'position' 
    """
    num = 2
    count_prime_nums = 0
    while True:
        if is_prime_number(num):
            count_prime_nums += 1
            if count_prime_nums == position:
                break
            else:
                num += 1
        else:
            num +=1
    return num

result = nth_prime_number(10001)
print(result)