def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def count_lines(path):
    content = read_file(path)
    if content is None:
        return 0
    return len(content.splitlines())

if __name__ == '__main__':
    print(count_lines(__file__))
