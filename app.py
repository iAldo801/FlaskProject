from flask import Flask, current_app
from flask_cors import CORS

from routes.api.hello import hello_blueprint
from routes.api.user_info import user_info_blueprint
from routes.sections.home import home_blueprint
from routes.sections.auth.register import register_blueprint
from routes.sections.auth.login import login_blueprint
from routes.sections.auth.logout import logout_blueprint
from routes.sections.dashboard import dashboard_blueprint
from utils.db import create_users_table
from utils.limiter import init_limiter

app = Flask(__name__, template_folder="views", static_folder="assets")
app.config['SECRET_KEY'] = 'your_secret_key'

CORS(app)
limiter = init_limiter(app)
create_users_table()

limiter.limit("5 per minute")(login_blueprint)
limiter.limit("5 per minute")(register_blueprint)

def get_routes():
    routes = []
    for rule in current_app.url_map.iter_rules():
        if rule.endpoint != 'static': 
            routes.append((rule.endpoint, rule.rule))
    return routes

@app.context_processor
def inject_routes():
    return dict(routes=get_routes())

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