import json
import os
import funciones.corefile as cf
generos  ={
    
    
}
cf. MY_DATABASE = 'data/generos.json'
def newmovie (data:dict):
    generos.update(data)
    cf.adddata(generos)
    
def validararchivo():
    if(cf.checkfile()):
        print('ok')
        os.system("pause")
    else:
        cf.NewFile(generos)
        
def search()->dict:
    idbusqueda = int(input("Ingrese el codigo a buscar"))
    return generos.get(idbusqueda,{})

def delete():
    idbuqueda = int(input("Ingrese la pelicula a buscar"))
    cf.eliminardata(idbuqueda,generos)
    
def modify(llave:int, busqueda : dict):
    for key,item in busqueda.items():
        if((key != "Actores")):
            if(bool(input(f"Desea editar{key} enter para si: "))== False):
                busqueda[key]=input(f"Ingrese el nuevo dato para {key.capitalize()}: ")
    generos[str(llave)].update(busqueda)
    cf.NewFile(generos)