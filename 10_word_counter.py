from collections import Counter

def word_count(text):
    words = text.lower().split()
    return Counter(words)

def most_common(text, n=5):
    return word_count(text).most_common(n)

if __name__ == '__main__':
    sample = 'the quick brown fox jumps over the lazy dog the fox is quick'
    print(most_common(sample))
