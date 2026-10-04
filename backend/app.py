from flask import Flask
from flask_cors import CORS
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from routes.health import health_bp
    from routes.sessions import sessions_bp
    from routes.quest import quest_bp
    from routes.recordings import recordings_bp

    app.register_blueprint(health_bp, url_prefix="/api/v1")
    app.register_blueprint(sessions_bp, url_prefix="/api/v1/sessions")
    app.register_blueprint(quest_bp, url_prefix="/api/v1/quest")
    app.register_blueprint(recordings_bp, url_prefix="/api/v1/recordings")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
