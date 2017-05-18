from comandos import get_all_stats, get_hdd, get_cpu, get_service
import json, time
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/home/check_user/repositories/so-exam2/A00212740/database.db'
#db = SQLAlchemy(app)

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #  hdd = db.Column(db.String(80), nullable=False)
 #   cpu = db.Column(db.Float, nullable=False)
 #   service = db.Column(db.String(80), nullable=False)
 #   ram = db.Column(db.String(120), nullable=False)



archivo = open('dblocal.txt', 'a+')



#list={}
#list["RAM en uso:"] = get_all_stats()[1]
#list["HDD disponible:"] = get_hdd()[1]
#list["% uso de CPU"] = get_cpu()[2]
#list["Estado httpd:"] = get_service()

var1 = "RAM en uso: "+ get_all_stats()[1]
var2 = "HDD disponible: "+ get_hdd()[1]
var3 = "% uso de CPU: "+ get_cpu()[2]
var4 = "Estado servicio httpd: "+ get_service()[0]
varFecha = "Fecha y Hora: "+ time.strftime("%c")
archivo.write(varFecha+"\n")
archivo.write(var1+"\n")
archivo.write(var2+"\n")
archivo.write(var3+"\n")
archivo.write(var4+"\n")
archivo.write("\n")

archivo.close()
leer = open('dblocal.txt', 'r+')
print('<<<<DATOS>>>>')
print(leer.read())









