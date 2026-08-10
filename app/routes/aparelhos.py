from flask import Blueprint, render_template

aparelhos_bp = Blueprint(
    "aparelhos",
    __name__
)

@aparelhos_bp.route("/aparelhos")
def listar_aparelhos():

        return render_template(
            "aparelhos/listar.html"
        )