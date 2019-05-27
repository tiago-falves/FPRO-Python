def cut(filename, delimiter, field):
    if type(field) != list: field = [field]
    field = [x-1 for x in field]
    with open(filename,'r') as f:
        lines = f.readlines()
        result = ""
        for i in lines:
            x = i.strip().split(delimiter)
            result += x[field[0]]
            for j in field[1:]:
                result += delimiter + x[j]
            result += "\n"
        return result[:-1]
            
