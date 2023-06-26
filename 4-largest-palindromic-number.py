"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome_number(num: int) -> bool:
    """
    Returns true if the input 'num' is palindrome else return false.
    
    Parameters:
    num (int): input number
    
    Returns:
    bool: True or False
    """
    temp_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10
    if reversed_num == temp_num:
        return True
    else:
        return False

def get_largest_palindrome() -> int:
    """
    Returns largest palindrome made from the product of two 3-digit numbers.
    """
    num_1 = None
    num_2 = None
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            num = i * j
            if is_palindrome_number(num) and num > largest_palindrome:
                largest_palindrome = num
                num_1 = i
                num_2 = j
    return (largest_palindrome, f'{num_1} * {num_2}')

result = get_largest_palindrome()
print(result)