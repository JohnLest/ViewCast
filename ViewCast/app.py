from flask import Flask
from views.app.views import  route as view


app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.register_blueprint(view)


if __name__ == '__main__':
    app.run()
