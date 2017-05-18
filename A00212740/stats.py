from flask import Flask, abort, request
import json
from flask_restplus import Resource, Api
from flask_restplus import fields

from comandos import get_all_stats, get_hdd, get_cpu, get_service

app = Flask(__name__)
#api_url= '/v1.0'
api = Api(app,version='1.0', title='API for resource management', description='Documentacion Proyecto Final Sistemas operativos')

ns = api.namespace('v1.0/stats', description='Operaciones para ver los recursos de servidor Ubuntu 16.04')
@ns.route('/')
#@app.route(api_url+'/stats', methods=['GET'])
class StatsCollection(Resource):
 @api.response(200, 'Recursos usados.')
 def get(self):
  """Lista de recursos"""
  list = {}
  list["RAM en uso:"] = get_all_stats()[1]
  list["HDD disponible:"] = get_hdd()[1]
  list["% uso de CPU"] = get_cpu()[2]
  list["Estado httpd:"] = get_service()
  return json.dumps(list),200

 @api.response(404, 'HTTP 404 NOT FOUND')
 def post(self):
  """NO APLICA"""
  return "HTTP 404 NOT FOUND", 404

 @api.response(404, 'HTTP 404 NOT FOUND')
 def put(self):
  """NO APLICA"""
  return "HTTP 404 NOT FOUND", 404

 @api.response(404, 'HTTP 404 NOT FOUND')
 def delete(self):
  """NO APLICA"""
  return "HTTP 404 NOT FOUND", 404


if __name__=="__main__":

  app.run(host='0.0.0.0', port=8080, debug='True')
