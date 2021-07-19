import pymongo
import gridfs

from bson.binary import Binary
from bson import ObjectId


def main():
    db = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = db["Prueba2"]
    mycol = mydb["audio"]

    i = 1
    for doc in mycol.find({}):
        name = doc['nombre_archivo']
        with open(name, "rb") as f:
            encoded = Binary(f.read())
        mycol.update({"_id": i}, {"$set": {"archivo": encoded}})
        print("Archivo", i, "subido a base de datos")
        i += 1


main()
