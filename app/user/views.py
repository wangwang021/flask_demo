from .import user
from flask_restful import Api, Resource
# from flask_cors import cross_origin
api = Api(user)


class UserIndex(Resource):
    def get(self):
        return {'index': 'user.index'}

    # def options(self):
    #     return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
    #                                 'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
    #                                 'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
    #                                 }


api.add_resource(UserIndex, '/user')
