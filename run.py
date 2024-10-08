from app import create_app
import os
from flask import Flask

app = Flask(__name__,
            static_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static'),
            template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates'))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
