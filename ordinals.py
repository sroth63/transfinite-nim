class Ordinal:
    def __init__(self, n):
        if isinstance(n, list):
            self.cantor = n
        if isinstance(n, int):
            if n == 0: self.cantor = []
            else:      self.cantor = [(Ordinal(0), n)]
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self == Ordinal(other)
        return self.cantor == other.cantor

    def __req__(self, other):
        return Ordinal(other) == self

    def is_finite(self):
        return self == 0 or self.cantor[0][0] == 0
    
    def __repr__(self):
        if self == 0:
            return "0"
        if self.is_finite():
            return str(self.cantor[0][1])
        repr = ""
        for (a,b) in self.cantor:
            if a == 0:
                repr += " + " + str(b)
            elif a == 1:
                repr += " + ω"
                if b > 1:
                    repr += " · " + str(b)
            else:
                repr += " + ω**(" + a.__repr__() + ")"
                if b > 1:
                    repr += " · " + str(b)
        return repr[3:]

    def __lt__(self, other):
        if isinstance(other, int): return self < Ordinal(other)
        if other == 0: return False
        if self == 0:  return True 
        (a1, b1), (a2, b2) = self.cantor[0], other.cantor[0]
        if a1 < a2: return True 
        if a2 < a1: return False 
        if b1 < b2: return True 
        if b2 < b1: return False
        return Ordinal(self.cantor[1:]) < Ordinal(other.cantor[1:])

    def __le__(self, other): 
        return self < other or self == other
    
    def __gt__(self, other):
        if isinstance(other, int): return self > Ordinal(other)
        return other < self
    
    def __ge__(self, other):
        if isinstance(other, int): return self >= Ordinal(other)
        return other <= self

    def __add__(self, other):
        if isinstance(other, int): return self + Ordinal(other)
        if self == 0: return other 
        if other == 0: return self
        (a1, b1), (a2, b2) = self.cantor[-1], other.cantor[0]
        if a1 > a2:
            return Ordinal(self.cantor + other.cantor)
        elif a1 == a2:
            return Ordinal(self.cantor[:-1] + [(a1, b1+b2)] + other.cantor[1:])
        else:
            return Ordinal(self.cantor[:-1] + other.cantor)

    def __radd__(self, other):
        return Ordinal(other) + self

    def __mul__(self, other):
        if isinstance(other, int): return self * Ordinal(other)
        if self == 0:
            return self
        prod = 0
        for (a, b) in other.cantor:
            if a == 0:
                (a0, b0) = self.cantor[0]
                prod += Ordinal([(a0, b0*b)] + self.cantor[1:])
            else:
                prod += Ordinal([(self.cantor[0][0] + a, b)])
        return prod
    
    def __rmul__(self, other):
        return Ordinal(other) * self

    def substract(self, other):
        '''returns a such that self = other + a, assuming self >= other'''
        if isinstance(other, int): return self.substract(Ordinal(other))
        assert self >= other
        if self == 0: return Ordinal(0)
        if other == 0: return self
        (a, b), (c, d) = self.cantor[0], other.cantor[0]
        if a > c: return self
        if b == d: return Ordinal(self.cantor[1:]).substract(Ordinal(other.cantor[1:]))
        return Ordinal([(a, b-d)] + self.cantor[1:])

    def __floordiv__(self, other):
        if isinstance(other, int): return self // Ordinal(other)
        if other == omega:
            return Ordinal([(a.substract(1), b) for (a, b) in self.cantor if a >= 1])
        else: raise NotImplementedError

    def __rfloordiv__(self, other):
        return Ordinal(other) // self

    def __mod__(self, other):
        if isinstance(other, int): return self // Ordinal(other)
        return self.substract(other * (self // other))
    
    def __rmod__(self, other):
        return Ordinal(other) % self

    def __pow__(self, other):
        if isinstance(other, int): return self**Ordinal(other)
        if other == 0: return 1
        if self == 0: return 0
        if self.is_finite():
            if other.is_finite():
                return self.cantor[0][1] ** other.cantor[0][1]
            q, r = other // omega, other % omega
            return omega**q * self**r
        if self == omega:
            return Ordinal([(other, 1)])
        raise NotImplementedError

    def __rpow__(self, other):
        return Ordinal(other)**self

    def binary(self):
        bin = []
        for (a, b) in self.cantor:
            b_bin = []
            exponent = 0
            while b > 0:
                if b % 2 == 1:
                    b_bin.append(exponent)
                b //= 2
                exponent += 1
            b_bin.reverse()
            bin += [omega * a + Ordinal(c) for c in b_bin]
        return bin
    
    def xor_binary(self, b1, b2):
        if b1 == []: return b2
        if b2 == []: return b1
        e1, e2 = b1[0], b2[0]
        if e1 > e2: return [e1] + self.xor_binary(b1[1:], b2)
        if e1 == e2: return self.xor_binary(b1[1:], b2[1:])
        if e1 < e2: return [e2] + self.xor_binary(b1, b2[1:])

    def __xor__(self, other):
        if isinstance(other, int):
            return self ^ Ordinal(other)
        xor = self.xor_binary(self.binary(), other.binary())
        return sum((2**e for e in xor))

    def __rxor__(self, other):
        return Ordinal(other) ^ self

omega = Ordinal([(Ordinal(1),1)])
ω = omega