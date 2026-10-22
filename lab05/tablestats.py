


def read_rows(lines):
    rows = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(',')

    for i in range(1,len(lines)):
        if len(lines[i]) == len(lines[0]):
            rows += [dict(zip(lines[0],lines[i]))]
    return rows



def count_types(rows):
    type_counts = {}
    for row in rows:
        type1 = row['тип']
        if type1 in type_counts:
            type_counts[type1] += 1
        else:
            type_counts[type1] = 1
    return type_counts



def total_minutes(rows, kind):
    kind_time = 0.0
    for row in rows:
        if row['тип'] == kind and row['минуты'] != 'ошибка':
            kind_time += float(row['минуты'])

    return kind_time


def to_csv(counts):
    csv_text = 'тип,количество\n'
    for row in sorted(counts):
        csv_text += f'{row},{counts[row]}\n'
    return csv_text


    

