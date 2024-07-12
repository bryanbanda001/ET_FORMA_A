import random
import csv



trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez","Pedro Rodríguez","Laura Hernandez","Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

inventario= []


#asignacion de sueldos
def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        inventario.append({"nombre":trabajador, "sueldo":sueldo})
        
    


def clasificar_sueldos():
    #contadores para mas adelante identificar sueldos bajos altos y medios
    contador_sueldos_menores= 0
    contador_sueldos_medios = 0
    contador_sueldos_altos = 0

    suma_sueldos= 0
    sueldos = []

    bajos = []
    medianos = []
    altos= []

    #aqui ordenaremos los trabajadores segun su sueldo en diferentes listas
    for trabajador in inventario:
        sueldo = trabajador['sueldo']
        sueldos.append(sueldo)

        if sueldo < 800000:
            bajos.append(trabajador)
            contador_sueldos_menores= contador_sueldos_menores+ 1

        elif 800000 <= sueldo <=2000000:
            medianos.append(trabajador)
            contador_sueldos_medios= contador_sueldos_medios + 1 

        else:
            altos.append(trabajador)
            contador_sueldos_altos = contador_sueldos_altos +1

    
    #imprimiendo la estadistica de los trabajadores
            
    print(f"Sueldos menores a $800.000 TOTAL : {contador_sueldos_menores}")

    print("")

    for bajo in bajos:
        print(f"Nombre del empleado: {bajo['nombre']}")
        print(f"Sueldo del empleado: ${bajo['sueldo']}")
        print("")

    

    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL : {contador_sueldos_medios}")

    print("")

    for mediano in medianos:
        print(f"Nombre del empleado: {mediano['nombre']}")
        print(f"Sueldo del empleado: ${mediano['sueldo']}")
        print("")
        
        
        

    print(f"Sueldos mayores a $2.000.000 TOTAL : {contador_sueldos_altos}")

    print("")

    for alto in altos:
        print(f"Nombre del empleado: {alto['nombre']}")
        print(f"Sueldo del empleado: ${alto['sueldo']}")
        print("")

  
    

    #sumando los sueldos totales 
    suma_sueldos= sum(sueldos)

    print(f"TOTAL SUELDOS: ${suma_sueldos}")
    
    

            
def ver_estadistica():
    #si no hay inventario se terminara la funcion enviando un return
    if not inventario:
        print("no hay estadistica que mostrar")
        return 
    
    sueldos = []
    cantidades = len(sueldos)

    #ASIGNANDO LOS SUELDOS MAS ALTOS Y BAJOS

    sueldo_masalto= inventario[0]
    sueldo_masbajo= inventario[0]

    for trabajador in inventario:
        sueldos.append(trabajador["sueldo"])

        if trabajador["sueldo"] > sueldo_masalto["sueldo"]:
            sueldo_masalto = trabajador
        
        if trabajador["sueldo"] < sueldo_masbajo["sueldo"]:
            sueldo_masbajo = trabajador

    #promedio de sueldos
    promedio_sueldos = sum(sueldos)/len(sueldos)
    
    try:

        media_geometrica = 1
        for i in sueldos:
            media_geometrica= media_geometrica * i

        media_geometrica_final = (media_geometrica)** (1/len(sueldos)) 

    except ZeroDivisionError:
        print("no se puede dividir por 0")
    

    #IMPRIMIENDO LA ESTADISTICA
    print("")
    print("IMPRIMIENDO ESTADISTICA")
    print(f"Sueldo mas alto: {sueldo_masalto}")
    print("")
    print(f"Sueldo mas bajo: {sueldo_masbajo}")
    print("")
    print(f"Promedio de sueldos: {promedio_sueldos}")
    print("")
    print(f"Media Geometrica: {media_geometrica_final}")






#aqui se guardaran todos los datos creados anteriormente en un archivo csv con sus respectivos
def reporte_sueldos():
    with open("usuarios.csv", 'w',newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(['nombre','sueldo','descuento_salud','descuento_afp', 'sueldo_liquido'])

        for trabajador in inventario:

            nombre = trabajador['nombre']            
            sueldo = trabajador['sueldo']
            descuento_salud = sueldo * 0.93
            descuento_afp = sueldo * 0.88
            sueldo_liquido= sueldo - descuento_salud - descuento_afp


        writer.writerow([trabajador['nombre'], trabajador['sueldo'],descuento_salud,descuento_afp,sueldo_liquido])





def main():

    while True:
        print("")
        print("Menu")
        print("")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")        
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion= input("Ingresar opcion para ejecutar: ")
        
        opcion = int(opcion)

        if opcion == 1:
            asignar_sueldos()
            print("se han ingresado los sueldos de los trabajadores entre el rango al azar ($800.000, $2.500.000) correctamente")
            
                

        elif opcion == 2:
            clasificar_sueldos()

        
        elif opcion == 3:
            ver_estadistica()

        elif opcion == 4:
            reporte_sueldos()
            print("reporte hecho con exito")
            

        elif opcion == 5:
            print("")
            print("Finalizando programa...")
            print("")
            print("Desarrollado por Bryan  Banda")
            print("")
            print("RUT:21.954.316-6")


       


main()