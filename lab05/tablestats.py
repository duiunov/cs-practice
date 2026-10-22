


def read_rows(lines):
    rows = []
    for i in range(len(lines)):
        line = []
        lines[i] = lines[i].split(',')

        for j in range(len(lines[i])):
            line += [lines[i][j].strip()]

        lines[i] += line



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
    print(0.0)
    kind_time = 0.0
    for row in rows:

        def to_float(s):
            try:
                return float(s)
            except valueerror:
                return 0.0

        if row['тип'] == kind and row['минуты']:
            kind_time += to_float((row['минуты']).strip().replace(",", "."))

    return round(kind_time,1)


def to_csv(counts):
    csv_text = 'тип,количество\n'
    for row in sorted(counts):
        csv_text += f'{row},{counts[row]}\n'
    return csv_text


    

