**Planificador de viajes**
Empresa de turismo desea lanzar una aplicación que permita a sus usuarios planificar su viaje por distintos destinos de América Latina.
Para ello, cuenta con una lista de destinos que puede ofrecer a sus usuarios. Siempre el origen es Buenos Aires, Argentina y el usuario podrá decidir paso a paso que otros destinos desea visitar.
Desarrollar un programa que permita al usuario seleccionar los destinos de su viaje.
El programa incluye un menú que listará los destinos disponibles junto a la distancia que hay hasta ellos (la distancia se generará con números aleatorios utilizando el modulo random en python). De esta manera el usuario podrá ir armando su itinerario hasta que seleccione la opcion Buenos Aires, Argentina lo que significa que el viaje ha llegado a su fin.
No se podran repetir destinos y en el menu solamente pueden aparecer los destinos no visitados hasta cada momento.

**Una vez terminado el itinerario el programa debera ser capaz de:**

1. Calcular el valor total del viaje (la idea acá seria que haya un costo por km recorrido, digase $500 y entonces se multiplique la distancia que se recorre para cada destino por este monto)

2. Calcular cual fue la cantidad total de kilometros recorrida

3. Calcular cual fue el tramo del viaje (origen-destino) mas economico (menor monto)

4. Mostrar de mayor a menor los destinos segun su valor

**El ejercicio incluye**

- Trabajo con listas paralelas (listas para destinos elegidos, distancia hasta ese destino )

- Trabajo con el modulo random para la generacion de numeros (en este caso distancias) aleatorios

- Metodos de ordenamiento para mostrar el listado de mayor a menor segun el valor de cada tramo

- Busqueda secuencial → en el menu antes de desplegar cada destino debo saber si ya fue seleccionado o no

