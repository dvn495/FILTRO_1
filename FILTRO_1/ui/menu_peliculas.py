import os
import funciones.peliculas as peliculas
import ui.menus as menu

def gestorpeliculas():
    os.system("cls")
    peliculas.cf.checkfile(peliculas.blockbuster)
    diccionariop = {}
    isActive = True
    while isActive:
        menu.menupeliculas()
        select = True
        while select:
            try:
                seleccion = int(input(":)_"))
                select = False
            except ValueError:
                print("ERROR EN EL DATO INGRESADO")
                os.system("pause")
        if seleccion == 1:
            creacion = True
            while creacion:
                os.system("cls")
                id = input("IDENTIFICACION DE LA NUEVA PELICULA: ")
                nombre = input("NOMBRE DE LA NUEVA PELICULA: ")
                duracion = input("DURACION DE LA NUEVA PELICULA: ")
                sinposis = input("SINOPSIS DE LA NUEVA PELICULA: ")
                
                idregistrar = id
                peliculas1 ={
                    idregistrar : {
                    "id":id,
                    "nombre":nombre,
                    "duracion": duracion,
                    "sinopsis": sinposis
                    }
                }
                creacion = bool(input("¿Desea registrar otro genero? Enter para si: "))==False
            diccionariop.update(peliculas1)
            peliculas.newmovie(diccionariop)  
                         
        elif seleccion == 2:
            os.system("cls")
            idbuscado = peliculas.search()
            if(len(idbuscado)):
                peliculas.modify(idbuscado["id"],idbuscado)
            #listageneros = gener.cf.readfile()
            #print(listageneros)
            os.system("pause")
        elif seleccion == 3:
            os.system("cls")
            peliculas.delete()
            print ("LA PELICULA FUE ELIMINADA SATISFACTORIAMENTE")
            os.system("pause")
        elif seleccion == 4:
            os.system("cls")
            print("SIN TERMINAR")
            os.system("pause")
        elif seleccion == 5:
            idbuscado = peliculas.search()
            print (idbuscado)
            os.system("pause")
        elif seleccion == 6:
            listapeliculas = peliculas.cf.readfile()
            print(listapeliculas["blockbuster"]["peliculas"])
            os.system("pause")
        elif seleccion == 7:
            isActive = False