from classes.cliente import Cliente
from classes.atividade import Atividade
import conectores.conector_plano as plano
import conectores.conector_instrutor as instrutor
from database.run_sql import run_sql, get_config

def get_all():
    
    clientes = []

    sql = "SELECT * FROM WEBUSER.TB_CLIENTES"
    results = run_sql(sql)

    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])

        cliente = Cliente(
            row["nome"],
            row["sobrenome"],
            row["data_nascimento"],
            row["endereco"],
            row["telefone"],
            row["email"],
            tipo_plano.plano,
            row["data_inicio"],
            row["ativo"],
            row["id"]
        )

        clientes.append(cliente)

    return clientes


def get_one(id : int):
      
    clientes = []

    sql = f"SELECT * FROM WEBUSER.TB_CLIENTES where id = {id}"
    value = [id]

    results = run_sql(sql, value)[0]

    if results is not None:

        tipo_plano = plano.get_one(results["tipo_plano"])

        cliente = Cliente(
            results["nome"],
            results["sobrenome"],
            results["data_nascimento"],
            results["endereco"],
            results["telefone"],
            results["email"],
            tipo_plano.plano,
            results["data_inicio"],
            results["ativo"],
            results["id"]
        )

    return cliente  

def get_n(n=10):

    clientes = []

    sql = f"SELECT * FROM WEBUSER.TB_CLIENTES LIMIT {n}"
    value = n
    results = run_sql(sql)

    for row in results:

        cliente = Cliente(
            row["nome"],
            row["sobrenome"],
            row["data_nascimento"],
            row["endereco"],
            row["telefone"],
            row["email"],
            row["tipo_plano"],
            row["data_inicio"],
            row["ativo"],
            row["id"]
        )

        clientes.append(cliente)

    return clientes

def new_cliente(cliente : Cliente):

    values = [
        cliente.nome,
        cliente.sobrenome,
        cliente.data_nascimento,
        cliente.endereco,
        cliente.telefone,
        cliente.email,
        cliente.tipo_plano,
        cliente.data_inicio,
        cliente.ativo
    ]

    sql = "INSERT INTO WEBUSER.TB_CLIENTES(nome,sobrenome,data_nascimento,endereco,telefone,email,tipo_plano,data_inicio,ativo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *;"

    results = run_sql(sql, values)
    cliente.id = results[0]['id']

    return cliente

def edit_one(cliente : Cliente) -> None:
    
    values = [
        cliente.nome,
        cliente.sobrenome,
        cliente.data_nascimento,
        cliente.endereco,
        cliente.telefone,
        cliente.email,
        cliente.tipo_plano,
        cliente.data_inicio,
        cliente.ativo,
        cliente.id
    ]

    sql = "UPDATE WEBUSER.TB_CLIENTES SET (nome,sobrenome,data_nascimento,endereco,telefone,email,tipo_plano,data_inicio,ativo) = (%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE ID = %s"
    run_sql(sql, values)

def delete_one(id : int) -> None:
    
    sql = "DELETE FROM WEBUSER.TB_CLIENTES WHERE ID = %s"
    values = [id]

    run_sql(sql, values)

def get_activitites(id : int) -> list:

    atividades = []

    sql = """select atv.* from webuser.tb_atividades atv
            inner join webuser.tb_agendamento agd
            on atv.id = agd.atividade
            where agd.cliente = %s"""
    
    value = [id]

    results = run_sql(sql, value)
    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])
        nome_instrutor = instrutor.get_one(row['instrutor'])

        atividade = Atividade(
            row['nome'],
            nome_instrutor.nome, 
            row['data_atividade'],
            row['duracao'],
            row['capacidade'],
            tipo_plano.plano,
            row['ativo'],
            row['id']
        )

        atividades.append(atividade)

    return atividades




def get_all_active(is_active = True) -> list:
    
    clientes = []

    sql = f"SELECT * FROM WEBUSER.TB_ATIVIDADE WHERE ATIVO = {is_active} ORDER BY NOME ASC"
    
    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])

        cliente = Cliente(
            row["nome"],
            row["sobrenome"],
            row["data_nascimento"],
            row["endereco"],
            row["telefone"],
            row["email"],
            tipo_plano.plano,
            row["data_inicio"],
            row["ativo"],
            row["id"]
        )

        clientes.append(cliente)
    
    return clientes

def get_all_inactive():
    return get_all_active(False)