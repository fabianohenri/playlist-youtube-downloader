from pytube import Playlist, YouTube

from utils.logging_format import LoggingFormat


class CountItemsPlaylistController:

    @staticmethod
    def run(url_playlist):
        colection = {}
        playlist = Playlist(url_playlist)
        if not playlist:
            message = "Erro ao coletar os dados da playlist. " \
                      "Provavelmente ela está como privada. " \
                      "Confirme e tente novamente"
            LoggingFormat.format(message, "Error")
            return {"Error": message}

        stream_count = len(playlist.video_urls)
        stream_title = playlist.title
        if stream_count == 1:
            message = f"Contagem de vídeos da playlist: '{stream_title}' concluída. Foi encontrado: " \
                      f"{str(stream_count)} vídeos."
        elif stream_count == 0:
            message = f"Contagem de vídeos da playlist: '{stream_title}' concluída. " \
                      f"Não foi encontrado nenhum vídeo nessa playlist"
        else:
            message = f"Contagem de vídeos da playlist: '{stream_title}' concluída. Foram encontrados: " \
                      f"{str(stream_count)} vídeos."
        LoggingFormat.format(message, "Info")

        LoggingFormat.format("Coletando dados dos vídeos dessa playlist", "Info")
        playlist_links = playlist.video_urls
        for link in playlist_links:
            if link:
                try:
                    yt = YouTube(link)
                    stream_link = yt.watch_url
                    stream = yt.streams.filter(progressive=True, file_extension='mp4')\
                                       .order_by('resolution')\
                                       .desc().first()
                    stream_title = yt.title
                    stream_author = yt.author
                    stream_size = stream.filesize_mb

                    colection.update({f"{stream_title}": {"author": f"{stream_author}",
                                                          "size": f"{stream_size}MB",
                                                          "link": f"{stream_link}"
                                                          }
                                      })
                except Exception as e:
                    message = f"Erro ao tentar baixar o vídeo: {stream_title}. Erro: {str(e)}"
                    LoggingFormat.format(message, "Error")

        return {"message": message,
                "count": f"{str(stream_count)}",
                "data": colection}



