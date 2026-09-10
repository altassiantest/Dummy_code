from datetime import datetime, timedelta

def days_between(d1, d2):
    fmt = '%Y-%m-%d'
    a = datetime.strptime(d1, fmt)
    b = datetime.strptime(d2, fmt)
    return abs((b - a).days)

def add_days(date_str, days):
    fmt = '%Y-%m-%d'
    d = datetime.strptime(date_str, fmt)
    return (d + timedelta(days=days)).strftime(fmt)

if __name__ == '__main__':
    print(days_between('2024-01-01', '2024-12-31'))
    print(add_days('2024-01-01', 100))
