import os 
import funciones.formatos as format
import ui.menus as menu

def gestorformatos():
    os.system("cls")

    format.cf.checkfile(format.formatos)
    diccionariof = {}
    isActive = True
    while isActive:
        menu.menuformatos()
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
                id = input("IDENTIFICACION DEL NUEVO FORMATO: ")
                nombre = input("NOMBRE DE EL NUEVO FORMATO  : ")
                idregistrar = id
                formatos ={
                    idregistrar : {
                    "id":id,
                    "nombre":nombre
                    }
                }
                
                creacion = bool(input("¿Desea registrar otro genero? Enter para si: "))==False
            diccionariof.update(formatos)
            format.newmovie(diccionariof)  
                         
        elif seleccion == 2:
            listaformatos = format.cf.readfile()
            print(listaformatos)
            os.system("pause")
        elif seleccion == 3:
            isActive = False