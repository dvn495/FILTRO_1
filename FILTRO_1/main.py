import os
import ui.menu_peliculas as mpeliculas
import ui.menu_generos as gener
import ui.menu_formatos as format
import ui.menu_actores as actor
import ui.menus as menu

if __name__ == '__main__':
    isActive = True
    seleccion = 0
    while isActive:
        os.system("cls")
        menu.menuprincipal()
        select = True
        while select:
            try:
                seleccion = int(input(":)_"))
                select = False
            except ValueError:
                print("ERROR AL INGRESAR EL DATO")
                os.system("pause")
        if seleccion == 1:
            gener.gestorgeneros()           
        elif seleccion == 2:
            actor.gestoractores()
        elif seleccion == 3:
            format.gestorformatos()
        elif seleccion == 4:
            os.system("cls")
            print("SIN TERMINAR")
            os.system("pause")
        elif seleccion == 5:
            mpeliculas.gestorpeliculas()
        elif seleccion == 6:
            isActive = False
    
        
        
        