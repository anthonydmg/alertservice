import psycopg2

conn = psycopg2.connect(database="fireDection",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")