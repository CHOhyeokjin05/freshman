import numpy as np

def polynominal(x):
    coefficients = list(map(float,input('계수 입력 (최고차항부터) : ').split()))
    equation = np.poly1d(coefficients)
    return equation

