import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='DohaLife12*',
    autocommit=True
)

def search_for_airports(icao):
    sql = f"select name, municipality from airport where ident = '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_data =cursor.fetchall()
    if len(database_data) > 0:
        for data in database_data:
            print(f" Airport Name: {data[0]}")
            print(f" Airport City: {data[1]}")

user_input =input("Enter ICAO code: ")
search_for_airports(user_input)