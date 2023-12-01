from waitress import serve

from resources.routes import initialize_routes
from utils.config import *

# Iniciar rotas
initialize_routes(api)

# Executar aplicacao
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8085)
