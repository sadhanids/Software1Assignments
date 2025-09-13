import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='DL123*',
    autocommit=True
)

def search_for_country(area_code):
    sql = f"SELECT type, COUNT(*) AS airport_count FROM airport WHERE iso_country = 'FI' GROUP BY type ORDER BY type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_data = cursor.fetchall()
    if len(database_data) > 0:
        for data in database_data:
            print(f" Airport Type: {data[0]}")
            print(f" Airport Count: {data[1]}")


user_input = input("Enter iso_country code: ")
search_for_country(user_input)