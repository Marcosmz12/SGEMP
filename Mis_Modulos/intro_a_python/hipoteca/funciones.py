import math

def cuota(h, n, i):
    r = i /(100 * 12)
    numerador = h * r
    e = math.pow((1 + r), (-12 * n))
    denominador = 1 - e

    m = numerador / denominador
    
    return round(m, 2)

def saludo():
    return "hola"