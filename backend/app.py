from flask import Flask, render_template
from flask_cors import CORS
from routes.api.user import user_blueprint

app = Flask(__name__)
CORS(app)

# @app.routes

@app.route("/")
def main():
    return render_template("index.html")

# Blueprint/Routes registration (Blueprints are basically routes like in Express.js)

app.register_blueprint(user_blueprint)

# Options for running the app

if __name__ == "__main__":
    app.run(port=8080)