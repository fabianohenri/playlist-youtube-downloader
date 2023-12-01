from pytube import Playlist, YouTube

from utils.logging_format import LoggingFormat


class DownloadPlaylistController:

    @staticmethod
    def run(url_playlist):

        colection = {}
        download_cont = 0
        playlist = Playlist(url_playlist)
        if not playlist:
            message = "Erro ao coletar os dados da playlist. " \
                      "Provavelmente ela está como privada. " \
                      "Confirme e tente novamente"
            LoggingFormat.format(message, "Error")
            return {"Error": message}

        LoggingFormat.format(f"Playlist: {playlist.title}, contem {len(playlist.video_urls)} vídeos.", "Info")
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

                    message = f"Iniciando o download do vídeo: {stream_title}, tamanho do arquivo: {stream_size}MB"
                    LoggingFormat.format(message, "Info")
                    stream.download(output_path='playlist')

                    download_cont += 1
                    colection.update({f"{stream_title}": {"author": f"{stream_author}",
                                                          "size": f"{stream_size}MB",
                                                          "link": f"{stream_link}"
                                                          }
                                      })
                    LoggingFormat.format("Dowload concluído.", "Success")
                except Exception as e:
                    message = f"Erro ao tentar baixar o vídeo: {stream_title}. Erro: {str(e)}"
                    LoggingFormat.format(message, "Error")

        LoggingFormat.format("Todos os vídeos da playlist, baixados com sucesso. "
                             f"Foram baixados {download_cont} vídeos.", "Success")
        return {"count": f"{str(download_cont)}",
                "data": colection}
