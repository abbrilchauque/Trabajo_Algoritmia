import random 

costoXkm = 500

# hacer una lista de destinos donde el origen sea buenos aires 
def menu_destinos():
    nombres_ciudades= ["Buenos Aires","Santiago", "Lima", "Sao Paulo", "Bogota"]
    destinos = []
    for i in range(len(nombres_ciudades)):
        kilometraje = random.randint(7000, 19000)
        destinos.append([i, kilometraje])
    return destinos

# se muestra la lista de destinos diponibles 
def destinos_disponibles(destinos):
    for i in range(len(destinos)): 
        nombre = destinos[i][0]
        kilometraje = destinos[i][1]
        print(f"{i + 1}, Nombre: {nombre}, kilometraje: {kilometraje}km") 

# destinos seleccionados 

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
        costo = distancias[i] * costoXkm
        if costo < min_tramo:
            min_costo = costo
            max_tramo = 1 
    return f"El tramo más economico: {destinos[min_tramo]}, Máximo: {destinos[max_tramo]}, Costo: {min_costo}" 

# destinos ordenados por su valor 
def destinos_ordenados(destinos, distancias):
    destinos_costos = []
    for i in range(len(destinos)):
        destinos_costos.append(destinos[i], distancias[i], distancias[i] * costoXkm)

# ordenar los costos de menos a mayor 
    
