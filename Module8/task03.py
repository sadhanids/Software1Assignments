import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password ='DL123*',
    autocommit = True
)
ICAO1 = input("Enter ICAO code of 1st airport: ").upper()
ICAO2 = input("Enter ICAO code of 2nd airport: ").upper()

def airport_code():
    sql = f"SELECT gps_code,name,latitude_deg,longitude_deg FROM airport WHERE gps_code IN ('{ICAO1}', '{ICAO2}')";
    cursor = connection.cursor()
    cursor.execute(sql)
    database_data = cursor.fetchall()

    if len(database_data) == 2:
        coordinates = []
        for data in database_data:
            gps_code, name, lat, lon = data
            print(f"{gps_code} - {name}: ({lat}, {lon})")
            coordinates.append((lat, lon))

        distance_km = geodesic(coordinates[0], coordinates[1]).kilometers
        print(f"Distance Between Two Airports: {distance_km:.2f} km")
    else:
        print("Invalid ICAO code.")

airport_code()
