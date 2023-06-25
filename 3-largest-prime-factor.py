"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def is_prime_number(num: int)-> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_largest_prime_factor(num: int) -> int:
	i = 2
	while i < num:
		if is_prime_number(i):
			if num % i == 0:
				num //= i
			else:
				i += 1
		else: 
			i += 1
	return num

number = 600851475143
result = get_largest_prime_factor(number)
if result == number:
    print(f"{number} is prime number itself.")
else:
    print(f"Largest prime factor of {number} is {result}.")