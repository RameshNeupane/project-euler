"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def is_prime_number(num: int) -> bool:
    """
    Returns True if input 'num' is prime number else False.

    Parameter:
    num (int): input number

    Returns:
    (bool): True or False
    """
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def sum_of_primes(stop_at: int) -> int:
    """
    Returns sum of all prime numbers below the input 'stop_at'.

    Parameters:
    stop_at(int): input number

    Returns:
    (int): summation of primes
    """
    sum = 2
    for num in range(3, stop_at):
        if num % 2 == 0:
            continue
        if is_prime_number(num):
            sum += num
            print(num, sum)
    return sum


result = sum_of_primes(stop_at=2000000)
print(result)
