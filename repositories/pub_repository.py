import random

from db.run_sql import run_sql

from models.pub import Pub

def save(pub):
    sql = "INSERT INTO pubs (name) VALUES (%s) RETURNING *"
    values = [pub.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    pub.id = id

def select_all():
    pubs = []

    sql = "SELECT * FROM pubs"
    results = run_sql(sql)

    for row in results:
        pub = Pub(row['name'], row['id'])
        pubs.append(pub)

    return pubs

def delete_all():
    sql = "DELETE FROM pubs"
    run_sql(sql)

def get_pub(pubs):
    return random.choice(pubs)
