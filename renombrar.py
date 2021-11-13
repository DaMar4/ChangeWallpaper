import pathlib
import os
from time import sleep
a2=[]
a=0
def f2():   
    #original
    ejemplo_dir = '/home/daniel/.local/share/backgrounds'
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        nombre=str(fichero.name)
        extension=len(nombre)
        nuevonombre=nombre[:extension-4]
        print(nuevonombre,"-->",nuevonombre.replace(" ",""))
        a2.append(nuevonombre.replace(" ",""))
    for i in range(len(a2)):
        if(i<=len(a2)):
            break
        else:
            print(a2(i))

def f3():
    for path in pathlib.Path("/home/daniel/.local/share/backgrounds").iterdir():
        if path.is_file():
            global a
            old_name = path.stem
            directory = path.parent
            new_name = a2[a]+".jpg"
            a+=1
            path.rename(pathlib.Path(directory, new_name))
    print(a,"Archivos renombrados exitosamente")
f2()
f3()
