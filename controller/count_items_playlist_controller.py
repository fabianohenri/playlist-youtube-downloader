from pytube import Playlist


class CountItemsPlaylistController:

    @staticmethod
    def run(url_playlist):
        playlist = Playlist(url_playlist)
        stream_count = len(playlist.video_urls)
        stream_title = playlist.title
        return {"title": stream_title,
                "total_streams": stream_count}

