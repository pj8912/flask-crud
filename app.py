from flask import Flask , render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__) #flask app
load_dotenv() #load env



DBNAME = os.environ.get("DB_NAME")
PWD = os.environ.get("DB_PWD")
USERNAME = os.environ.get("DB_USERNAME")
HOST = os.environ.get("DB_HOST")

cnx = mysql.connector.connect(user=USERNAME, password=PWD, host=HOST, database=DBNAME)
cursor = cnx.cursor()



@app.route("/product/create")
def create():
    return render_template('create.html')


@app.route("/product/createnew", methods=['POST'])
def create_new():
    title = request.form['title']
    short_notes = request.form['shortnotes']
    price = request.form['price']
    cursor.execute("INSERT INTO products(title,short_notes,price) VALUES(%s, %s, %s)", (title, short_notes, price))
    return redirect("/")

@app.route("/product/edit/<int:id>")
def edit(id):
    #select based on id
    #cursor.execute("SELECT * FROM products WHERE id=?",(id,))
    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    row = cursor.fetchone()
    return render_template('edit.html', product=row)


@app.route("/product/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    return redirect("/")

#update
@app.route("/product/updateProduct", methods=['POST'])
def update():
    id = request.form['id']
    title = request.form['title']
    short_notes = request.form['shortnotes']
    price = request.form['price']
    cursor.execute("UPDATE products SET title=%s, short_notes=%s, price=%s WHERE id=%s", (title, short_notes, price, id))
    return redirect('/')




#home
@app.route('/')
def home():    
    #fetch 'products'
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows)



if __name__ == '__main__':
    app.run(debug=True)






