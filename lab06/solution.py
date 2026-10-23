

values = ["ошибка", "запуск", "ошибка", "проверка"]

def count_items(values):
    item_counts = {}
    for item in values:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts


def unique_sorted(values):
    return set(sorted(count_items(values)))


# print(count_items(values))
# print(unique_sorted(values))