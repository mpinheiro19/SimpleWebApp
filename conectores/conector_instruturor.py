from classes.instrutor import Instrutor
from classes.atividade import Atividade
from database.run_sql import run_sql, get_config

def get_all():

    instrutores = []

    sql_query = "SELECT * FROM webuser.tb_instrutores"
    results = run_sql(sql_query)

    for row in results:

        item = Instrutor(
            row["nome"],
            row["sobrenome"],
            row["data_nascimento"],
            row['endereco'],
            row['telefone'],
            row['id']
            )
        
        instrutores.append(item)

    return instrutores

def get_one(id : int):

    sql_query = f"SELECT * FROM webuser.tb_instrutores where id = {id}"
    value = [id]

    results = run_sql(sql_query, value)[0]

    if results is not None:
        instrutor = Instrutor(
            results["nome"],
            results["sobrenome"],
            results["data_nascimento"],
            results['endereco'],
            results['telefone'],
            results['id']
            )

    return instrutor

def get_n(n=10):

    instrutores = []

    sql_query = f"SELECT * FROM webuser.tb_instrutores limit {n}"
    results = run_sql(sql_query, n)

    for row in results:

        item = Instrutor(
            row["nome"],
            row["sobrenome"],
            row["data_nascimento"],
            row['endereco'],
            row['telefone'],
            row['id']
            )
        
        instrutores.append(item)

    return instrutores

def get_activities(instrutor_id):

    lista_atividades = []

    sql = "SELECT * FROM WEBUSER.TB_ATIVIDADES WHERE INSTRUTOR = %s"
    value = [instrutor_id]

    query_results = run_sql(sql, value)
    
    for item in query_results:

        atividade = Atividade(
            item["nome"],
            item["instrutor"],
            item["data_atividade"],
            item["duracao"],
            item["capacidade"],
            item["tipo_plano"],
            item['ativo'],
            item['id']
        )

        lista_atividades.append(atividade)

    return lista_atividades

def new(instrutor : Instrutor):
    
    value = [
        instrutor.nome,
        instrutor.sobrenome,
        instrutor.data_nascimento,
        instrutor.endereco,
        instrutor.telefone
        ]

    sql_query = "INSERT INTO webuser.tb_instrutores(nome, sobrenome,data_nascimento,endereco,telefone) VALUES (%s, %s, %s, %s, %s) RETURNING *;"

    results = run_sql(sql_query, value)

    instrutor.id = results[0]["id"]

    return instrutor

def edit_one(instrutor : Instrutor) -> None:
    
    value = [
        instrutor.nome,
        instrutor.sobrenome,
        instrutor.data_nascimento,
        instrutor.endereco,
        instrutor.telefone,
        instrutor.id
        ]

    sql = "UPDATE webuser.tb_instrutores SET ( nome, sobrenome, data_nascimento, endereco, telefone) = (%s,%s,%s,%s,%s) where id = %s;"

    run_sql(sql, value)

def delete_instrutor(id) -> None:
    sql = "DELETE FROM webuser.tb_instrutores where id = %s"
    value = [id]

    run_sql(sql, value)