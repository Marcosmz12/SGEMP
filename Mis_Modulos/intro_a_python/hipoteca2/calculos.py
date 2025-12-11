from funciones import cuota
from funciones import importe_total

def resultado():
    
    hipoteca = 150000
    anios = 15
    intereses = 4.75
    pago_mensual = cuota(hipoteca, anios, intereses)
    print(f"La cuota mensual es = {pago_mensual}")




