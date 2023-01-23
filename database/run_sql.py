import os
import yaml
import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):

    conn=None
    results=[]

    config=get_config()
    dbapp=config['db_connection']

    try:
        conn=psycopg2.connect(dbapp)
        cur=conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql,values)
        conn.commit()
        results=cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()

    return results

def get_config():

    with open("SimpleWebApp\config.yml","r") as f:
        config = yaml.safe_load(f)

    return config