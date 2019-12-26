import os
from werkzeug.middleware.shared_data import SharedDataMiddleware
from app import create_app
from config import configObj

main_app = create_app()
application = SharedDataMiddleware(
    main_app, {"/shared": os.path.join(configObj.UPLOAD_FOLDER)}, cache=False,
)

if __name__ == "__main__":
    main_app.wsgi_app = SharedDataMiddleware(
        main_app.wsgi_app,
        {"/shared": os.path.join(configObj.UPLOAD_FOLDER)},
        cache=False,
    )
    main_app.run(host="localhost", port=9001, debug=True)
