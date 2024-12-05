import psycopg2


def connect_to_db(query, params):
    conn = psycopg2.connect(dbname='postgres', **params)
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute(query, params)
    result = cur.fetchall()
    return result

