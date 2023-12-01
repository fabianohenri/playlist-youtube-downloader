from flask_restful import Resource

from controller.status_controller import StatusController


class StatusApi(Resource):

    @staticmethod
    def get():
        response = StatusController().status()
        return response
