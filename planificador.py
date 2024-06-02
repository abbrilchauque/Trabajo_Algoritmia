import random

costoXkm = 500

def menu_destinos():
    nombres_ciudades = ["Santiago", "Lima", "Sao Paulo", "Bogota", "Asunción"]
    destinos = []
    for nombre in nombres_ciudades:
        kilometraje = random.randint(1000, 10000)
        destinos.append([nombre, kilometraje])
    return destinos

def destinos_disponibles(destinos):
    print("Destinos disponibles origen Buenos Aires: ")
    for i in range(len(destinos)):
        nombre, kilometraje = destinos[i]
        print(f"{i + 1}, Ciudad: {nombre}, kilometraje: {kilometraje}km")

def mostrar_destinos(destinos, distancias):
    print("Destinos que usted ha visitado: ")
    for i in range(len(destinos)):
        print(f"Ciudad: {destinos[i]}, kilometraje: {distancias[i]}km")

def seleccion_destinos(destinos):
    select_destinos = []
    select_distancias = []
    seleccion_num = -1
    
    while seleccion_num != 0 and len(destinos) > 0:
        destinos_disponibles(destinos)
        select = input("Ingrese el ID de su destino (0 para terminar): ")

        if select.isdigit():
            seleccion_num = int(select)
            if 1 <= seleccion_num <= len(destinos):
                seleccion_i = seleccion_num - 1
                select_destino = destinos[seleccion_i]
                select_destinos.append(select_destino[0])
                select_distancias.append(select_destino[1])
                
                print(f"Usted ha seleccionado la Ciudad: {select_destino[0]}, Kilometraje: {select_destino[1]}KM")
                if select_destino[0] == "Buenos Aires":
                    print("destino: BUENOS AIRES. Viaje finalizado")
                    break
            # esto obtiene una lista donde están todos los destinos
            # menos los que ya hayan sido seleccionados 
            # :seleccion_i desde el principio hasta el indice antes del destino q se seleccione
            # seleccion_i + 1: todos los destinos en la lista desde el indice que le sigue
            # hasta el final de la lista (los q van despues del seleccionado se mantienen)
                destinos = destinos[:seleccion_i] + destinos[seleccion_i + 1:]
            else:
                print("Número ingresado incorrecto. Vuelva a ingresar.")
        else:
            print("Por favor elija un número entero.")

    return select_destinos, select_distancias

def costo_total(distancias):
    total = sum(distancia * costoXkm for distancia in distancias)
    return f"Su viaje se estima un total de ${total}"

def km_totales(distancias):
    total = sum(distancias)
    return f"Su recorrido tuvo un total de {total}km"

def tramo_economico(destinos, distancias):
    min_tramo = min(distancias) * costoXkm
    min_in = distancias.index(min(distancias))
    return f"Destino más económico: {destinos[min_in]}, Distancia: {distancias[min_in]}km, Costo: ${min_tramo}"

# destinos ordenados por su valor 
def destinos_ordenados(destinos, distancias):
    destinos_costos = [[destinos[i], distancias[i], distancias[i] * costoXkm] for i in range(len(destinos))]
    destinos_costos.sort(key=lambda x: x[2])
    return destinos_costos
# [2] 3er elemento de cada sublista en destinos_costos, el tercer elemento
# representa el costo que se asocia con cada destino 

# los indices en el print representan la tupla y los elementos que contiene (son 3)
def mostrar_ordenados(destinos_ordenados):
    print("Destinos ordenados de menor a mayor: ")
    for ordenado in destinos_ordenados:
        print(f"Nombre: {ordenado[0]}, kilometraje: {ordenado[1]}km, Costo: ${ordenado[2]}")

# Programa Principal
destinos = menu_destinos()
select_destinos, select_distancias = seleccion_destinos(destinos)

print("Resumen de su viaje: ")
mostrar_destinos(select_destinos, select_distancias)
print(costo_total(select_distancias))
print(km_totales(select_distancias))
print(tramo_economico(select_destinos, select_distancias))
mostrar_ordenados(destinos_ordenados(select_destinos, select_distancias))