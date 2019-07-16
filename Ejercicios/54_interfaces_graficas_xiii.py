from tkinter import *
from tkinter import filedialog

raiz = Tk()
raiz.title("Ejemplo de file chooser")

def abreFichero():
    # Se le indica dónde comenzar a buscar y qué tipo de ficheros puede abrir.
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="/home/", filetypes=(
        ("Ficheros imágenes", "*.jpg"), 
        ("Ficheros de imágenes", "*.png"),
        ("Todos los ficheros", "*.*")
        )) 
    print(fichero) # Solo imprime la ruta del archivo

Button(raiz, text="Abrir fichero", command=abreFichero).pack()

raiz.mainloop()