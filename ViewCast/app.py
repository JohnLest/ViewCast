from flask import Flask
from flask_session import Session
from flask_openapi3 import OpenAPI, OAuthConfig
from flask_openapi3.models.security import OAuth2, OAuthFlows, OAuthFlowImplicit


from logging.config import dictConfig
from views.views.views import app as route
from views.views.openapi import app as api

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


oauth_config = OAuthConfig(
    clientId="xxx",
    clientSecret="xxx"
)

oauth2 = OAuth2(flows=OAuthFlows(
    implicit=OAuthFlowImplicit(
        authorizationUrl="/openapi/swagger/",
        scopes={
            "write:pets": "modify pets in your account",
            "read:pets": "read your pets"
        }
    )))
security_schemes = {"oauth2": oauth2}

app = OpenAPI(__name__, oauth_config=oauth_config, security_schemes=security_schemes)
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SESSION_TYPE"] = "filesystem"

Session(app=app)
app.register_blueprint(route)
app.register_api(api)


if __name__ == '__main__':
    app.run()
