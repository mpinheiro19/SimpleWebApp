from flask import render_template, request, redirect
from flask import Blueprint
from classes.instrutor import Instrutor
import conectores.conector_instrutor as conn


bp = Blueprint("instrutores", __name__)

@bp.route("/instrutores")
def instrutor_index():

    val = conn.get_all()
    
    render = render_template(
        "instrutores/index.html",
        instrutores = val,
        title = "Instrutores"
    )