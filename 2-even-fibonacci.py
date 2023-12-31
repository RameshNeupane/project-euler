"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibonacci(n):
    if n <= 1:
        return 1
    fib1 = fibonacci(n-1)
    fib2 = fibonacci(n -2)
    return fib1 + fib2

sum = 2
n = 3
print("Even-numbered fibonacci (<=4000000):")
while(True):
    fib_num = fibonacci(n)
    if fib_num <= 4000000:
        if fib_num % 2 == 0:
            print(fib_num, end='\t')
            sum += fib_num
        n += 1
    else: break
print(f'\nSum: {sum}\n')
