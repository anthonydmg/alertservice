import psycopg2


def insertDataAlerDb(temperatura_maxima, latitud, longitud, distancia, area_region_incendiada):
    conn = psycopg2.connect(database="fireDetection",
                    host="127.0.0.1",
                    user="postgres",
                    password="admin",
                    port="5432")
    try:
        cursor = conn.cursor()
        postgres_insert_query = """ INSERT INTO fire_detection (temperatura_maxima, latitud, longitud, distancia , area_region_incendiada) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (temperatura_maxima, latitud, longitud, distancia, area_region_incendiada)
        cursor.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into fireDetection table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into fireDetection table", error)

    finally:
        # closing database conn.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")