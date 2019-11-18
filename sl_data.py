import sqlite3

#Connection variables
db = sqlite3.connect('main.sqlite')
cursor = db.cursor()

#Creating database if not present when bot starts
def setup_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main(
    channel_id TEXT,
    author_id TEXT,
    message TEXT
    )
    ''')

#Update user search history
def update_history(message,query):
    cursor.execute('''INSERT INTO main VALUES(?,?,?)''',(str(message.channel),str(message.author),str(query)))
    db.commit()

#Fetch recent terms searched by user
def show_history(message,search_term):
    cursor.execute(''' Select message from main where channel_id = ? and author_id = ? and message like ?''',(str(message.channel),str(message.author),'%'+search_term+'%'))
    result= cursor.fetchall()
    return result
