#Funcion para mostrar la informacion del alumno
def informacion_alumno(alumno):
    print("Datos del Alumno:")
    print(f"Nombre: {alumno['Nombre']}")
    print(f"Apellido: {alumno['Apellido']}")
    print(f"DNI: {alumno['DNI']}")
    print(f"Fecha de Nacimiento: {alumno['Fecha de nacimiento']}")
    print(f"Tutor: {alumno['Tutor']}")
    print(f"Notas: {alumno['Notas']}")
    print(f"Faltas: {alumno['Faltas']}")
    print(f"Amonestaciones: {alumno['Amonestaciones']}")

#Funcion para modificar la informacion de un alumno  
def modificarinfo_alumno(alumno, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento, nuevo_tutor,nuevas_notas,nuevas_faltas,nuevas_amonestaciones):
    alumno['Nombre'] = nuevo_nombre
    alumno['Apellido'] = nuevo_apellido
    alumno['Fecha de nacimiento'] = nueva_fecha_nacimiento
    alumno['Tutor'] = nuevo_tutor
    alumno['Notas'] = nuevas_notas
    alumno['Faltas'] = nuevas_faltas
    alumno['Amonestaciones']=nuevas_amonestaciones
##Funcion para agregar un alumno
def agregar_alumno(datos, nuevo_alumno):
    datos['Alumnos'].append(nuevo_alumno)
##Funcion para ingresar los datos de de un alumno   
def ingresar_datos_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    tutor = input("Ingrese el nombre y apellido del tutor: ")

    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    return nuevo_alumno

#Funcion para modificar un solo dato del alumno
def modificar_dato(alumno, dato, nuevo_valor):
    if dato in alumno:
        alumno[dato] = nuevo_valor
        print(f"Dato '{dato}' del alumno modificado exitosamente.")
    else:
        print(f"No se encontró el dato '{dato}' en la información del alumno.")

#Funcion para expulsar alumno
def expulsar_alumno(datos, nombre_alumno):
    for alumno in datos['Alumnos']:
        if alumno['Nombre'] == nombre_alumno:
            datos['Alumnos'].remove(alumno)
            print(f"Alumno con nombre {nombre_alumno} expulsado.")
            return
    print(f"No se encontró ningún alumno con ese nombre {nombre_alumno}.")