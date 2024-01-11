import os 
import funciones.generos as gener
import ui.menus as menu

def gestorgeneros():
    os.system("cls")
    gener.cf.checkfile(gener.generos)
    diccionariog = {}
    isActive = True
    while isActive:
        menu.menugeneros()
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
                id = input("IDENTIFICACION DEL NUEVO GENERO: ")
                nombre = input("NOMBRE DE EL NUEVO GENERO: ")
                idregistrar = id
                generos1 ={
                    idregistrar : {
                    "id":id,
                    "nombre":nombre
                    }
                }
                creacion = bool(input("¿Desea registrar otro genero? Enter para si: "))==False
            diccionariog.update(generos1)
            gener.newmovie(diccionariog)  
                         
        elif seleccion == 2:
            listageneros = gener.cf.readfile()
            print(listageneros)
            os.system("pause")
        elif seleccion == 3:
            isActive = False
        
        
        
        

    