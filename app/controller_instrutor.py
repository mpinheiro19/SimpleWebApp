from flask import render_template, request, redirect
from flask import Blueprint
from classes.instrutor import Instrutor
import conectores.conector_instrutor as conn


instructor_bp = Blueprint("instrutores", __name__)

@instructor_bp.route("/instrutores")
def instrutor_index():

    val = conn.get_all()

    render = render_template(
        "instrutores/index.html",
        instrutores = val,
        title = "Instrutores"
    )

    return render

@instructor_bp.route("/instrutores/<id>")
def exibir_detalhes(id):
    
    instrutor_atividades = conn.get_activities(id)
    instrutor = conn.get_one(id)

    render = render_template(
        "instrutores/mostrar.html",
        instrutor=instrutor,
        instrutor_atividades=instrutor_atividades,
        title="Detalhes"
    )

    return render

# @instructor_bp.route("/instrutores/novo")
# def novo_instrutor():
    
#     render=render_template(
#         "instrutores/novo.html",
#         title="Novo Cadastro"
#     )

#     return render

# @instructor_bp.route("/instrutores", methods = ["POST"])
# def cria_instrutor():

#     nome = request.form["nome"]
#     sobrenome = request.form["sobrenome"]
#     data_nascimento = request.form["data_nascimento"]
#     endereco = request.form["endereco"]
#     telefone = request.form["telefone"]

#     novo_instrutor = Instrutor(nome,sobrenome,data_nascimento,endereco,telefone)
#     conn.new(novo_instrutor)

#     return redirect("/instrutores")

@instructor_bp.route("/instrutores/<id>/edit")
def edita_instrutor(id):

    instrutor=conn.get_one(id)
    render=render_template(
        "instrutores/editar.html",
        instrutor=instrutor,
        title="Editar Informações"
    )

    return render

@instructor_bp.route("/instrutores/<id>",methods=["POST"])
def atualiza_instrutor(id):

    nome=request.form["nome"]
    sobrenome=request.form["sobrenome"]
    data_nascimento=request.form["data_nascimento"]
    endereco=request.form["endereco"]
    telefone=request.form["telefone"]

    instrutor_att=Instrutor(nome,sobrenome,data_nascimento,endereco,telefone,id)
    conn.edit_one(instrutor_att)

    return redirect("/instrutores")

@instructor_bp.route("/instrutores/<id>/delete")
def deletar_instrutor(id):
    conn.delete_instrutor(id)
    return redirect("/instrutores")