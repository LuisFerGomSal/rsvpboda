from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

# CONFIG DB
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'guests1234'
app.config['MYSQL_DB'] = 'guests'

guests = [{'id':1,'name':'Luis', 'guests':3},
          {'id':2,'name':'Jose', 'guests':0},
          {'id':3,'name':'Juan', 'guests':1}]

@app.route("/")
def home():
    try:
        guestId = int(request.args.get('guestId'))
    except TypeError:
        guestId = 0

    confirmed = 0
    return render_template("home.html", guests = guests, guestId = guestId, confirmed = confirmed)



if __name__ == "__main__":
    app.run(debug=True)