#3) Hacer un programa que gestiones datos para una escuela.
#El programa tiene que ser capaz de:
#a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
#Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
#notas, cantidad de faltas, cantidad de amonestaciones recibidas.
#Recomendación: Para llevar un registro de estos dato se puede
#utilizar un diccionario estructurado de la siguiente manera:
#{
#“Alumnos” : [alumno1,alumno2,alumno3 ]
#}
#Donde cada alumno es otro diccionario estructurado de la
#siguiente forma:
#{
#“Nombre”: nombre de alumno,
#“Apellido” : apellido de alumno,
#“DNI” : DNI de alumno
#“Fecha de nacimiento”, fecha de nacimiento de alumno,
#“Tutor” : nombre y apellido de tutor,
#“Notas” : todas las notas del alumno,
#“Faltas” : cantidad de faltas,
#“amonestaciones” : cantidad de amonestaciones
#}
#En esta estructura:
#Datos = {
#“Alumnos” : [alumno1,alumno2,alumno3 ]
#}
#Para acceder por ejemplo al numero de DNI del tercer alumno
#podríamos hacer algo así:
#Datos[“Alumnos”][2][“DNI”]
#Este es un ejemplo de estructura, se puede cambiar
#completamente o hacer algunos cambios sobre el para mejorar el
#orden (si lo consideran necesario)
#b) Mostrar los datos de cada alumno
#c) Modificar los datos de los alumnos
#d) Agregar alumnos
#e) Expulsar alumnos

##Parte de las funciones:
import funciones
import json
##Datos de alumnos
alumno1={"Nombre":"Tomas",
         "Apellido":"Villagra",
         "DNI":"45768262",
         "Fecha de nacimiento":"14/07/2004",
         "Tutor":"Alejandro Villagra",
         "Notas":[8,7,5,1,6],
         "Faltas":10,
         "Amonestaciones":0}
alumno2={"Nombre":"Nahuel",
         "Apellido":"Portal",
         "DNI":"45768123",
         "Fecha de nacimiento":"13/09/2004",
         "Tutor":"Manuel Portal",
         "Notas":[9,5,0,8,6],
         "Faltas":6,
         "Amonestaciones":1}
alumno3={"Nombre":"Hernan",
         "Apellido":"Pogonsa",
         "DNI":"45675361",
         "Fecha de nacimiento":"12/09/2004",
         "Tutor":"Leonel Pogonsa",
         "Notas":[4,7,7,7,5],
         "Faltas":4,
         "Amonestaciones":2}
alumno4={"Nombre":"Roberto",
         "Apellido":"Zanet",
         "DNI":"45769265",
         "Fecha de nacimiento":"21/07/2004",
         "Tutor":"Nicolas Zanet",
         "Notas":[1,4,8,9,10],
         "Faltas":15,
         "Amonestaciones":3}

Datos={
    "Alumnos":[alumno1,alumno2,alumno3,alumno4]
}
archivo_datos = "datos.json"
try:
    with open(archivo_datos, 'r') as file:
        Datos = json.load(file)
except FileNotFoundError:
    Datos = {
        "Alumnos": [alumno1, alumno2, alumno3, alumno4]
    }
##Menu de opciones:
while True:
    print("Menú:")
    print("a. Mostrar datos de un alumno")
    print("b. Modificar datos de un alumno")
    print("c. Modificar un solo dato de un alumno")
    print("d. Agregar nuevo alumno")
    print("e. Expulsar alumno")
    print("f. Salir")

    opcion = input("Ingrese la opción deseada (a, b, c, d, e, f): ").lower()

    with open(archivo_datos, 'w') as file:
        json.dump(Datos, file, indent=2)
    
    if opcion == "f":
        print("¡Programa cerrado!")
        break

    if opcion in ("a", "b", "c", "d", "e"):
        
        if opcion == "d":
            
            nuevo_alumno = funciones.ingresar_datos_alumno()
            funciones.agregar_alumno(Datos, nuevo_alumno)
            print("Nuevo alumno agregado exitosamente.")
        
        
        print("Nombre de los alumnos")
        for alumno in Datos["Alumnos"]:
            print(alumno["Nombre"])
        nombre_alumno = input("Ingrese el nombre del alumno:")

        
        alumno_encontrado = None
        for alumno in Datos["Alumnos"]:
            if alumno['Nombre'] == nombre_alumno:
                alumno_encontrado = alumno
                break

        if opcion == "a" and alumno_encontrado:
            funciones.informacion_alumno(alumno_encontrado)
        elif opcion == "b" and alumno_encontrado:
            
            nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del alumno: ")
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno: ")
            nuevo_tutor = input("Ingrese el nuevo nombre y apellido del tutor: ")

            funciones.modificarinfo_alumno(alumno_encontrado, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento, nuevo_tutor)
            print("Datos del alumno modificados correctamente.")
        elif opcion == "c" and alumno_encontrado:
            
            print("Dato disponibles para modificar:")
            print(", ".join(alumno_encontrado.keys()))
            dato_a_modificar = input("Ingrese el dato que desea modificar: ")
            nuevo_valor = input(f"Ingrese el nuevo valor para '{dato_a_modificar}': ")

            funciones.modificar_dato(alumno_encontrado, dato_a_modificar, nuevo_valor)
        elif opcion == "e" and alumno_encontrado:
            funciones.expulsar_alumno(Datos, nombre_alumno)
        elif not alumno_encontrado:
            print(f"No se encontró ningún alumnio con el nombre: {nombre_alumno}.")
    else:
        print("Esta opcion no es valida. Por favor ingrese una de las opciones que salen en pantalla")