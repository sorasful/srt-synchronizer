from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import routes, forms, methods