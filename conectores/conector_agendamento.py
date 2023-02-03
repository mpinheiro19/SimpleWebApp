from database.run_sql import run_sql, get_config
from classes.agendamento import Agendamento
import conectores.conector_atividade as atv
import conectores.conector_cliente as cli

def get_all() -> list:
    agendamentos = []

    sql = "SELECT * FROM WEBUSER.TB_AGENDAMENTO"

    results = run_sql(sql)

    for row in results:

        agendamento = Agendamento(
            row['atividade'],
            row['cliente'],
            row['id']
        )

        agendamentos.append(agendamento)
        
    return agendamentos

def get_n(n=10):
    agendamentos = []

    sql = "SELECT * FROM WEBUSER.TB_AGENDAMENTO limit %s"
    value = [n]

    results = run_sql(sql, value)

    for row in results:

        agendamento = Agendamento(
            row['atividade'],
            row['cliente'],
            row['id']
        )

        agendamentos.append(agendamento)
        
    return agendamentos

def get_one(id : int):

    sql = "SELECT * FROM WEBUSER.TB_AGENDAMENTO where id = %s"
    value = [id]

    results = run_sql(sql, value)[0]

    if results is not None:
        result = Agendamento(
            results['atividade'],
            results['cliente'],
            results['id']
        ) 

    return result


def new(agendamento : Agendamento):
    
    sql = "INSERT INTO WEBUSER.TB_AGENDAMENTO (atividade, cliente) values (%s,%s) returning *;"

    values = [
        agendamento.atividade,
        agendamento.cliente
    ]

    results = run_sql(sql,values)

    agendamento.id = results[0]['id']

    return agendamento

def delete_one(id : int) -> None:
    
    value=[id]
    sql = "DELETE FROM WEBUSER.TB_AGENDAMENTO WHERE id = %s;"

    run_sql(sql,value)

def deleta_agendamento_de_cliente(atividade_id : int, user_id : int) -> None:
    
    value=[atividade_id, user_id]
    sql = "DELETE FROM WEBUSER.TB_AGENDAMENTO WHERE atividade = %s and cliente = %s;"

    run_sql(sql,value)

def check_one(atividade_id, cliente_id):
        
    value=[atividade_id, cliente_id]
    sql = "select * from webuser.tb_agendamento where atividade = %s and cliente = %s"

    results = run_sql(sql,value)
    
    return (len(results) == 0)