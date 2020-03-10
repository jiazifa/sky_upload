import os
from werkzeug.middleware.shared_data import SharedDataMiddleware
from app.config import Config
from app import create_app

main_app = create_app()
# application = SharedDataMiddleware(
#     main_app, {"/shared": os.path.join(Config().UPLOAD_FOLDER)}, cache=False,
# )
application = main_app

if __name__ == "__main__":
    main_app.wsgi_app = SharedDataMiddleware(
        main_app.wsgi_app,
        {"/shared": os.path.join(Config().UPLOAD_FOLDER)},
        cache=False,
    )
    main_app.run(host="localhost", port=9001, debug=True)
