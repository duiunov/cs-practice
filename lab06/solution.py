

def count_items(values):
    item_counts = {}
    for item in values:
        if item in item_counts:
            type_counts[item] += 1
        else:
            type_counts[item] = 1
    return type_counts