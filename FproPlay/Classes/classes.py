#class Point:
#    def __init__(self):
#        self.x=0
#        self.y=0
class Point:
    def __init__(self,x=0,y=0):
        """ Create a new point at x, y """
        self.x=x
        self.y=y
        
p=Point()
q=Point()
#print(p.x,p.y,q.x,p.y)
#p.x=3
#p.y=4
#print(p.x,p.y,q.x,p.y)
#a=Point()
#print(a.x)
p=Point(4,2)
q=Point(6,3)
r=Point()
print(p.x,q.y,r.x)