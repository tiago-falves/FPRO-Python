def paint(n,boards):
    if n==1:
        return max(boards)
    best=sum(boards)
    for i in range(1,len(boards)-n+1):
        if max(boards[0:i])+paint(n-1,boards[i+1:])<best:
            best=max(boards[0:i])+paint(n-1,boards[i+1:])
    return best
            
print(paint(2,[60, 70, 10, 20, 40, 50, 10, 40]))
def paint(n,boards):
    if n==1:
        return max(boards)
    best=sum(boards)
    for i in range(len(boards)-n):
        best=min(best,max(boards[:i+1])+paint(n-1,boards[i+1:]))
    return best