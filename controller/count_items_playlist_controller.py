from pytube import Playlist

from utils.logging_format import LoggingFormat


class CountItemsPlaylistController:

    @staticmethod
    def run(url_playlist):
        playlist = Playlist(url_playlist)
        if not playlist:
            message = "Erro ao coletar os dados da playlist. " \
                      "Provavelmente ela está como privada. " \
                      "Confirme e tente novamente"
            LoggingFormat.format(message, "Error")
            return {"Error": message}

        stream_count = len(playlist.video_urls)
        stream_title = playlist.title
        message = f"Contagem de vídeos da playlist: '{stream_title}' concluída. Foram encontrados: " \
                  f"{str(stream_count)} vídeos."
        LoggingFormat.format(message, "Info")
        return {"message": message}


