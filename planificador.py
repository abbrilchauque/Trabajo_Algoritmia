import random 

costoXkm = 500

# hacer una lista de destinos donde el origen sea buenos aires 
def menu_destinos():
    nombres_ciudades= ["Santiago", "Lima", "Sao Paulo", "Bogota", "Asunción"]
    destinos = []
    for nombre in range(len(nombres_ciudades)):
        kilometraje = random.randint(1000, 10000)
        destinos.append([nombre, kilometraje])
    return destinos

# se muestra la lista de destinos diponibles 
def destinos_disponibles(destinos):
    print("Destinos disponibles origen Buenos Aires: ")
    for i in range(len(destinos)): 
        nombre = destinos[i][0]
        kilometraje = destinos[i][1]
        print(f"{i + 1}, Nombre: {nombre}, kilometraje: {kilometraje}km") 

# destinos seleccionados 
def detinos_seleccionados(destinos, distancias):
    print("Destinos que usted ha visitado: ")
    for i in range(len(destinos)):
        print(f"Nombre: {i + 1}, kilometraje: {distancias[i]}km ")

# costo total del kilometraje
def costo_total(distancias):
    total = 0 
    for distancia in distancias:
        total += distancia * costoXkm
    return f"Su viaje se estima un total de ${total}"

# kilometraje total
def km_totales(distancias):
    total = 0 
    for distancia in distancias:
        total += distancia
    return f"Su recorrido tuvo un total de {total}km"

# cual es el tramo más económico
def tramo_economico(destinos, distancias):
    min_tramo = distancias[0] * costoXkm 
    max_tramo = 0 
    for i in range(1, len(distancias)): 
        costoTramo = distancias[i] * costoXkm
        if costoTramo < min_tramo:
            min_costo = costoTramo
            max_tramo = i 
    return f"El tramo más economico: {destinos[min_tramo]}, Máximo: {destinos[max_tramo]}, Costo: {min_costo}" 

# destinos ordenados por su valor 
def costos_ordenados(destinos, distancias):
    destinos_costos = []
    for i in range(len(destinos)):
        costo = distancias[i] * costoXkm
        destinos_costos.append([destinos[i], distancias[i], costo])

    for x in range(len(destinos_costos)):
        for j in range(0, len(destinos_costos) - x -1): 
            if destinos_costos[j][2] < destinos_costos [j + 1][2]:
                aux = destinos_costos[j]
                destinos_costos[j] = destinos_costos [j + 1]
                destinos_costos[j + 1] = aux 
    return destinos_costos
# [2] 3er elemento de cada sublista en destinos_costos, el tercer elemento
# representa el costo que se asocia con cada destino 

def mostrar_ordenados(destinos, distancias):
   destinos_ordenados = ordenados_valor(destinos, distancias)
   print("Destinos ordenados de menor a mayor: ")
   for ordenado in destinos_ordenados:
       print(f"Nombre: {ordenado[0]}, kilometraje: {ordenado[1]}, Costo: {ordenado[2]}")


# def programa(): 
#     destinos = menu_destinos()
    

    

