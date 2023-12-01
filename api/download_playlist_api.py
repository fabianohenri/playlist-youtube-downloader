from flask import request, jsonify
from flask_restful import Resource

from controller.download_playlist_controller import DownloadPlaylistController
from utils.logging_format import LoggingFormat


class DownloadPlaylist(Resource):

    def __init__(self):
        self.__url_playlist = request.get_json(silent=True)

    def get(self):
        LoggingFormat.format("Recebendo requisição para coletar um playlist.", "Info")

        # Validar se existe contúdo na requisição.
        if 'url' not in self.__url_playlist:
            message = "Requisitação inválida. Valor 'url' não informado."
            LoggingFormat.format(message, "Error")
            return jsonify({"message": message})

        response = DownloadPlaylistController.run(self.__url_playlist['url'])
        # Se existir chamo o controller
        return response
