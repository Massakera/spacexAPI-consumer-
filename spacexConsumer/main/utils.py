from collections import Counter

def most_frequent(List) -> int:
    """function returning the most frequent element inside a list."""
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]