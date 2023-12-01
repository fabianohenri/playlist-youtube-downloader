from api.count_items_playlis_api import CountItemsPlaylistApi
from api.download_playlist_api import DownloadPlaylist
from api.status_api import StatusApi


def initialize_routes(app):
    # Rotas de acesso aos endpoints da API
    app.add_resource(StatusApi, '/status')

    #### Playlist ####
    # Download
    app.add_resource(DownloadPlaylist, '/playlist/download')

    # Count streams contents
    app.add_resource(CountItemsPlaylistApi, '/playlist/count')
