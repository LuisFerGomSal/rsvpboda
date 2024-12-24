from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import sys



app = Flask(__name__)

# CONFIG DB
app.config['MYSQL_HOST'] = 'luisxd.mysql.pythonanywhere-services.com' 
app.config['MYSQL_USER'] = 'luisxd'
app.config['MYSQL_PASSWORD'] = 'luis8888'
app.config['MYSQL_DB'] = 'guests'

mysql = MySQL(app)



guests = [{'id':1,'name':'Luis', 'guests':3},
          {'id':2,'name':'Jose', 'guests':0},
          {'id':3,'name':'Juan', 'guests':1}]

@app.route("/")
def home():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM guests")
    data = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    
    try:
        guestId = int(request.args.get('guestId'))
    except TypeError:
        guestId = 0

    confirmed = 0
    return render_template("home.html", guests = guests, guestId = guestId, confirmed = confirmed, data=data)



if __name__ == "__main__":
    app.run(debug=True)