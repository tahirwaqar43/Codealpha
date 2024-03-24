# Created by Waqar Tahir
# Created on 25th March 2024
fibRange = int(input('Enter Range of Fibonacci '))
def generate_fibonacci(n):
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
        yield num1
print(list(generate_fibonacci(fibRange)))
