from flask_restful import Api, Resource
from app import app
api = Api(app)


class Index(Resource):
    def get(self):
        return {'index': 'index'}


api.add_resource(Index, '/')
