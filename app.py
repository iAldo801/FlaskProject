from flask import Flask
from flask_cors import CORS
from routes.api.hello import hello_blueprint
from routes.api.user_info import user_info_blueprint
from routes.sections.home import home_blueprint
from routes.sections.auth.register import register_blueprint
from routes.sections.auth.login import login_blueprint
from routes.sections.auth.logout import logout_blueprint
from routes.sections.dashboard import dashboard_blueprint
from utils.db import create_users_table

app = Flask(__name__, template_folder="views", static_folder="assets")
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)
create_users_table()

# Normal routes
app.register_blueprint(home_blueprint)

# Auth
app.register_blueprint(register_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(dashboard_blueprint)

# API's
app.register_blueprint(hello_blueprint)
app.register_blueprint(user_info_blueprint)

if __name__ == "__main__":
    app.run(port=8080, debug=True)