import pymongo
import certifi

ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://alejo89:alejo123@registraduria-app.qrmr0ba.mongodb.net/bd_registro_academico?retryWrites=true&w=majority",tlsCAFile=ca)
baseDatos = client["bd_registro_academico"]
print(baseDatos.list_collection_names())
