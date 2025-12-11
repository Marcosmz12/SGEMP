import math

def cuota(h, n, i):
    r = i /(100 * 12)
    numerador = h * r
    e = math.pow((1 + r), (-12 * n))
    denominador = 1 - e

    m = numerador / denominador
    
    return round(m, 2)


def importe_total(h , n ,i):
    
    pm = cuota(h, n ,i)

    total = pm * 12 * 15     
    return round(total, 2)