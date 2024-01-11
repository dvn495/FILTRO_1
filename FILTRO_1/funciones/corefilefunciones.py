import os
import json
MY_DATABASE=' '

def NewFile(*param):
    with open(MY_DATABASE,"w")as wf:
        json.dump(param[0],wf,indent=4)

def adddata(*param):
    with open(MY_DATABASE,"r+")as rwf:
        data_file = json.load(rwf)
        if(len(param)> 1):
            data_file.update({param[0]:param[1]})
        else:
            data_file.update(param[0])
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)
        rwf.close()

def eliminar(*param):
    data = list(param)
    data[1].pop(data[0])
    NewFile (data[1])
    
def eliminardata(clave:int,*param):
    diccionario = param[0]
    if str(clave) in diccionario:#[][]:
        del diccionario[str(clave)]#[][][str(clave)]
        NewFile(diccionario)
    else:
        print ("NO SE ENCONTRO UNA PELICULA A ESE NOMBRE")
        os.system ("pause")
        
def readfile():
    with open(MY_DATABASE,"r")as rf:
        return json.load(rf)
    
def checkfile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(readfile())
    else:
        if(len(param)):
            NewFile(data[0])