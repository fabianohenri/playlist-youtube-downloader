from utils.logging_format import LoggingFormat
from flask import jsonify


class StatusController:

    @staticmethod
    def status():
        message = "Api respondendo com sucesso."
        LoggingFormat.format(message, "Sucess")
        return jsonify({"message": "Api respondendo com sucesso."})