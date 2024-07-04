import psycopg2

from flask import Flask,render_template, request,redirect,url_for

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="conecction",host="localhost",user="postgres", password="popy9714",port="5432")
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cur= conn.cursor()
    cur.execute ('''SELECT * FROM oficina_ventas order by Id''')
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template ('index.html',data=data)



@app.route('/create',methods=['POST'])
def create():
    conn=db_conn()
    cur = conn.cursor()
    nombre=request.form['nombre']
    fecha_ing=request.form['fecha_ing']
    zona=request.form['zona']
    total_ventas=request.form['total_ventas']
    comisiones=request.form['comisiones']
    cur.execute('''INSERT INTO  oficina_ventas (nombre,fecha_ing,zona,total_ventas,comisiones) VALUES(%s,%s,%s,%s,%s)''',(nombre,fecha_ing,zona,total_ventas,comisiones))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update',methods=['POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()
    nombre=request.form['nombre']
    fecha_ing=request.form['fecha_ing']
    zona=request.form['zona']
    total_ventas=request.form['total_ventas']
    comisiones=request.form['comisiones']
    id=request.form['id']
    cur.execute(
        '''UPDATE oficina_ventas SET nombre=%s, fecha_ing=%s, zona=%s, total_ventas=%s,comisiones=%s WHERE id=%s ''',(nombre,fecha_ing,zona,total_ventas,comisiones,id))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete',methods=['POST'])
def delete():
    conn=db_conn()
    cur=conn.cursor()
    id=request.form['id']
    cur.execute('''DELETE FROM oficina_ventas WHERE id=%s''',(id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/query',methods=['POST'])
def query():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        ''' select * from oficina_ventas where fecha_ing > ('2024-01-01') ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query1',methods=['POST'])
def query1():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''SELECT * FROM oficina_ventas ORDER BY zona,nombre''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query2',methods=['POST'])
def query2():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''SELECT * FROM oficina_ventas  WHERE comisiones  > 10000 ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query3',methods=['POST'])
def query3():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''select * from oficina_ventas where zona = 'este' ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query4',methods=['POST'])
def query4():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''select * from oficina_ventas where zona ='oeste' ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)


@app.route('/query5',methods=['POST'])
def query5():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
         '''select * from oficina_ventas where zona = 'norte' ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query6',methods=['POST'])
def query6():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
         '''select * from oficina_ventas where zona = 'sur' ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query7',methods=['POST'])
def query7():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''SELECT * FROM oficina_ventas WHERE total_ventas > 100000 ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)

@app.route('/query8',methods=['POST'])
def query8():
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(
        '''SELECT nombre, max(total_ventas) as ventas_netas FROM oficina_ventas group by nombre ''')
    data=cur.fetchall()
    conn.commit()
    return render_template ('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)



