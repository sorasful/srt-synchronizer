from app import app
from config import Config

if __name__ == "__main__":
    app.run(host=Config.HOST, debug=Config.DEBUG)
