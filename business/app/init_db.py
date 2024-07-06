import psycopg2
psycopg2
conn = psycopg2.connect(database="conecction",host="localhost",user="postgres", password="popy9714",port="5432")

cur= conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS oficina_ventas (zona_ventas integer null, suma_ventas integer null,id serial PRIMARY KEY, nombre varchar (50) , fecha_ing date , zona varchar (30), total_ventas integer, comisiones integer  ) ''')

cur.execute(''' INSERT INTO oficina_ventas (nombre,fecha_ing,zona,total_ventas,comisiones) VALUES ('Juan','2022/12/31','este',50000,9000), ('Oscar','2015/09/21','oeste',90000,18000),('Carlos','2020/06/15','norte',70000,12000)''')

conn.commit()
cur.close()
conn.close()