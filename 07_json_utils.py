import json

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    sample = {'name': 'Alice', 'age': 30}
    print(json.dumps(sample, indent=2))
