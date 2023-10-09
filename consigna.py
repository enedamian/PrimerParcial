# Primer Parcial - Programación 2 TUP

# Apellido y nombre:
# Legajo

# 1) implementar una funcion hashPrimerParcial(stringNombre, stringFecha) que recibe un nombre y una fecha de nacimiento y devuelve un numero 
# entero que representa el hash de la persona. stringFecha tiene formato dd-mm-aaaa. El hash se calculará de la siguiente forma:
# Se deben sumar los valores ASCII de los caracteres del nombre. (los valores ASCII se obtienen con la funcion "ord(caracter)" de python)
# Si la suma de los caracteres es un numero impar se debe sumar el dia de la fecha de nacimiento y calcular el residuo de la division por 5.
# Si la suma de los caracteres es un numero par se debe sumar el mes de la fecha de nacimiento y calcular el residuo de la division por 5.
# Luego, a ese resultado se le suma el año, y se calcula el módulo de la división por 7 (es el valor final que retorna la función).
# Asegúrate de incluir manejo de errores para verificar que la cadena de fecha esté en el formato correcto y que los valores de día, mes y año sean números enteros.

def hashPrimerParcial(stringNombre, stringFecha):
    
    return 0



# 2) Dada la siguiente lista, devolver una lista nueva ordenada alfabéticamente con todos los nombres que contienen una letra pasada por parámetro sin distingir entre mayuscula y minusculas..
lista_nombres = ["Juan", "Pedro", "Maria", "Ana", "Florencia", "Hector", "jose", "Jorge", "Harry", "Haydee", "gisela","valeria", "valentina", 
         "Vanesa", "violeta", "Viviana", "ximena", "yanina", "Zoe", "Zulema", "Abril", "Agustin", "ivan", "federico"]

def filtrarLista(lista, letra):
    
    return []


# 3) Un club deportivo abrió la venta de entradas VIP para un torneo importante, cada entrada se vendía a $500 y los socios podían encargar entradas desde la página del club.
# Las solicitudes de los socios se almacenaron en el archivo entradas.csv con el siguiente formato: nombre, cantidad_entradas
# Pero la página aceptó más solicitudes de las que había disponibles. Procese las ventas del archivo en el orden en que se recibieron y muestre 
# por pantalla los nombres de los socios que pudieron comprar y cuantas entradas compraron. Y luego muestra los nombres de los socios que no pudieron comprar entradas.

# Ejemplo Hay 10 entradas disponibles y se recibieron las siguientes solicitudes:
# Entradas vendidas a:
# Juan, 2 entradas
# Pedro, 3 entradas
# Maria, 3 entradas
# Ana, 2 entradas
# Socios que no pudieron comprar entradas: 
# Florencia
# Hector .....
# ruta archivo para usar F5: PrimerParcial\entradas.csv
# probar con 20 entradas

def procesarVentas(rutaArchivo, cantidadEntradas):
    
    return 0

# 4) a) # En el punto anterior, los datos se procesaron como una estructura de datos llamada .... que sigue el principio de ....


# 4) b) ¿Qué es un "Pull Request" (PR) en GitHub y cuál es su propósito en un proyecto colaborativo? 



# 5) Dadas dos listas de diccionarios, una con listado de productos y precios, y otra con listado de productos y cantidad de unidades en stock próximas al vencimiento, 
# generar una nueva lista de diccionarios que contenga para cada producto la cantidad de unidades que están por vencer y un precio promocional con 20% de descuento.
# Ejemplo:
# lista_precios = [{"producto": "arroz", "precio": 125.50}, {"producto": "fideos", "precio": 50.75}, {"producto": "pan", "precio": 35.00}]
# lista_ventas = [{"producto": "arroz", "cantidad": 100}, {"producto": "fideos", "cantidad": 200}, {"producto": "pan", "cantidad": 300}]
# lista_resultado = [{"producto": "arroz", "cantidad": 100, "precio_promocional": 112.95}, {"producto": "fideos", "cantidad": 200, "precio_promocional": 45.675}, {"producto": "pan", "cantidad": 300, "precio_promocional": 31.5}]

lista_precios = [
    {"producto": "arroz", "precio": 125.50}, {"producto": "fideos", "precio": 50.75},
    {"producto": "pan", "precio": 35.00}, {"producto": "leche", "precio": 80.00}, 
    {"producto": "azucar", "precio": 45.00}, {"producto": "harina", "precio": 55.00},
    {"producto": "aceite", "precio": 100.00}, {"producto": "yerba", "precio": 110.00},
    {"producto": "galletitas", "precio": 70.00}, {"producto": "cacao", "precio": 90.00}
    ]
lista_stock_a_vencer = [
    {"producto": "arroz", "cantidad": 400}, {"producto": "fideos", "cantidad": 200}, 
    {"producto": "pan", "cantidad": 300}, {"producto": "leche", "cantidad": 100},
    {"producto": "galletitas", "cantidad": 50}, {"producto": "cacao", "cantidad": 150}]

def generarLista(lista_precios, lista_stock_a_vencer):
    
    return []
