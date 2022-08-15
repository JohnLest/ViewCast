from flask import Flask
from flask_session import Session

from logging.config import dictConfig
from views.views.views import app as route

UPLOAD_FOLDER = 'E:\\Python\\viewcast\\ViewCast\\static\\medias'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': "%(levelname)s - %(asctime)s - %(message)s",
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SESSION_TYPE"] = "filesystem"

Session(app=app)
app.register_blueprint(route)


if __name__ == '__main__':
    app.run()
