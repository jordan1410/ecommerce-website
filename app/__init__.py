from flask import Flask, session, render_template
from config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.extensions import db, login_manager, talisman
from models import Logins
import datetime


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    talisman.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Logins, int(user_id))

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = datetime.timedelta(minutes=10)
        session.modified = True

    # Initialize blueprints
    from .home.views import homeBP
    app.register_blueprint(homeBP)

    from .forms.views import formsBP
    app.register_blueprint(formsBP)

    from .admin.views import adminBP
    app.register_blueprint(adminBP)

    # default redirect page when request requires login
    login_manager.login_view = 'adminBP.adminLogin'

    # 404 Error Page (not found)
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("/404.html"), 404

    # 500 Error Page (internal error)
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template("/500.html"), 500

    return app
