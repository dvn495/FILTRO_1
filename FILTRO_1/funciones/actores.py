import json
import os
import funciones.corefilaactores as cf
actores  ={
    
    
}
cf. MY_DATABASE = 'data/actores.json'

def newmovie (data:dict):
    actores.update(data)
    cf.adddata(actores)
    
def validararchivo():
    if(cf.checkfile()):
        print('ok')
        os.system("pause")
    else:
        cf.NewFile(actores)
        
def search()->dict:
    idbusqueda = int(input("Ingrese el codigo a buscar"))
    return actores.get(idbusqueda,{})

def delete():
    idbuqueda = int(input("Ingrese la pelicula a buscar"))
    cf.eliminardata(idbuqueda,actores)
    
def modify(llave:int, busqueda : dict):
    for key,item in busqueda.items():
        if((key != "Actores")):
            if(bool(input(f"Desea editar{key} enter para si: "))== False):
                busqueda[key]=input(f"Ingrese el nuevo dato para {key.capitalize()}: ")
    actores[str(llave)].update(busqueda)
    cf.NewFile(actores)