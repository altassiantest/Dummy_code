import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def is_valid_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    emails = ['test@example.com', 'invalid.email', 'user@domain.co']
    for e in emails:
        print(f'{e}: {is_valid_email(e)}')
