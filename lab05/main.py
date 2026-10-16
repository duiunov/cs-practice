from tablestats import read_rows


##  'events-small.csv'

path = 'events-small.csv' # input()

f = []

with open(path , encoding="utf-8") as table:
    rows = table
    
    for i in rows:
        f += [i[:-1].split(',')]


##for i in f:
##    print(i)
    
print(read_rows(f))



