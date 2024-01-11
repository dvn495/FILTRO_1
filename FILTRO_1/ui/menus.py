import os
menu = ["Administrador de Generos","Administrador de Actores","Administrador de Formatos","Gestor de informes","Gestor peliculas","Salir"]
menupeliculas1=["Agregar peliculas", "Editar peliculas", "Eliminar peliculas", "Eliminar actor", "Buscar peicula", "listar todas las peliculas", "Menu principal"]
def menuprincipal():
    header="""
    ++++++++++++++++++++++++++++
    ++++++ MENU PRINCIPAL ++++++
    ++++++++++++++++++++++++++++
    """
    print(header)
    for i,item in enumerate(menu):
        print(f"{i+1}-{item}")
    
def menugeneros():
    header="""
    +++++++++++++++++++++++++++++
    ++++ GESTOR  DE  GENEROS ++++
    +++++++++++++++++++++++++++++
    """
    print(header)
    print("1-Crear genero\n2-listar generos\n3-Ir a menu principal")
    
def menuformatos():
    header="""
    ++++++++++++++++++++++++++++++
    ++++ GESTOR  DE  FORMATOS ++++
    ++++++++++++++++++++++++++++++
    """
    print(header)
    print("1-Crear formatos\n2-listar formatos\n3-Ir a menu principal")
    
def menuactores():
    header="""
    +++++++++++++++++++++++++++++
    ++++ GESTOR  DE  ACTORES ++++
    +++++++++++++++++++++++++++++
    """
    print(header)
    print("1-Crear actores\n2-listar actores\n3-Ir a menu principal")
    
def menupeliculas():
    header="""
    +++++++++++++++++++++++++++++
    +++++  GESTOR PELICULAS +++++
    +++++++++++++++++++++++++++++
    """
    print(header)
    for i,item in enumerate(menupeliculas1):
        print(f"{i+1}-{item}")
    

    