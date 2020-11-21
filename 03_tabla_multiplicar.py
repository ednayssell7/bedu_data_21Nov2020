#script que calcule la tabla de multiplicar de un numero
#solicitar numero al usuario por consola
numero = input('que numero quieres multiplicar?')
#el dato ingresado es string
#convertir a INT para poder multiplicar
numero =int(numero)

#for n in range(10):
#    resultado = numero * (n + 1)
#    print(resultado)

#TAREA
# imprimir resultado asi
#8 x 1 = 8
#8 x 2 = 16
#8 x 3 =32
...

print(f'A continuacion se muestra la tabla de multiplicar del numero {numero}')
print(f'-----------')
for n in range(10):
    resultado = numero * (n+1)
    print(f'{numero} x {n+1} = {resultado}')

