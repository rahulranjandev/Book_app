from flask import Flask, render_template, request, redirect, url_for
from flask.wrappers import Request
import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="20.228.144.187",
    user="root",
    password="Passwd@123r",
    port=3306,
    database="bookapp"
)

print(mydb)
mycursor = mydb.cursor()


@app.route("/")
def index():
    return redirect(url_for('list_book'))

# Books List


@app.route("/list_book", methods=['GET', 'POST'])
def list_book():
    mycursor.execute("SELECT * FROM books_list")

    myresult = mycursor.fetchall()

    # print(myresult[0])

    return render_template("/list_book.html", data=myresult)


@app.route("/high_low", methods=['GET', 'POST'])
def high_low():
    mycursor.execute("SELECT * FROM books_list ORDER BY book_price DESC")

    myresult = mycursor.fetchall()

    print(myresult[0])

    return render_template("/list_book.html", data=myresult)


@app.route("/add_book", methods=['GET', 'POST'])
def add_book():
    if request.method == "POST":
        book_name = request.form.get('Book_name')
        author_name = request.form.get('Author_name')
        book_pages = request.form.get('Book_pages')
        book_price = request.form.get('Book_price')

        print(book_name)
        print(author_name)
        print(book_pages)
        print(book_price)

        sql = "INSERT INTO books_list (book_name, author_name, book_pages, book_price) VALUES (%s, %s, %s, %s)"
        val = (book_name, author_name, book_pages, book_price)

        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        return redirect(url_for('list_book'))

    return render_template("/add_book.html")


@app.route("/edit_book/<id>", methods=['GET', 'POST'])
def edit_book(id):
    pass
    print(id)
    if request.method == "POST":
        book_name = request.form.get('Book_name')
        author_name = request.form.get('Author_name')
        book_pages = request.form.get('Book_pages')
        book_price = request.form.get('Book_price')

        sql = "UPDATE books_list SET book_name = %s, author_name = %s, book_pages= %s, book_price=%s WHERE id = %s"

        val = (book_name, author_name, book_pages, book_price, id)

        mycursor.execute(sql, val)

        mydb.commit()

        return redirect(url_for("list_book"))

    else:
        sql = "SELECT * FROM books_list WHERE id= %s"
        val = (id,)
        mycursor.execute(sql, val)
        read = mycursor.fetchone()
        print(read)
        return render_template("/edit_book.html", book=read)


@app.route("/delete_book/<id>", methods=['POST'])
def delete_book(id):
    if request.method == "POST":
        sql = "DELETE FROM books_list WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for("list_book"))


if __name__ == '__main__':
    app.run(debug=True)
