from functools import reduce

# 1) implementar una funcion hashPrimerParcial(stringNombre, stringFecha) que recibe un nombre y una fecha de nacimiento y devuelve un numero 
# entero que representa el hash de la persona. El hash se calculará de la siguiente forma:
# Se deben sumar los valores ASCII de los caracteres del nombre. (los valores ASCII se obtienen con la funcion "ord(caracter)" de python)
# Si la suma de los caracteres es un numero impar se le debe sumar el dia de la fecha de nacimiento y calcular el residuo de la division por 5.
# Si la suma de los caracteres es un numero par se le debe sumar el mes de la fecha de nacimiento y calcular el residuo de la division por 5.
# Luego, a ese resultado se le suma el año, y se calcula el módulo de la división por 7 (es el valor final que retorna la función).
# Asegúrate de incluir manejo de errores para verificar que la cadena de fecha esté en el formato correcto y que los valores de día, mes y año sean números enteros.

# les dejo otra forma de validar fecha extraida de un parcial:
def validacionFecha(dia, mes, año):  # Realizamos funcion para validar que la fecha introducida sea correcta.
    if 1 <= año <= 2023:
        if 1 <= mes <= 12:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                return 1 <= dia <= 31
            elif mes == 2:
                # Febrero (posiblemente bisiesto)
                if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                    return 1 <= dia <= 29
                else:
                    return 1 <= dia <= 28
            else:
                # Meses con 30 días
                return 1 <= dia <= 30
    return False

def hashPrimerParcial(stringNombre, stringFecha):
    # Suma de los valores ascii de los caracteres del nombre    
    # alternativas com lambda:
    # alternativa 1
    sumaNombre = reduce(lambda x, y: x + y, list(map(lambda letra: ord(letra), stringNombre)))
    # alternativa 2
    sumaNombre = reduce(lambda x,y: x+ord(y), stringNombre, 0)
    #alternativa con for
    sumaNombre = 0
    for letra in stringNombre:
        sumaNombre += ord(letra)
    # tratamiento de stringFecha
    fecha = stringFecha.split('-')
    if len(fecha) != 3:
        return -1
    try:
        dia = int(fecha[0])
        mes = int(fecha[1])
        anio = int(fecha[2])
    except ValueError:
        return -1
    if sumaNombre % 2 == 0:
        sumaNombre += mes
    else:
        sumaNombre += dia
    sumaNombre = (sumaNombre % 5)
    return (sumaNombre + anio) % 7



# 2) Dada la siguiente lista, devolver una lista nueva ordenada alfabéticamente con todos los nombres que contienen una letra pasada por parámetro sin distingir entre mayuscula y minusculas..
lista_nombres = ["Juan", "Pedro", "Maria", "Ana", "Florencia", "Hector", "jose", "Jorge", "Harry", "Haydee", "gisela","valeria", "valentina", 
         "Vanesa", "violeta", "Viviana", "ximena", "yanina", "Zoe", "Zulema", "Abril", "Agustin", "ivan", "federico"]

def filtrarLista(lista, letra):
    lista_nueva = sorted(list(filter(lambda nombre: letra.lower() in nombre.lower(), lista)), key=str.lower)
    return lista_nueva

def filtrarLista2(lista, letra):
    lista_nueva=[]
    for nombre in lista:
        if letra.lower() in nombre.lower():
            lista_nueva.append(nombre)
    lista_nueva = sorted(lista_nueva, key=str.lower)
    return lista_nueva

def filtrarLista3(lista, letra):
    lista_nueva = sorted([nombre for nombre in lista if letra.lower() in nombre.lower()], key=str.lower)
    return lista_nueva

print(filtrarLista(lista_nombres, 'j'))
print(filtrarLista2(lista_nombres, 'j'))
print(filtrarLista3(lista_nombres, 'j'))

# 3) Un club deportivo abrió la venta de entradas VIP para un torneo importante, cada entrada se vendía a $500 y los socios podían encargar entradas desde la página del club.
# Las solicitudes de los socios se almacenaron en el archivo entradas.csv con el siguiente formato: nombre, cantidad_entradas
# Pero la página aceptó más solicitudes de las que había disponibles. Procese las ventas del archivo en el orden en que se recibieron y muestre 
# por pantalla los nombres de los socios que pudieron comprar y cuantas entradas compraron. Y luego muestra los nombres de los socios que no pudieron comprar entradas.
# Aclaración: si en el proceso alguien pide mas entradas que las disponibles no se le vende ninguna y se continua con el siguiente socio.
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
import os
def procesarVentas(rutaArchivo, cantidadEntradas):
    if os.path.isfile(rutaArchivo):
        with open(rutaArchivo,'r', encoding="utf8") as archivo:
            lineas = archivo.readlines()
            entradas_vendidas = []
            no_compraron =[]
            for linea in lineas:
                socio={}
                datos = linea.split(',')
                nombre = datos[0]
                cantidad = int(datos[1])
                
                if cantidad <= cantidadEntradas:
                    cantidadEntradas -= cantidad
                    socio['nombre'] = nombre
                    socio['cantidad'] = cantidad
                    entradas_vendidas.append(socio)
                else:
                    no_compraron.append(nombre)
            print("Entradas vendidas a:")
            for socio in entradas_vendidas:
                print(socio["nombre"], "compró", socio["cantidad"], "entradas" )
            print("Socios que no pudieron comprar entradas:")
            for socio in no_compraron:
                print(socio)
    else:
        print("El archivo no existe")
    return 0

