from tablestats import read_rows, count_types, total_minutes, to_csv




path = input() # 'events.csv'

lines = []

with open(path , encoding="utf-8") as table:
    rows = table
    
    for i in rows:
        lines += [i[:-1]]

    
# print(lines)
rows = read_rows(lines)
type_counts = count_types(rows)
total = total_minutes(rows,'запуск')



err = 0
tip = []

for i in range(1,len(lines)):
    if len(lines[i]) > 1:
        if lines[i][1] == 'ошибка':
            err += float(lines[i][2])

print(len(rows))
print(len(type_counts))
print(err)






