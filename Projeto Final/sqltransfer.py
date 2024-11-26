import json
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Marcelo123!',
    'database': 'book_shop'
}

json_file_path = 'xddd.json'

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

insert_query = """
    INSERT INTO advices(id,quote_text)
    VALUES(%s, %s)
"""

try:
    with open(json_file_path,'r',encoding="utf-8") as file:
        quotes = json.load(file)

    for quote in quotes:
        quote_text = quote.get('advice')
        id = quote.get('id')

        cursor.execute(insert_query,(id,quote_text))
    
    connection.commit()
    print(f"Inserted {cursor.rowcount} quotes into the database: {db_config['database']}.")

except Exception as e:
    print(f"An error has occurred: {e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()