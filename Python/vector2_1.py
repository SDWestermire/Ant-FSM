import math

class Vector22():

    def __init__ (self, x=0.0, y=0.0, name=""):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return"(%s, %s, %s)"%(self.x, self.y, self.name)

    def return_self(self):
        return (self.x,self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0] - P1[0], P2[1]- P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    
        
A = ( 10.0, 20.0,'start')
B = ( 30.0, 50.0,'end')
print("Vector A:  ",A)
print("Vector B:  ",B)

print(A[2] == 'start')


AB = Vector22.from_points(A, B)
print("Vector AB is ", AB)
AB.normalize()

print("Vector AB Normalized is ", AB)




