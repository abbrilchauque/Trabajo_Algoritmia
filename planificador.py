import random 

costoXkm = 500

# hacer una lista de destinos donde el origen sea buenos aires 
def menu_destinos():
    nombres_ciudades= ["Santiago", "Lima", "Sao Paulo", "Bogota", "Asunción"]
    destinos = []
    for nombre in nombres_ciudades:
        kilometraje = random.randint(1000, 10000)
        destinos.append([nombre, kilometraje])
    return destinos

# se muestra la lista de destinos diponibles
# los destinos van incrementando  
def destinos_disponibles(destinos):
    print("Destinos disponibles origen Buenos Aires: ")
    for i in range(len(destinos)): 
        nombre = destinos[i][0]
        kilometraje = destinos[i][1]
        print(f"{i + 1}, Ciudad: {nombre}, kilometraje: {kilometraje}km") 

# mostrar destinos seleccionados 
def mostrar_destinos(destinos, distancias):
    print("Destinos que usted ha visitado: ")
    for i in range(len(destinos)):
        print(f"Ciudad: {i + 1}, kilometraje: {distancias[i]}km ")

#seleccionar destinos 
def seleccion_destinos(destinos):
    select_destinos = []
    select_distancias = []

    seleccion_num = 0
    while seleccion_num != 0 and len(destinos) > 0 :
        print("Destinos desde buenos aires: ")   
        for i in range(len(destinos)):
            nombre, kilometraje = destinos[i]
            print(f"{i + 1} - Ciudad: {nombre}, Kilometraje: {kilometraje}KM")  
        
        select = int(input("Ingrese el ID de su destino (0 para terminar): "))
       
        if select.isdigit():
            seleccion_num = int(select)
            if seleccion_num == 0:
                break
            elif 1 <= seleccion_num <= len(destinos):
                seleccion_i = seleccion_num - 1
                select_destino = destinos[seleccion_i]
                select_destinos.append(select_destino[0])
                select_distancias.append(select_destino[1])

                print(f"Usted ha seleccionado la Ciudad: {select_destino[0]}, Kilometraje: {select_destino[1]}KM")

                if select_destino[0] == "Buenos Aires": 
                    print("Usted ha seleccionado BUENOS AIRES. Viaje finalizado.")
                    break

            # esto obtiene una lista donde están todos los destinos
            # menos los que ya hayan sido seleccionados 
            # :seleccion_i desde el principio hasta el indice antes del destino q se seleccione
            # seleccion_i + 1: todos los destinos en la lista desde el indice que le sigue
            # hasta el final de la lista (los q van despues del seleccionado se mantienen)
                destinos = destinos[:seleccion_i] + destinos[seleccion_i + 1:]
            else: 
                print("El número que usted ha ingresado es incorrecto. Por favor, vuelva a ingresar.")
        else: 
            print("Por favor ingrese un entero :(. Vuelva a intentarlo")

    return select_destinos, select_distancias

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
# max tramo indica el primer destino 
# itera desde el segundo elemento hasta el ult 
def tramo_economico(destinos, distancias):
    min_tramo = distancias[0] * costoXkm 
    min_in = 0 
    for i in range(1, len(distancias)): 
        costoTramo = distancias[i] * costoXkm
        if costoTramo < min_tramo:
            min_costo = costoTramo
            min_in = i 
    return f"Destino más más economico: ${destinos[min_in]}, Distancia que le corresponde: {distancias[min_in]}, Costo: ${min_costo}" 

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
       print(f"Nombre: {ordenado[0]}, kilometraje: {ordenado[1]}, Costo: {ordenado[2]}")

# PROGRAMA PRINCIPAL
def main():
    destinos = menu_destinos()
    select_destinos, select_distancias = seleccion_destinos(destinos)

    print("Resumen de su viaje: ")
    mostrar_destinos(select_destinos, select_distancias)
    print(costo_total(select_distancias))
    print(km_totales(select_distancias))
    print(tramo_economico(select_destinos, select_distancias))
    mostrar_ordenados(destinos_ordenados(destinos, select_distancias))

if __name__ == "__main__":
    main()