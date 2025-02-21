import math
class Vector:
        def __init__(self, *components):
            self.components = tuple(components)  # Store components as a tuple for immutability
        def __str__(self):
            return f"Vector{(self.components)}"
        def checking_dimensions(self, other):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for this operation!")
        def __add__(self,other):
            self.checking_dimensions(other)
            return Vector(*(a + b for a, b in zip(self.components, other.components)))
        def __sub__(self,other):
            self.checking_dimensions(other)
            return Vector(*(a - b for a, b in zip(self.components, other.components)))   
        def __mul__(self,other):
            self.checking_dimensions(other)
            return sum(a * b for a,b in zip(self.components, other.components))   
        def scalar_mul(self,number):
            return Vector(*(number * a for a in self.components))
        def magnitude(self):
            return math.sqrt(sum(a**2 for a in self.components))  
        def normalize(self):
            return Vector(*(round(a / self.magnitude(),3) for a in self.components))     
