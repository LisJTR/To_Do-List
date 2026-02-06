
tareas = ["hacer deberes"]

while True:

    try:

        print("---- TO-DO LIST ----")

        print("MENÚ DE OPCIONES:")
        print("1- Mostrar todas las tareas")
        print("2- Añadir una tarea")
        print("3- Modificar una tarea")
        print("4- Eliminar una tarea")
        print("5- Salir")
        opcion = int(input("Introduce la opción deseada: "))




        match opcion:

            case 1:

                if len(tareas) > 0 :

                    for i, valor in enumerate(tareas):
                        print(i,valor )

                else:

                    print("No existe ninguna tarea que mostrar")   
        

            case 2:

                print("Donde desea añadir: ")
                print("1- Al final de la lista")
                print("2- Al princio")
                print("3- En un lugar especifico")
                print("4- Salir de esta opción")
                eleccion = int(input("opcion elegida: "))

                if eleccion == 1:

                    tarea = input("Introduzca su tarea: ")
                    tareas.append(tarea)

                elif eleccion == 2:
                
                    tarea = input("Introduzca su tarea: ")
                    tareas.insert(0,tarea)
                    
                elif eleccion == 3:

                    tarea = input("Introduzca su tarea: ")
                    posicion = int(input("Introduzca posición: "))
                    tareas.insert(posicion, tarea)

                elif eleccion == 4:
                    
                    continue

                else:
                    print("opción NO válida")


            case 3:

                n_tarea = int(input("Número de tarea a modificar: "))
                tarea = input("Intruduce tarea nueva")
                tareas[n_tarea] = tarea

            case 4:

                print("1- Eliminar una tarea especifica")
                print("2- Eliminar TODAS las tareas")
                eliminar = int(input("Introducir la opción a eleminar: "))

                if eliminar == 1:

                    E_posicion = int(input("Introduce la posición a eleminar: "))
                    tareas.pop(E_posicion)
                
                elif eliminar == 2:

                    print("Se procedera a eliminar TODA la lista")
                    tareas.clear()
                else:
                    print("Opción no válida")
            case 5:

                print("Fin")
                break

            case _:
                print ("Opcion No válida")

    except ValueError:
        
        print("El tipo dato introducido tiene que ser un NUMERO ENTERO")

    except IndexError:

        print("El número de ópcion esta fuera de rango")
