import random
import string

def generate_password(length=12, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    print(generate_password())
    print(generate_password(16, False))
