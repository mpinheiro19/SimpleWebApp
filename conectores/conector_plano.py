from classes.plano import TipoPlano
from database.run_sql import run_sql, get_config

def get_all():

    tipos_planos = []

    sql_query = "SELECT * FROM webuser.tb_planos"
    results = run_sql(sql_query)

    for row in results:

        item = TipoPlano(
            row["plano"],
            row['id']
            )
        
        tipos_planos.append(item)

    return tipos_planos

def get_n(n = 10):

    tipos_planos = []

    sql_query = f"SELECT * FROM webuser.tb_planos limit {n}"
    results = run_sql(sql_query)

    for row in results:

        item = TipoPlano(
            row["plano"],
            row['id']
            )
        
        tipos_planos.append(item)

    return tipos_planos

def get_one(id : int):

    sql_query = f"SELECT * FROM webuser.tb_planos where id = {id}"
    value = [id]

    results = run_sql(sql_query, value)[0]

    if results is not None:
        tipo_plano = TipoPlano(results["plano"], results["id"])

    return tipo_plano


def edit_one(tipo_plano : TipoPlano) -> None:
    
    value = [tipo_plano.plano, tipo_plano.id]    
    sql = f"UPDATE webuser.tb_planos SET plano = '{tipo_plano.plano}' where id = {tipo_plano.id};"

    run_sql(sql, value)

def delete_one(id : int) -> None:
    
    sql_query = "DELETE FROM webuser.tb_planos where id = %s"
    value = [id]

    run_sql(sql_query, value)

def new(tipo_plano : TipoPlano):

    sql_query = "INSERT INTO webuser.tb_planos (plano) VALUES (%s) RETURNING *;"
    values = [tipo_plano.plano]

    results = run_sql(sql_query, values)

    tipo_plano.id = results[0]["id"]

    return tipo_plano

def get_user_confirmation():
    raise NotImplementedError