def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

if __name__ == '__main__':
    print('Add:', add(5, 3))
    print('Sub:', subtract(5, 3))
    print('Mul:', multiply(5, 3))
    print('Div:', divide(5, 3))
