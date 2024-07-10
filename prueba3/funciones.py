import random
import csv

def sueldoaleatorio(trabajadores):
    sueldos_trabajador = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos_trabajador[trabajador] = sueldo

    print("Sueldos aleatorios aplicados con exito!")
    print(sueldos_trabajador)
    return sueldos_trabajador

def clasificar_sueldos(sueldos_trabajador):
    menor_800 = {}
    entre_800_2000 = {}
    mayor_2000 = {}

    for trabajador,sueldo in sueldos_trabajador.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800_2000[trabajador] = sueldo
        else:
            mayor_2000[trabajador] = sueldo

    print("Sueldos Menores a $800.000 TOTAL: ",len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print(trabajador,": $",sueldo)
    print("")
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ",len(entre_800_2000))
    for trabajador,sueldo in entre_800_2000.items():
        print(trabajador,": $",sueldo)
    print("")
    print("Sueldos superiores a $2.000.000 TOTAL: ",len(mayor_2000))
    for trabajador,sueldo in mayor_2000.items():
        print(trabajador,": $",sueldo)

def calcular_estadisticas(sueldos_trabajador):
    sueldos = list(sueldos_trabajador.values())
    
    if not sueldos:
        print("No se han asignado los sueldos aun")
        return None,None,None
    
    max_sueldos = max(sueldos)
    min_sueldos = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    return max_sueldos,min_sueldos,promedio_sueldo

def generar_reportesueldos(sueldos_trabajador):
    with open('reportes_sueldos.csv', 'w', newline='') as archivo:
        escribir = csv.writer(archivo, delimiter=',')
        
        escribir.writerow(['Nombre Trabajador', 'Sueldo', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])
        
        for trabajador, sueldo in sueldos_trabajador.items():
            descSalud = sueldo * 0.07
            descAFP = sueldo * 0.12
            liquidopagar = sueldo - descSalud - descAFP

            escribir.writerow([trabajador, sueldo, descSalud, descAFP, liquidopagar])
        
    print("Reporte de sueldos creado correctamente!")







    
      
    