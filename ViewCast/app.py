from flask import Flask
from views.views.views import app as route

UPLOAD_FOLDER = 'C://media/john'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(route)


if __name__ == '__main__':
    app.run()
