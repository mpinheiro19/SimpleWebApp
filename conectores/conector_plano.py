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
