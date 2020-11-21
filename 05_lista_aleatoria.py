#generar una lista con valores aleatorios
from random import randint

#lista vacia
lista_aleatoria = []

#solicitar cuantos valores

elementos = input('cuantos elementos necesitas: ')
elementos = int(elementos)

contador = 1

while contador <= elementos:
    #generamos un valor aleatorio
    matriz = randint(1, 100)
    # num aleatorio multiplicado por los elementos
    valor = matriz * elementos
   #guardar valor aleatorio en la lista
    lista_aleatoria.append(valor)

    #sumar valor a contador para la siguiente vuelta
    contador = contador +1
print(lista_aleatoria)