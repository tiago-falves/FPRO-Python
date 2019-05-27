
def sort_by_field(filename, field):
    
    result = ''
    
    with open(filename, 'r') as f:
        
        content = f.read()
        
    content = content.split('\n')
        
    a = content[0].split(',')
    content.remove(content[0])
    
    for i in range(len(content)):
        content[i] = content[i].split(',')
    
    content = sorted(content, key = lambda x: x[a.index(field)])
        
    for i in range(len(content)):
        content[i] = ','.join(content[i])
        content[i] = [content[i]]

    a = ','.join(a)
    content.append([a])
    content = content[len(content) - 1] + content[:len(content) - 1]

    for i in content:
        for n in i:
            result += n
        result += '\n'
    return result
