from .import user
from flask_restful import Api,Resource

api=Api(user)

class UserIndex(Resource):
    def get(self):
        return {'index':'user.index'}

api.add_resource(UserIndex,'/user')