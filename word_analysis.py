import string
from collections import Counter

def analyze_text(text):
    list_text = [word.strip(string.punctuation).lower() for word in text.split()]
    counter = Counter(list_text)
    
    return {
        'unique_count': len(counter),
        'repeated_words': sorted([word for word, count in counter.items() if count > 1]),
        'palindromes': sorted([word for word in counter if word == word[::-1]])
    }