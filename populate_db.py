import mysql.connector
from config import dbHost, dbuser, dbpasswd, dbport, db

mydb = mysql.connector.connect(host=dbHost, user=dbuser, password=dbpasswd, port=dbport, database=db)

mycursor = mydb.cursor()

sql = "INSERT INTO books_list (book_name, author_name, book_pages, book_price) VALUES (%s, %s, %s, %s)"

val = [
    ("The Alchemist", "Paulo Coelho", 208, 10.0),
    ("The Great Gatsby", "F. Scott Fitzgerald", 180, 15.0),
    ("Man's Search for Meaning", "Viktor Frankl", 165, 12.0),
    ("The Kite Runner", "Khaled Hosseini", 371, 20.0),
    ("To Kill a Mockingbird", "Harper Lee", 281, 18.0),
    ("The Catcher in the Rye", "J.D. Salinger", 214, 14.0),
    ("The Hobbit", "J.R.R. Tolkien", 310, 25.0),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1178, 30.0),
    ("The Da Vinci Code", "Dan Brown", 689, 22.0),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223, 16.0),
    ("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 251, 17.0),
    ("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 317, 19.0),
    ("Harry Potter and the Goblet of Fire", "J.K. Rowling", 636, 21.0),
    ("Harry Potter and the Order of the Phoenix", "J.K. Rowling", 766, 23.0),
    ("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 607, 24.0),
    ("Harry Potter and the Deathly Hallows", "J.K. Rowling", 607, 24.0),
    ("The Hunger Games", "Suzanne Collins", 374, 20.0),
    ("Catching Fire", "Suzanne Collins", 391, 21.0),
    ("Mockingjay", "Suzanne Collins", 390, 21.0),
    ("Angels & Demons", "Dan Brown", 713, 23.0),
    ("Inferno", "Dan Brown", 611, 22.0),
    ("The Lost Symbol", "Dan Brown", 509, 21.0),
    ("Origin", "Dan Brown", 632, 24.0),
    ("Digital Fortress", "Dan Brown", 510, 21.0),
    ("Deception Point", "Dan Brown", 556, 22.0),
    ("Divergent", "Veronica Roth", 487, 20.0),
    ("Insurgent", "Veronica Roth", 525, 21.0),
    ("Allegiant", "Veronica Roth", 526, 21.0),
    ("Four", "Veronica Roth", 285, 18.0),
    ("The Maze Runner", "James Dashner", 371, 20.0),
    ("The Scorch Trials", "James Dashner", 360, 20.0),
    ("The Death Cure", "James Dashner", 324, 19.0),
    ("The Kill Order", "James Dashner", 327, 19.0),
    ("The Fever Code", "James Dashner", 370, 20.0),
    ("The Giver", "Lois Lowry", 180, 15.0),
    ("Gathering Blue", "Lois Lowry", 215, 16.0),
    ("Messenger", "Lois Lowry", 169, 14.0),
    ("Son", "Lois Lowry", 393, 20.0),
    ("The Outsiders", "S.E. Hinton", 192, 16.0),
    ("That Was Then, This Is Now", "S.E. Hinton", 159, 14.0),
    ("Rumble Fish", "S.E. Hinton", 144, 13.0),
    ("Tex", "S.E. Hinton", 198, 16.0),
    ("Taming the Star Runner", "S.E. Hinton", 224, 18.0),
    ("The Last Book in the Universe", "Rodman Philbrick", 223, 16.0),
    ("Freak the Mighty", "Rodman Philbrick", 169, 14.0),
    ("Max the Mighty", "Rodman Philbrick", 169, 14.0),
    ("The Young and the Restless", "Rodman Philbrick", 169, 14.0),
    ("The House of the Scorpion", "Nancy Farmer", 380, 20.0),
    ("The Lord of Opium", "Nancy Farmer", 411, 21.0),
    ("The Ear, the Eye, and the Arm", "Nancy Farmer", 311, 19.0)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mydb.close()