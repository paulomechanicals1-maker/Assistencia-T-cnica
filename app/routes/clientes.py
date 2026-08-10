from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from app.models import Cliente


clientes_bp = Blueprint(
    "clientes",
    __name__
)


@clientes_bp.route("/")
def dashboard():

    return render_template(
        "dashboard.html"
    )


@clientes_bp.route("/clientes")
def listar_clientes():

    clientes = Cliente.listar()

    return render_template(
        "clientes/listar.html",
        clientes=clientes
    )


@clientes_bp.route(
    "/clientes/cadastrar",
    methods=["GET", "POST"]
)
def cadastrar_cliente():

    if request.method == "POST":

        Cliente.criar(
            request.form["nome"],
            request.form["cpf"],
            request.form["whatsapp"],
            request.form["email"],
            request.form["observacoes"]
        )

        return redirect(
            url_for("clientes.listar_clientes")
        )

    return render_template(
        "clientes/cadastrar.html"
    )