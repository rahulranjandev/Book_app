from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import dbHost, dbuser, dbpasswd, dbport, db

app = Flask(__name__)

# Config Sql
mydb = mysql.connector.connect(host=dbHost, user=dbuser, password=dbpasswd, port=dbport, database=db)

mycursor = mydb.cursor()


# Redirect Home Page
@app.route("/")
def index():
    return redirect(url_for("list_book"))


# Favicon Icon
@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"))


# Books List
@app.route("/list_book", methods=["GET", "POST"])
def list_book():
    current_page = request.args.get("page_no")

    sql = ""
    limit = 5
    offset = 0

    if current_page is None:
        current_page = 1
        offset = 0
        sql = "SELECT * FROM books_list LIMIT %s, %s "

    else:
        current_page = int(current_page)
        offset = (current_page - 1) * limit

        sql = "SELECT * FROM books_list LIMIT %s, %s "

    val = (offset, limit)
    # mycursor.execute(sql)
    mycursor.execute(sql, val)

    # mycursor.execute("SELECT * FROM books_list")

    myresult = mycursor.fetchall()

    return render_template("/list_book.html", data=myresult, current_page=current_page)


# Low to High
@app.route("/high_low", methods=["GET", "POST"])
def high_low():
    mycursor.execute("SELECT * FROM books_list ORDER BY book_price DESC")

    myresult = mycursor.fetchall()

    return render_template("/list_book.html", data=myresult)


# Add Book
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book_name = request.form.get("Book_name")
        author_name = request.form.get("Author_name")
        book_pages = request.form.get("Book_pages")
        book_price = request.form.get("Book_price")

        sql = "INSERT INTO books_list (book_name, author_name, book_pages, book_price) VALUES (%s, %s, %s, %s)"
        val = (book_name, author_name, book_pages, book_price)

        mycursor.execute(sql, val)

        mydb.commit()

        return redirect(url_for("list_book"))

    return render_template("/add_book.html")


# Edit
@app.route("/edit_book/<id>", methods=["GET", "POST"])
def edit_book(id):
    if request.method == "POST":
        book_name = request.form.get("Book_name")
        author_name = request.form.get("Author_name")
        book_pages = request.form.get("Book_pages")
        book_price = request.form.get("Book_price")

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

        return render_template("/edit_book.html", book=read)


# Delete
@app.route("/delete_book/<id>", methods=["POST"])
def delete_book(id):
    if request.method == "POST":
        sql = "DELETE FROM books_list WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        mydb.commit()

        return redirect(url_for("list_book"))


# Search
@app.route("/search")
def search():
    cast = request.args.get("search")

    mycursor.execute("SELECT * FROM books_list WHERE Book_name LIKE CONCAT('%', %s, '%')", (cast,))

    print(mycursor.statement)

    myresult = mycursor.fetchall()

    return render_template("/list_book.html", data=myresult)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
