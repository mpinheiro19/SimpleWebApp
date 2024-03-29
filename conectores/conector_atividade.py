from classes.cliente import Cliente
from classes.atividade import Atividade
import conectores.conector_plano as plano
import conectores.conector_instrutor as instrutor
from database.run_sql import run_sql, get_config

def get_all():

    atividades = []

    sql_query = "SELECT * FROM webuser.tb_atividades"
    results = run_sql(sql_query)

    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])
        nome_instrutor = instrutor.get_one(row['instrutor'])

        item = Atividade(
            row["nome"],
            nome_instrutor.nome +" "+ nome_instrutor.sobrenome,
            row["data_atividade"],
            row['duracao'],
            row['capacidade'],
            tipo_plano.plano,
            row['ativo'],
            row['id']
            )
        
        atividades.append(item)

    return atividades

def get_members(id : int):

    clientes =[]

    sql = f"""select cliente.* from webuser.tb_clientes as cliente 
    inner join webuser.tb_agendamento agd 
    on agd.cliente = cliente.id 
    where agd.atividade = {id};"""

    value = [id]

    results = run_sql(sql, value)
    
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
    
    
def get_all_active_ordered():

    atividades = []

    sql_query = "SELECT * FROM WEBUSER.TB_ATIVIDADES WHERE ATIVO = TRUE ORDER BY DATA_ATIVIDADE ASC"
    results = run_sql(sql_query)

    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])
        nome_instrutor = instrutor.get_one(row['instrutor'])

        item = Atividade(
            row["nome"],
            nome_instrutor.nome,
            row["data_atividade"],
            row['duracao'],
            row['capacidade'],
            tipo_plano.plano,
            row['ativo'],
            row['id']
            )
        
        atividades.append(item)

    return atividades

def get_all_active():

    atividades = []

    sql_query = "SELECT * FROM WEBUSER.TB_ATIVIDADES WHERE ATIVO = TRUE"
    results = run_sql(sql_query)

    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])
        nome_instrutor = instrutor.get_one(row['instrutor'])

        item = Atividade(
            row["nome"],
            nome_instrutor.nome,
            row["data_atividade"],
            row['duracao'],
            row['capacidade'],
            tipo_plano.plano,
            row['ativo'],
            row['id']
            )
        
        atividades.append(item)

    return atividades

def get_one(id : int):

    sql_query = f"SELECT * FROM webuser.tb_atividades where id = {id}"
    value = [id]

    results = run_sql(sql_query, value)[0]

    if results is not None:

        tipo_plano = plano.get_one(results["tipo_plano"])
        nome_instrutor = instrutor.get_one(results['instrutor'])

        atividade = Atividade(
            results["nome"],
            nome_instrutor.nome,
            results["data_atividade"],
            results['duracao'],
            results['capacidade'],
            tipo_plano.plano,
            results['ativo'],
            results['id']
            )

    return atividade

def get_n(n=10):

    atividades = []

    sql_query = f"SELECT * FROM webuser.tb_atividades limit {n}"
    results = run_sql(sql_query, n)

    for row in results:

        tipo_plano = plano.get_one(row["tipo_plano"])
        nome_instrutor = instrutor.get_one(row['instrutor'])

        atividade = Atividade(
            row["nome"],
            nome_instrutor.nome,
            row["data_atividade"],
            row['duracao'],
            row['capacidade'],
            tipo_plano.plano,
            row['ativo'],
            row['id']
            )
        
        atividades.append(atividade)

    return atividades

def edit_one(atividade : Atividade) -> None:

    sql = "UPDATE WEBUSER.TB_ATIVIDADES SET (nome, instrutor, data_atividade, duracao, capacidade, tipo_plano, ativo) = (%s,%s,%s,%s,%s,%s,%s) where id = %s;"
    
    values = [atividade.nome, 
    atividade.instrutor, 
    atividade.data_atividade, 
    atividade.duracao,
    atividade.capacidade,
    atividade.tipo_plano,
    atividade.ativo,
    atividade.id
    ]

    run_sql(sql, values)
    
    

def new(atividade : Atividade):
    
    sql = "INSERT INTO WEBUSER.TB_ATIVIDADES (nome, instrutor, data_atividade, duracao, capacidade, tipo_plano, ativo) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *;"
    values = [atividade.nome, atividade.instrutor, atividade.data_atividade, atividade.duracao, atividade.capacidade, atividade.tipo_plano, atividade.ativo]

    results = run_sql(sql, values)
    atividade.id = results[0]["id"]

    return atividade

def delete_one(id : int) -> None:
    sql = "DELETE FROM WEBUSER.TB_ATIVIDADES WHERE ID = %s"
    value = [id]

    run_sql(sql,value)

