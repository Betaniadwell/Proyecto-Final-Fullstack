import psycopg2
psycopg2
conn = psycopg2.connect(database="conecction",host="localhost",user="postgres", password="popy9714",port="5432")

cur= conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS oficina_ventas (zona_ventas integer null , suma_ventas integer null,suma_comisiones integer null, id serial PRIMARY KEY, nombre varchar (50) , fecha_ing date , zona varchar (30), total_ventas integer, comisiones integer  ) ''')

cur.execute(''' INSERT INTO oficina_ventas (nombre,fecha_ing,zona,total_ventas,comisiones) VALUES ('Juan','2022/12/31','este',50000,9000), ('Oscar','2015/09/21','oeste',90000,18000),('Carlos','2020/06/15','norte',70000,12000),('Jorge','2024/02/28','sur',1200000,6500), ('Francisco','2024/09/21','sur',190000,18000),('Roque','2024/06/15','oeste',70000,12000),('Sergio','2021/12/31','este',80000,5500), ('Mario','2015/09/21','este',85000,9500),('Osvaldo','2020/06/15','norte',70000,12000)''')

conn.commit()
cur.close()
conn.close()