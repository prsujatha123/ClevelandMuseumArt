from flask import Flask
import sqlite3,json


def extract_data():

   try:

    con = sqlite3.connect("cma-artworks.db")
    c = con.cursor()
    json_data = []
    sql = """
        select a.id as artwork_id,  a.accession_number, a.title, a.tombstone, ac.creator_id,c.role,c.description, ad.department_id, d.name as department_name
            from artwork a LEFT JOIN  artwork__creator ac on a.id=ac.artwork_id
            Left Join (select DISTINCT id, role, description from creator) as c
            on c.id = ac.creator_id
            left join artwork__department ad on ad.artwork_id = a.id
            Left join department d on d.id = ad.department_id
    """
    print(sql)
    c.execute(sql)
    payload = []
    content = {}
    for result in c.fetchall():
        content = {'artwork_id':result[0], 'accession_number': result[1], 'title': result[2], 'tombstone': result[3],'creator_id':result[4],'role':result[5],
                   'description': result[6],'department_id':result[7],'department_name':result[8]}
        payload.append(content)
        content = {}

   except Exception:
                    """ LOG the errors"""


   finally:
    c.close()
    con.close()
    write_file(payload,'cma_artworks.json')


def write_file(payload,fileName):
    data_json = json.dumps(payload)
    my_data_file = open(fileName, 'w')
    my_data_file.write(data_json)
    print(data_json)











