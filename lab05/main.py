from tablestats import read_rows, count_types




path = input() # 'events.csv' 

lines = []

with open(path , encoding="utf-8") as table:
    rows = table
    
    for i in rows:
        lines += [i[:-1]]

    
print(lines)
rows = read_rows(lines)
type_counts = count_types(rows)
print(rows)
# print(type_counts)
print(len(rows))

err = 0
tip = []
for i in range(1,len(lines)):
    if len(lines[i]) > 1:
        tip += [lines[i][1]]
        
        if lines[i][1] == 'ошибка':
            err += float(lines[i][2])

print(len(set(tip)))
print(err)






