from flask import Flask

from app.database import criar_tabelas

def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object("config.Config")

    criar_tabelas()

    from app.routes.clientes import clientes_bp

    app.register_blueprint(clientes_bp)

    from app.routes.aparelhos import aparelhos_bp

    app.register_blueprint(aparelhos_bp)

    return app