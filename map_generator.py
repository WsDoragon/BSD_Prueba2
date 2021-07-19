from os import read
from tkinter.constants import GROOVE
from typing import Text
import pandas as pd
from folium.plugins import MarkerCluster
import folium  # pip install folium
import pymongo
import tkinter as tk
from tkinter import messagebox as mb
import webbrowser
import playsound

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Prueba2"]
mycol = mydb["audio"]


# Muestra todos los puntos en el mapa de la base de datos
def showAll():
    url = "mapOutputShowAll.html"
    # Define coordinates of where we want to center our map
    valdivia_coords = [-39.8139, -73.2458]

    # Create the map
    my_map = folium.Map(location=valdivia_coords, zoom_start=13)
    i = 1
    for doc in mycol.find({}):
        coords = [doc['latitud'], doc['longitud']]
        folium.Marker(coords, popup="ID:"+str(doc['_id'])+"\nFecha:"+doc['fecha de grabacion']
                      + "\nLatitud:"+doc['latitud']
                      + "\nLongitud:"+doc['longitud']
                      # + "\nFuente:" +
                      # doc['segmentos'[{'etiquetas': {'nombre_fuente'}}]]

                      ).add_to(my_map)
        print("coordenada ", i, " agregada al mapa")
        i += 1
    my_map.save(url)

    webbrowser.open(url)

# Muestra los puntos de un dia especifico almacenados en la base de datos


def daySpec(day):
    url = "mapOutputSpecificDay.html"
    # Define coordinates of where we want to center our map
    valdivia_coords = [-39.8139, -73.2458]

    # Create the map
    my_map = folium.Map(location=valdivia_coords, zoom_start=13)
    i = 1
    for doc in mycol.find({"fecha de grabacion": day}):
        coords = [doc['latitud'], doc['longitud']]

        # añadido de marcadores con informacion
        folium.Marker(coords, popup="ID:"+str(doc['_id'])+"\nFecha:"+doc['fecha de grabacion'] +
                      "\nLatitud:"+doc['latitud'] +
                      "\nLongitud:"+doc['longitud']
                      # +"\nFuente:"+doc['segmentos.etiquetas.categoria']

                      ).add_to(my_map)
        print("coordenada ", i, " agregada al mapa")
        i += 1

    my_map.save(url)

    webbrowser.open(url)


# muestra la categoria especifica
def catSpec(cat):
    url = "mapOutputSpecificCat.html"
    # Define coordinates of where we want to center our map
    valdivia_coords = [-39.8139, -73.2458]

    # Create the map
    my_map = folium.Map(location=valdivia_coords, zoom_start=13)
    i = 1
    for doc in mycol.find({'segmentos.etiquetas.categoria': cat}):
        coords = [doc['latitud'], doc['longitud']]
        folium.Marker(coords, popup="ID:"+str(doc['_id'])+"\nFecha:"+doc['fecha de grabacion'] +
                      "\nLatitud:"+doc['latitud'] +
                      "\nLongitud:"+doc['longitud']
                      #+ "\nFuente:"+doc['segmentos.etiquetas.categoria']

                      ).add_to(my_map)
        print("coordenada ", i, " agregada al mapa")

        i += 1
    my_map.save(url)

    webbrowser.open(url)


# Escuchar audio especifico
def specListen(id):
    # salida y reproduccion de audio de la base de datos
    info = mycol.find_one({"_id": id})
    nom = "salida_" + info['nombre_archivo']
    with open(nom, "wb") as f:
        f.write(info['archivo'])
    print("Archivo de audio " + nom + " descargado")
    playsound.playsound(nom)

#-#-#-#-#-#-#-#-# cerrar app #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


def ExitApplication(r):
    r.iconify()
    MsgBox = mb.askquestion(
        'Exit Application', '¿Desea finalizar sus busquedas?\n(Se cerrara el programa)', icon='warning')
    if MsgBox == 'yes':
        r.destroy()
    else:
        r.deiconify()
        tk.messagebox.showinfo(
            'Return', 'Volvera enseguida al programa')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


def main():
    r = tk.Tk()

    r.title('Audio Map Gen')
    r.geometry('360x540')

    # variables para consultas
    date_var = tk.StringVar()
    cat_var = tk.StringVar()
    id_var = tk.StringVar()

    # Labels de texto
    labelIn = tk.Label(
        r, text="\nBienvenido a la consulta de datos de la BSD.\n\nPara mostrar todos los puntos presione el boton inferior")

    labelDay = tk.Label(
        r, text="\nPara consultar por una fecha especifica introduzca\n la fecha y presione buscar por fecha\nFormato busqueda: dd/mm/yyyy\n(03/06/2021)")

    labelCat = tk.Label(
        r, text="\nPara consultar por una categoria especifica introduzca\n la categoria y presione buscar categoria\n(WIP:se acepta una entrada)")

    labelCats = tk.Message(
        r, text="Categorias:\n1.Humanos\n2.Música\n3.Animales\n4.Climáticos y Medio ambientales\n5.Mecánicos\n6.Vehiculos\n7.Alertas", anchor="w", relief=GROOVE)

    labelListen = tk.Label(r, text="\nIngrese ID de audio que desea escuchar:")

    # Variables de busqueda
    date = tk.Entry(r, textvariable=date_var)
    cat = tk.Entry(r, textvariable=cat_var)
    audio = tk.Entry(r, textvariable=id_var)

    # Botones de consultas
    buttonAll = tk.Button(r, text='Mostrar todos los puntos',
                          command=lambda: [
                              showAll(), ExitApplication(r)])

    buttonDay = tk.Button(r, text='Buscar dia especifico',
                          command=lambda: [
                              daySpec(date_var.get()), ExitApplication(r)]
                          )

    buttonSpec = tk.Button(r, text='Buscar categoria especifica',
                           command=lambda: [
                               catSpec(cat_var.get()), ExitApplication(r)]
                           )

    buttonListen = tk.Button(r, text="Reproducir audio", command=lambda: [
                             specListen(int(id_var.get())), ExitApplication(r)])
    # pack Todos los puntos
    labelIn.pack()
    buttonAll.pack()

    # pack dia especifico
    labelDay.pack()
    date.pack()
    buttonDay.pack()

    # pack categoria especifica
    labelCat.pack()
    cat.pack()
    buttonSpec.pack()
    labelCats.pack()

    # pack Escuchar audio especifico
    labelListen.pack()
    audio.pack()
    buttonListen.pack()

    r.resizable(False, False)
    r.mainloop()


main()
