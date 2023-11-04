
class Vector():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __abs__(self):
        return(self.x**2+self.y**2+self.z**2)**0.5
    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x + other.x,self.y + other.y,self.z + other.z)
        elif isinstance(other,int) or isinstance(other,float):
            return Vector(self.x + other,self.y + other,self.z + other)
    def __sub__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x - other.x,self.y - other.y,self.z - other.z)
        elif isinstance(other,int) or isinstance(other,float):
            return Vector(self.x - other,self.y - other,self.z - other)
    def __mul__(self,other):
        if isinstance(other,Vector):
            return Vector(self.y * other.z - self.z * other.y, self.z * other.x-self.x * other.z,self.x * other.y-self.y * other.x)
        elif isinstance(other,int) or isinstance(other,float):
            return Vector(self.x * other,self.y * other,self.z * other)
    def __rmul__(self,other):
        if isinstance(other,Vector):
            return Vector(self.y * other.z - self.z * other.y, self.z * other.x-self.x * other.z,self.x * other.y-self.y * other.x)
        elif isinstance(other,int) or isinstance(other,float):
            return Vector(self.x * other,self.y * other,self.z * other)
    def __radd__(self,other):
        return self + other
    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
