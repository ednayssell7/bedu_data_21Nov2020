precios_en_menu = [1975, 1825, 275, 1500, 850, 675, 1175, 1600, 2175, 2175, 625, 1150, 1175, 350, 1125, 1250, 1875, 1275, 825, 1575, 300, 1275, 875, 1650, 875]

iva = 0.16

for x in (precios_en_menu):
    calculo_iva = (x * iva) 
    calculo_iva = float(calculo_iva)
    precio_mas_iva = calculo_iva + x 
    resultado_con_strings = (f'Precio sin IVA: ${x}, IVA calculado: ${calculo_iva}, Precio mas IVA: ${precio_mas_iva}')
    print(resultado_con_strings)
