import json
import os
import funciones.corefilepeliculas as cf
blockbuster  ={
    "blockbuster":{
        "peliculas" : {}
    }
    
    
}
cf. MY_DATABASE = 'data/PELICULAS.json'

def newmovie (data:dict):
    blockbuster["blockbuster"]["peliculas"].update(data)#[][].update(data)
    cf.adddata(blockbuster)
    
def validararchivo():
    if(cf.checkfile()):
        print('ok')
        os.system("pause")
    else:
        cf.NewFile(blockbuster)
        
def search()->dict:
    idbusqueda = (input("Ingrese el codigo a buscar: "))
    return blockbuster["blockbuster"]["peliculas"].get(idbusqueda,{})

def delete():
    idbuqueda = (input("Ingrese la pelicula a buscar: "))
    cf.eliminardata(idbuqueda,blockbuster["blockbuster"]["peliculas"])
    
def modify(llave:str, busqueda : dict):
    for key,item in busqueda.items():
        if((key != "Actores")and (key != "id")):
            if(bool(input(f"¿Desea editar {key}? enter para si: "))== False):
                busqueda[key]=input(f"Ingrese el nuevo dato para {key.capitalize()}: ")
    blockbuster["blockbuster"]["peliculas"][str(llave)].update(busqueda)#[][][str(llave)].update(busqueda)
    cf.NewFile(blockbuster)
    
#busqueda = peliculas.sarch()
#if(len(busqueda)):
#   peliculas.modify(busqueda[],busqueda)