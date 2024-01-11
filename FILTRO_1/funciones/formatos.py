import json
import os
import funciones.corefilefunciones as cf
formatos  ={
    
    
}
cf. MY_DATABASE = 'data/formatos.json'

def newmovie (data:dict):
    formatos.update(data)
    cf.adddata(formatos)
    
def validararchivo():
    if(cf.checkfile()):
        print('ok')
        os.system("pause")
    else:
        cf.NewFile(formatos)
        
def search()->dict:
    idbusqueda = int(input("Ingrese el codigo a buscar"))
    return formatos.get(idbusqueda,{})

def delete():
    idbuqueda = int(input("Ingrese la pelicula a buscar"))
    cf.eliminardata(idbuqueda,formatos)
    
def modify(llave:int, busqueda : dict):
    for key,item in busqueda.items():
        if((key != "Actores")):
            if(bool(input(f"Desea editar{key} enter para si: "))== False):
                busqueda[key]=input(f"Ingrese el nuevo dato para {key.capitalize()}: ")
    formatos[str(llave)].update(busqueda)
    cf.NewFile(formatos)