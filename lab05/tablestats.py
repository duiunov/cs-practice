


def read_rows(lines):
    rows = []
    for i in range(1,len(lines)):
        if len(lines[i]) > 1:
            rows += [dict(zip(lines[0],lines[i]))]
    return rows


    

