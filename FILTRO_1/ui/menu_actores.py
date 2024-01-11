import os 
import funciones.actores as actor
import ui.menus as menu

def gestoractores():
    os.system("cls")    
    actor.cf.checkfile(actor.actores)
    diccionarioa = {}
    isActive = True
    while isActive:
        select = True
        menu.menuactores()
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
                id = input("IDENTIFICACION DEL NUEVO ACTOR: ")
                nombre = input("NOMBRE DE EL NUEVO ACTOR: ")
                idregistrar = id
                actor1 ={
                    idregistrar : {
                    "id":id,
                    "nombre":nombre
                    }
                }
                
                creacion = bool(input("¿Desea registrar otro actor? Enter para si: "))==False
            diccionarioa.update(actor1)
            actor.newmovie(diccionarioa)  
                         
        elif seleccion == 2:
            listaformatos = actor.cf.readfile()
            print(listaformatos)
            os.system("pause")
        elif seleccion == 3:
            isActive = False