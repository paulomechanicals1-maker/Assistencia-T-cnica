from flask import Flask

def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object("config.Config")

    from app.routes.clientes import clientes_bp

    app.register_blueprint(clientes_bp)

    return app