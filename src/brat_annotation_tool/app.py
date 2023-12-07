import os
from flask import Flask, Blueprint, redirect

# Prefix configuration
root_url_prefix = os.getenv('FLASK_APP_URL_PREFIX', '/')

# path to this file
my_dir = os.path.dirname(os.path.realpath(__file__))


# Create app
def create_app():
    app = Flask(__name__)
    root_bp = Blueprint("root", __name__, template_folder='templates')

    @root_bp.route("/")
    def hello_world():
        os.system(f'python3 {my_dir}/standalone.py')
        return "Hello brat"

    @root_bp.route("/brat")
    def brat():
        return redirect("http://0.0.0.0:8001")

    app.register_blueprint(root_bp, url_prefix=root_url_prefix)

    return app