# Alternativa 2
#  el siguiente procesar ventas en lugar de generar una lista iba guardando en un string lo que tenía que mostrar luego por pantalla:
def procesarVentas2(rutaArchivo, cantidadEntradas):
    """Imprime listado de socios a los que se les vendio entradas y socios a los que no

    Args:
        rutaArchivo (str): Ruta del archivo con la informacion de solicitudes de entradas vendidas
        cantidadEntradas (int): Cantidad de entradas disponibles
    """
    try:
        archivo = open(rutaArchivo, "r", encoding = "UTF-8")
        vendidas = 0
        compraron = ""
        noCompraron = ""
        for linea in archivo:
            datos = linea.split(",")
            cantidad_entradas = int(datos[1])
            if len(datos) == 2:
                if vendidas + cantidad_entradas <= cantidadEntradas:
                    vendidas += cantidad_entradas
                    #compraron += f"{datos[0]}, {cantidad_entradas} entradas\n" if cantidad_entradas > 1 else f"{datos[0]}, 1 entrada\n"
                    if cantidad_entradas == 1:
                        compraron += f"{datos[0]}, 1 entrada\n"
                    else:
                        compraron += f"{datos[0]}, {cantidad_entradas} entradas\n"
                else:
                    noCompraron += f"{datos[0]}\n"
        archivo.close()
        impresion = ""
        if compraron != "":
            impresion += f"Entradas vendidas a:\n{compraron}\n"
        if noCompraron != "":
            impresion += f"Socios que no pudieron comprar entradas:\n{noCompraron}"
        if impresion != "":
            print(impresion)
        else:
            print("Nadie solicito comprar entradas")
        return
    except FileNotFoundError:
        print("Archivo no encontrado")
        return

# alternativa 3
def existe_archivo(archivo):
    """Devulve True si el archivo existe, y False en caso contrario"""
    if os.path.isfile(archivo):
        return True 
    else:
        return False

def enListar(ruta):
    socios=[]
    if existe_archivo(ruta):

        with open(ruta, 'r', encoding="utf-8") as file:
            for line in file:
                nombre,entradas = line.strip().split(',')
                socio = {'nombre':nombre,'entradas': entradas}
                socios.append(socio)
        return socios

def procesarVentas3(rutaArchivo, cantidadEntradas):
    listaSocios = enListar(rutaArchivo)
    vendidas=0
    listaSociosCompraron=[]
    listaSociosNOCompraron=[]
    for socio in listaSocios:
        if cantidadEntradas>vendidas and int(socio['entradas'])<=(cantidadEntradas-vendidas):
            vendidas+= int(socio['entradas'])
            datos={'nombre':socio['nombre'],'entradas':socio['entradas']}
            listaSociosCompraron.append(datos)
        else:
            datos={'nombre':socio['nombre'],'entradas':socio['entradas']}
            listaSociosNOCompraron.append(datos)

    return listaSociosCompraron, listaSociosNOCompraron


#procesarVentas('entradas.csv', 20)

# 4: a)  los datos se procesaron como una estructura de datos llamada "cola" que sigue el principio 
# FIFO (first in first out) en el que el primero en llegar es el primero en salir.

# b)  ¿Qué es un "Pull Request" (PR) en GitHub y cuál es su propósito en un proyecto colaborativo? 
# un pull request es una solicitud de cambios que se hace en un repositorio de github, 
# el cual se hace para que el dueño del repositorio pueda revisar los cambios y aceptarlos o rechazarlos.
# El objetivo principal es favorecer la revisión de código. No solo sirve para enviar tu código 
# sino que es importante que puedan comentar tu código y tener un feedback



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

#la siguiente función, como vimos en clase, funciona pero modifica la lista original
def generarLista(lista_precios, lista_stock_a_vencer):
    lista_remate =[]
    for producto in lista_stock_a_vencer:
        for precio in lista_precios:
            if producto['producto'] == precio['producto']:
                producto['precio_promocional'] = precio['precio'] * 0.8
                lista_remate.append(producto)
    return lista_remate

# Alternativa 2
def generarLista2(lista_precios, lista_stock_a_vencer):
    lista_resultado = []
    for producto_precio in lista_precios:
        for producto_a_vencer in lista_stock_a_vencer:
            if producto_precio["producto"] == producto_a_vencer["producto"]:
                precio = producto_precio["precio"]
                precio_promocional = precio - (precio * 0.2)
                # crea un diccionario para guardar los datos en la lista_resultado
                producto = {
                    "producto": producto_precio["producto"],
                    "cantidad": producto_a_vencer["cantidad"],
                    "precio_promocional": precio_promocional
                }
        lista_resultado.append(producto)
    return lista_resultado

# algunos resolvieron igual que en el ciclo anterior pero generando un nuevo 
# diccionario agregandole el precio original también.

# Alternativa 3
def generarLista3(lista_precios, lista_stock_a_vencer):
    lista_remate = [ { 'producto': producto['producto'], 'cantidad' : producto['cantidad'], 'precio_promocional': precio['precio'] * 0.8 } for producto in lista_stock_a_vencer for precio in lista_precios if producto['producto'] == precio['producto'] ]
    return lista_remate

# lista=generarLista2(lista_precios, lista_stock_a_vencer)
# for i in lista:
#     print(i)