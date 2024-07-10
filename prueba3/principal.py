import funciones as fn
trabajadores = [
    'Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez',
    'Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez'
    ]
sueldos_trabajador = {} 
while True:
    print("-----(Menú Trabajadores)-----")
    print("(0) - Inializar creditos")
    print("(1) - Asignar sueldos aleatorios")
    print("(2) - Clasificar sueldos")
    print("(3) - Ver Estadisticas")
    print("(4) - Reporte de Sueldos")
    print("(5) - Salir del programa")

    opc = int(input("Ingrese una opción válida: "))

    if opc == 0:
        sueldos_trabajador = {trabajador : 0 for trabajador in trabajadores}
        print("Inializado con exito!")
    elif opc == 1:
        if not sueldos_trabajador:
            print("Primero debes inializar")
        else:
            sueldos_trabajador = fn.sueldoaleatorio(trabajadores)
    elif opc == 2:
        if sueldos_trabajador:
            fn.clasificar_sueldos(sueldos_trabajador)
    elif opc == 3:
        if sueldos_trabajador:
            max_sueldos,min_sueldos,promedio_sueldo = fn.calcular_estadisticas(sueldos_trabajador)
            if max_sueldos is not None:
                print("Sueldo Mas Alto: $",max_sueldos)
                print("Sueldo Mas Bajo: $",min_sueldos)
                print("Promedio de Sueldos: $",promedio_sueldo)
                ##PENDIENTE MEDIA GEOMETRICA!!!!!!
            else:
                print("Debes asignar sueldos primero!")
    elif opc == 4:
        if sueldos_trabajador:
            fn.generar_reportesueldos(sueldos_trabajador)
            print("")
        else:
            print("Asigna sueldos primero!")        
    elif opc == 5:
        print("Finalizando programa...")
        print("Desarrollado por Benjamin Briceño")
        print("RUT 22.016.962-6")
        break



