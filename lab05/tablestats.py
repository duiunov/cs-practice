


def read_rows(lines):
    rows = []
    for i in range(1,len(lines)):
        if len(lines[i]) > 1:
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




    

