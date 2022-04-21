from collections import Counter
from typing import Dict, List

def most_frequent(List) -> int:
    """return the most frequent element inside a list."""
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def get_json_values(key,input_data) -> List:
    """return the values of dicts inside a list."""
    return [sub_val[key] for sub_val in input_data if key in sub_val]

def max_dict_value(List,key) -> List:
    """return the key that is linked to the most frequent value."""
    counts = dict()
    for dictionary in List:
        counts[dictionary[key]] = counts.get(dictionary[key],0) + 1
    max_keys = [key for key, value in counts.items() if value == max(counts.values())]
    return max_keys

def get_max_dict(List,key) -> List:
    """return the dictionary that maps to the max_dict_value."""
    for dictionary in List:
        if dictionary[key] == max_dict_value(List,key)[0]:
            return dictionary
