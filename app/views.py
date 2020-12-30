from flask_restful import Api, Resource
from app import app
api = Api(app)


class Index(Resource):
    def get(self):
        return {'index': 'index'}

    # def options(self):
    #     return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
    #                                  'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
    #                                  'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
    #                                  }


api.add_resource(Index, '/')
