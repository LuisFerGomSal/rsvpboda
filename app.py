from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# CONFIG DB
app.config['MYSQL_HOST'] = 'luisxd.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'luisxd'
app.config['MYSQL_PASSWORD'] = 'luis8888'
app.config['MYSQL_DB'] = 'luisxd$guests'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def home():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM guests")
    dataset = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()

    try:
        guestId = int(request.args.get('guestId'))
    except TypeError:
        guestId = 0

    guest = 0
    guestId = guestId
    guest=guest
    guestName=''
    aditionalGuests=0
    confirmed=0
    totalGoing=0


    for data in dataset:
        if data[0] == guestId:
            guest = data
            guestName=guest[1]
            aditionalGuests=guest[2] - 1
            confirmed=guest[3]
            totalGoing=guest[4]

    if guestName == '' : guestId = 0

    if request.method == "POST":
        cursor = mysql.connection.cursor()
        cursor.execute(""" UPDATE guests SET confirmed = 1 WHERE guest_id = %s """, (guestId,))
        mysql.connection.commit()
        cursor.close()
        return render_template("home.html",
                           guestId=guestId,
                           guest=guest,
                           guestName=guestName,
                           aditionalGuests=aditionalGuests,
                           confirmed=1,
                           totalGoing=totalGoing)

    return render_template("home.html",
                           guestId=guestId,
                           guest=guest,
                           guestName=guestName,
                           aditionalGuests=aditionalGuests,
                           confirmed=confirmed,
                           totalGoing=totalGoing)


@app.route("/admin")
def admin():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM guests")
    guests = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()

    confirmedGuests = 0

    for guest in guests:
        if guest[3] == 1:
            confirmedGuests += 1

    return render_template("admin.html", guests=guests, confirmedGuests=confirmedGuests)


if __name__ == "__main__":
    app.run(debug=True)