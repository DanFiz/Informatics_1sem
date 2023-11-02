import numpy as np
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
print('Упражнение 1')
print('Введите вектор в формате: x y z')
x1,y1,z1 = map(float,input().split())
v1=Vector(x1,y1,z1)
print('Введите второй объект в формате: "x y z" или "b", где x y z координаты точки, а b число')
A=list(map(float,input().split()))
if len(A)==1:
    b=A[0]
else:
    x2, y2, z2 = A[0], A[1],A[2]
    b=Vector(x2, y2, z2)
print('Какую операцию провести с этими данными (умножение векторное): -,+,*?')
oper=input()
if oper == '-':
    print(f'Ответ: {v1-b}')
elif oper == '+':
    print(f'Ответ: {v1+b}')
else:
    print(f'Ответ: {v1*b}')
print('Упражнение 1.1 и 1.2')
print('Введите количество точек для рассчёта центра масс и площади')
n=int(input())
print('Вводите координаты точек и массы этих точек через Enter по образцу: x y z m')
M=0
V=[]
c=Vector(0,0,0)
for i in range(n):
    A=list(map(float,input().split()))
    v=Vector(A[0],A[1],A[2])
    m=A[3]
    V.append(v)
    c += v*m
    M+=m
M0=1/M
C=c*M0
s=0
S=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            S=abs((V[j]-V[i])*(V[k]-V[i]))
            if S>s:
                s=S
            S=0
print(f'1.1 Центр масс: {C}')
print(f'1.2 Треугольник с максимальной площадью: {s}')