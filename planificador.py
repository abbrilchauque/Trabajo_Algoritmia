import random

costoXkm = 500

def menu_destinos():
    nombres_ciudades = ["Santiago, Chile", "Lima, Perú", "Sao Paulo, Brasil", "Bogota, Colombia", "Asunción, Paraguay"]
    destinos = []
    for nombre in nombres_ciudades:
        kilometraje = random.randint(1000, 10000)
        destinos.append([nombre, kilometraje])
    return destinos

def destinos_disponibles(destinos):
    print("Destinos disponibles origen Buenos Aires: ")
    for i in range(len(destinos)):
        nombre, kilometraje = destinos[i]
        print(f"{i + 1} - Ciudad: {nombre}, kilometraje: {kilometraje}km")

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
            # el 1 es el primer número que el usuario puede seleccionar 
            # len destinos, el ultimo número 
            if 1 <= seleccion_num <= len(destinos):
                # numero sea al menos 1, que sea menor a la cantidad de destinos
                #con esto, nos aseguramos que no se seleccione un num fuera de rango
                # se convierte al numero ingresado, en un i válido
                seleccion_i = seleccion_num - 1
                select_destino = destinos[seleccion_i]
                select_destinos.append(select_destino[0])
                select_distancias.append(select_destino[1])
                
                print("___________________________________")
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
                print("Número ingresado incorrecto.")
        else:
            print("Por favor elija un número entero.")

    return select_destinos, select_distancias

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
# max tramo indica el primer destino 
# itera desde el segundo elemento hasta el ult 
def tramo_economico(destinos, distancias):
    min_costo = distancias[0] * costoXkm 
    min_in = 0 
    for i in range(1, len(distancias)): 
        costoTramo = distancias[i] * costoXkm
        if costoTramo < min_costo:
            min_costo = costoTramo
            min_in = i 
    return f"Destino más más economico: {destinos[min_in]}, Distancia que le corresponde: {distancias[min_in]}km, Costo: ${min_costo}"

# destinos ordenados por su valor 
def destinos_ordenados(destinos, distancias):
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

# los indices en el print representan la tupla y los elementos que contiene (son 3)
def mostrar_ordenados(destinos_ordenados):
    print("Destinos ordenados de menor a mayor: ")
    for ordenado in destinos_ordenados:
        print(f"Nombre: {ordenado[0]}, kilometraje: {ordenado[1]}km, Costo: ${ordenado[2]}")

# Programa Principal
destinos = menu_destinos()
select_destinos, select_distancias = seleccion_destinos(destinos)

print("___________________________________")
print("Resumen de su viaje: ")
mostrar_destinos(select_destinos, select_distancias)
print(costo_total(select_distancias))
print(km_totales(select_distancias))
print(tramo_economico(select_destinos, select_distancias))
mostrar_ordenados(destinos_ordenados(select_destinos, select_distancias))