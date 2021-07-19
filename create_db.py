
import pymongo
from bson.binary import Binary
from bson import ObjectId

import add_wavfile as aw

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Prueba2"]
mycol = mydb["audio"]

# Insert de los datos a base de datos
mycol.insert_many([{"_id": 1,
                    "nombre_archivo": "bark.wav",
                    "archivo": '',
                    "fecha de grabacion": "03/06/2021",
                    "ciudad": "Valdivia",
                    "duracion": "17",
                    "formato": ".wav",
                    "latitud": "-39.827960",
                    "longitud": "-73.237042",
                    "exterior": "si",
                    "usuario": {"RUT": "20318537-5", "nombre": "Jorge", "apellido": "González"},
                    "segmentos":
                        {"ID": "1",
                         "formato": ".wav",
                         "duracion": "",
                         "inicio": "0",
                         "fin": "17",
                         "etiquetas": [{"nombre_fuente": "perro",
                                        "descripcion": "Perro ladrando frente al supermercado",
                                        "categoria": "3",
                                        "id_analizador": "3"}]
                         }},
                   {"_id": 2,
                   "nombre_archivo": "crowd.wav",
                    "archivo": '',
                    "fecha de grabacion": "01/07/2021",
                    "ciudad": "Valdivia",
                    "duracion": "5",
                    "formato": ".wav",
                    "latitud": "-39.832648",
                    "longitud": "-73.239542",
                    "exterior": "si",
                    "usuario": {"RUT": "20318537-5", "nombre": "Jorge", "apellido": "González"},
                    "segmentos":
                        {"ID": '1',
                         "formato": ".wav",
                         "duracion": "",
                         "inicio": "0",
                         "fin": "5",
                         "etiquetas": [{"nombre_fuente": "perro",
                                        "descripcion": "gritos y aplausos fuera del hospital base",
                                        "categoria": "1",
                                        "id_analizador": "2"}]
                         }},
                   {"_id": 3,
                   "nombre_archivo": "acordion.wav",
                    "archivo": '',
                    "fecha de grabacion": "01/07/2021",
                    "ciudad": "Valdivia",
                    "duracion": "2",
                    "formato": ".wav",
                    "latitud": "-39.815904",
                    "longitud": "-73.242966",
                    "exterior": "si",
                    "usuario": {"RUT": "20318537-5", "nombre": "Jorge", "apellido": "González"},
                    "segmentos":
                        [{"ID": "1",
                         "formato": ".wav",
                          "duracion": "10",
                          "inicio": "0",
                          "fin": "2",
                          "etiquetas": [{"nombre_fuente": "Humano",
                                        "descripcion": "persona tocando acordion fuera del mall plaza valdivia",
                                         "categoria": "2",
                                         "id_analizador": "1"}]
                          }]}])

# comentado para ver el ingreso de datos antes de subir archivos a la base de datos
# puede ejecutarse directamente desde ADD_WAVfile.py o descomentando aw.main()
# aw.main()
print(mydb.list_collection_names())
