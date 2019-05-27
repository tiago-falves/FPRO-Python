"""
5. Minimum path
Write a function min_path(matrix, a, b, visited=[]) that discovers the minimum path
between a and b inside the matrix maze without going through visited twice. Positions a
and b are tuples (line, column), matrix is a matrix of booleans with False indicating no
obstacle and True indicating an obstacle and visited is a list of visited tuples. Valid
movements include all 8 adjacent tiles.
For the maze of the following figure, a minimum path between a and b, in yellow, is 4:
b
a
Save the program in the file min_path.py inside the folder PE3.
For example:
 mx = [
[False]*4,
[False, True, False, False],
[False, True, False, False],
[False]*4
]
 min_path(mx, (2, 0), (0, 3)) returns the integer 4
 min_path(mx, (3, 1), (0, 1)) returns the integer 3
 min_path(mx, (0, 0), (3, 3)) returns the integer 4
"""
inf = 1e100
def min_path(matrix, a, b, visited=[]):
    if (a[0]<0 or len(matrix   ) <= a[0] or a[1]<0 or len(matrix[0]) <= a[1]):
        return inf
    if a in visited:
        return inf
    if matrix[a[0]][a[1]]:
        return inf
    if a == b:
        return 0
    
    visited.append(a)
    
    potNW = (a[0]-1, a[1]-1); potNN = (a[0], a[1]-1); potNE = (a[0]+1, a[1]-1)
    potWW = (a[0]-1, a[1]  );                         potEE = (a[0]+1, a[1]  )
    potSW = (a[0]-1, a[1]+1); potSS = (a[0], a[1]+1); potSE = (a[0]+1, a[1]+1)
    
    l = [potNW, potNE,\
         potSW, potSE,\
         potNN, potWW, potEE, potSS]
    r = inf
    for t in l:
        r = min(r, min_path(matrix, t, b, visited[:]))
    return r+1
"""
mx = [\
      [False]*4,\
      [False, True, False, False],\
      [False, True, False, False],\
      [False]*4\
     ]

print(min_path(mx, (2, 0), (0, 3)))
print(min_path(mx, (3, 1), (0, 1)))
print(min_path(mx, (0, 0), (3, 3)))
"""
