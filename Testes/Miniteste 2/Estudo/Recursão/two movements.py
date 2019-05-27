def reach_two_steps(sx,sy,dx,dy):
    if (sx+sy==dx and sy==dy) or (sx==dx and dy==sx+sy) or(sx==dx and sy==dy):
        return True
    if sx>dx or sy>dy:
        return False
    return reach_two_steps(sx+sy,sy,dx,dy) or reach_two_steps(sx,sx+sy,dx,dy)
source_x, source_y = 2, 10
dest_x, dest_y = 26, 12
if (reach_two_steps(source_x, source_y, dest_x, dest_y)): 
    print("True") 
else: 
    print("False") 