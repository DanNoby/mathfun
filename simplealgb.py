'''
class X:
    def __init__(self, coeiff=1, pow=1):
        self.coeiff = coeiff
        self.pow = pow

    def __repr__(self) -> str:
        if self.pow == 1:
            return f"{self.coeiff}x"
        elif self.pow == 2:
            return f"{self.coeiff}x²"
        elif self.pow ==3:
            return f"{self.coeiff}x³"
        elif self.pow==0:
            return f"{self.coeiff}"


def main():
    s = input("Enter a polynomial expression: ")
    s0 = [i.strip() for i in s.split('+')]
    print("Parsed terms:", s0)
    L = []
    for term in s0:
        parts = term.split('x')
        if parts[0]=="":
            coeiff = 1
        else:
            coeiff = int(parts[0])
        pow = 1
        print(f"{parts[0]} and {parts[1]}") 
        if '^' in parts[1]:
            pow = int(parts[1][1:])
        L.append(X(coeiff, pow))
    print("List of objects:", L)

main()
'''
import re
import math
from fractions import Fraction
import sympy as sp
class X:
    def __init__(self, coeiff=1, pow=1):
        self.coeiff = coeiff
        self.pow = pow

    def __repr__(self) -> str:
        if self.pow == 1:
            return f"{self.coeiff}x"
        elif self.pow == 2:
            return f"{self.coeiff}x²"
        elif self.pow == 3:
            return f"{self.coeiff}x³"
        elif self.pow == 0:
            return f"{self.coeiff}"

def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        root1 = (-b + math.sqrt(abs(discriminant))) / (2 * a)
        root2 = (-b - math.sqrt(abs(discriminant))) / (2 * a)
        return f"{(root1)}i", f"{(root2)}i"
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1), (root2)


def solve_polynomial(coefficients):
    x = sp.symbols('x')
    polynomial = sum(c * x**i for i, c in enumerate(coefficients[::-1]))
    solutions = sp.solve(polynomial, x)
    return solutions

def main():
    s = input("Enter a polynomial expression: ")
    s0 = re.findall(r'(-?\d*)x\^?(\d*)', s)
    print("Parsed terms:", s0)
    
    coefficients = [0] * (max([int(pair[1]) for pair in s0]) + 1)

    for coeiff, pow in s0:
        coeiff = int(coeiff) if coeiff else 1
        pow = int(pow) if pow else 1
        coefficients[pow] += coeiff

    if len(coefficients) >= 3:
        print("Coefficients:", coefficients)
        a, b, c = coefficients[2], coefficients[1], coefficients[0]
        print("Solving quadratic equation:")
        print(f"{a}x² + {b}x + {c} = 0")
        print("Roots:", solve_quadratic(a, b, c))
    else:
        print("Not a quadratic equation")

if __name__ == "__main__":
    main()
















