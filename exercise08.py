from numpy import *


# Task 01
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        r1, r2 = self.real, other.real
        im1, im2 = self.imaginary, other.imaginary
        return complex(r1 + r2, im1 + im2)

    def __sub__(self, other):
        r1, r2 = self.real, other.real
        im1, im2 = self.imaginary, other.imaginary
        return complex(r1 - r2, im1 - im2)

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imaginary

    def is_imaginary(self):
        pass

    def is_real(self):
        pass

    def __repr__(self):
        return f"{self.real} + {self.imaginary}j"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary


a = ComplexNumber(1, 2)
b = ComplexNumber(1, 2)
print(a == b)
