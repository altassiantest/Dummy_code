def factorial(n):
    if n < 0:
        raise ValueError('Factorial not defined for negatives')
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    for i in range(6):
        print(f'{i}! = {factorial(i)}')
