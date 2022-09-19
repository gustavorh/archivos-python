# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:41:13 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Función que determinará cuántos cartones se jugaron en total.


# Como parámetro se usa el nombre del archivo.
def n_cartones_jugados(nombre_archivo):
    # Se inicializa "cartones_jugados" en 0 ya que este actuará como un contador.
    cartones_jugados = 0
    # Se abre el archivo con el nombre obtenido de la función como LECTURA (read).
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:  # Para cada linea dentro del archivo.
            cartones_jugados += 1  # Incrementa el contador en 1.
    return cartones_jugados

# Función que determinará cuántos cartones se jugaron con x número.


def cartones_jugados_con_numero(nombre_archivo, numero_jugado):
    # Se inicializa una lista vacía para almacenar los números de cada cartón jugado.
    lista_numeros = []
    # Se abre el archivo con el nombre obtenido de la función como LECTURA (read).
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:  # Para cada línea dentro del archivo.
            # Agrega a la lista "lista_numeros" cada valor, usando como separador un espacio (" ").
            lista_numeros += map(int, linea.split(" "))
        # print(lista_numeros)
    cartones_jugados_con_n = 0
    for i in lista_numeros:
        if numero_jugado == i:
            cartones_jugados_con_n += 1
    return cartones_jugados_con_n


def hay_ganadores(nombre_archivo, n_ganadores):
    # Se abre el archivo con el nombre obtenido de la función como LECTURA (read).
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # Se quitan los espacios en blanco, como los saltos de línea (\n).
            linea = linea.rsplit()
            # Mediante la función map(), se castea a desde str a int cada elemento (número jugado en cartón) y se guarda en un conjunto.
            n_jugados = set(map(int, linea))
            print(n_ganadores)
            print(n_jugados)
            # Si el conjunto (set) con los números ganadores se encuentra en el conjunto (set) de números jugados.
            if len(n_ganadores & n_jugados) == 6:
                return True  # True: hay ganador.
    return False


def n_aciertos(nombre_archivo, n_ganadores, n):
    contador = 0
    # Se abre el archivo con el nombre obtenido de la función como LECTURA (read).
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # Se quitan los espacios en blanco, como los saltos de línea (\n).
            linea = linea.rsplit()
            # Mediante la función map(), se castea a desde str a int cada elemento (número jugado en cartón) y se guarda en un conjunto.
            n_jugados = set(map(int, linea))
            print(n_ganadores)
            print(n_jugados)
            # Si el conjunto (set) con los números ganadores se encuentra en el conjunto (set) de números jugados.
            if len(n_ganadores & n_jugados) == n:
                contador += 1
                # return True # True: hay ganador.
    return contador


# Se pregunta al usuario por el nombre del archivo y su extensión.
nombre_archivo = input(
    "Ingrese el nombre del archivo y su extensión (Ejemplo.txt): ")

numero_cartones_jugados = n_cartones_jugados(nombre_archivo)
print(
    f"El número de cartones jugados, según la información en el archivo {nombre_archivo} es: {numero_cartones_jugados}")

numero_jugado = int(input(
    "Ingrese un número para determinar cuantos cartones escogieron dicho número: "))

cartones_jugados_con_numero = cartones_jugados_con_numero(
    nombre_archivo, numero_jugado)
print(
    f"La cantidad de veces que se jugó un carton con el número {numero_jugado} es: {cartones_jugados_con_numero}")

# Se pregunta al usuario por el conjunto de números ganadores
lista_n_ganadores = []
for n in range(0, 6):
    n_ganador = int(input("Ingrese el número ganador: "))
    lista_n_ganadores.append(n_ganador)

conjunto_n_ganadores = set(lista_n_ganadores)
print(f"El conjunto n ganadores: {conjunto_n_ganadores}")

ganadores = hay_ganadores(nombre_archivo, conjunto_n_ganadores)
print(ganadores)

cantidad_aciertos = int(
    input("Ingrese el número de aciertos que se está buscando: "))
aciertos = n_aciertos(nombre_archivo, conjunto_n_ganadores, cantidad_aciertos)
print(aciertos)
