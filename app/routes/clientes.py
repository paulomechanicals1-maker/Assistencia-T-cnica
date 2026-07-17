from flask import Blueprint, render_template

clientes_bp = Blueprint(
    "Clientes",
    __name__
)

@clientes_bp.route("/")
def dashboard():
    return render_template("dashboard.html")