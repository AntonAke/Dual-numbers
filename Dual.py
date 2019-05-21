import math

class Dual:
    real = 0
    dual = 0
    
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual

    def getReal(self):
        return self.real

    def getDual(self):
        return self.dual

    #converts a number to a dual number with inifinitesimal part 0
    def convert(num):
        if not isinstance(num, Dual):
            return Dual(num, 0)
        else:
            return num
        
    #Determines how dual numbers are represented as string
    def __repr__(self):
        return (str(self.real) + (" + " if self.dual>=0 else " - ")
                + str(abs(self.dual)) + u'\u03B5')

    """Overloading of basic arithmetic operations,
    both from left and right"""
    def __add__(self, other):
        other = Dual.convert(other)
        return Dual(self.real+other.real, self.dual + other.dual)

    def __radd__(self,other):
        other = Dual.convert(other)
        return Dual(self.real+other.real, self.dual + other.dual)

    def __sub__(self, other):
        other = Dual.convert(other)
        return Dual(self.real-other.real, self.dual - other.dual)

    def __rsub__(self, other):
        other = Dual.convert(other)
        return Dual(other.real-self.real, other.dual - self.dual)

    def __mul__(self, other):
        other = Dual.convert(other)
        return Dual(self.real*other.real,
                    self.dual*other.real + self.real*other.dual)

    def __rmul__(self, other):
        other = Dual.convert(other)
        return Dual(self.real*other.real,
                    self.dual*other.real + self.real*other.dual)

    def __truediv__(self, other):
        other = Dual.convert(other)
        return Dual(self.real/other.real,
                    (self.dual*other.real-self.real*other.dual)/
                    (other.real**2))    

    def __rtruediv__(self, other):
        other = Dual.convert(other)
        return Dual(other.real/self.real,
                    (other.dual*self.real-other.real*self.dual)/
                    (self.real**2))    

    #Elementary functions
    def sin(one):
        return Dual(math.sin(one.real), one.dual*math.cos(one.real))

    def cos(one):
        return Dual(math.cos(one.real), - one.dual*math.sin(one.real))

    def tan(one):
        return Dual(math.tan(one.real), one.dual/(math.cos(one.real)**2))
    
    def exp(one):
        return Dual(math.exp(one.real), math.exp(one.real)*one.dual)

    def log(one):
        return Dual(math.log(one.real), one.dual/one.real)

    #Valid only if n is a constant
    def pow(one, n):
        return Dual(math.pow(one.real, n),
                    n*one.dual*math.pow(one.real, n-1))

    def asin(one):
        return Dual(math.asin(one.real), one.dual*(1-one.real**2)**0.5)

    def acos(one):
        return Dual(math.acos(one.real), -one.dual*(1-one.real**2)**0.5)

    def atan(one):
        return Dual(math.atan(one.real), one.dual/(1+one.real**2))

    def sinh(one):
        return Dual(math.sinh(one.real), one.dual*math.cosh(one.real))

    def cosh(one):
        return Dual(math.cosh(one.real), one.dual*math.sinh(one.real))

    def tanh(one):
        return Dual(math.tanh(one.real),
                    one.dual*(1-math.tanh(one.real)**2))
                    
