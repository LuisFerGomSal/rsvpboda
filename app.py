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
        
    #dataset = ((1, 'luis', 0, 0, 0), (2, 'juan', 0, 0, 0), (3, 'Patricia Cecilia Alvarez Damian', 1, 0, 0), (4, 'Javier Israel Reynoso German', 2, 0, 0), (5, 'Hector Reynoso German', 2, 0, 0), (6, 'Roberto Benjamin Reynoso German', 2, 0, 0), (7, 'Jose Eduardo Reynoso German', 2, 0, 0), (8, 'Karina Reynoso German', 2, 0, 0), (9, 'Jose Luis Antonio Reynoso German', 2, 0, 0), (10, 'Eva Reynoso Huerta', 2, 0, 0), (11, 'Eduardo Vargas Reynoso', 2, 0, 0), (12, 'Sergio Vargas Reynoso', 2, 0, 0), (13, 'Artemio Miranda', 2, 0, 0), (14, 'Jorge Reynoso Huerta', 2, 0, 0), (15, 'Gloribel Echavarría', 2, 0, 0), (16, 'Esmeralda Reynoso', 1, 0, 0), (17, 'Araceli Juarez', 2, 0, 0), (18, 'Israel Reynoso', 2, 0, 0), (19, 'Raquel Reynoso Huerta', 1, 0, 0), (20, 'Arcelia Reynoso Valenzuela', 2, 0, 0), (21, 'Fernanda Reynoso Valenzuela', 2, 0, 0), (22, 'Angelica Reynoso Valenzuela', 2, 0, 0), (23, 'Lourdes Reynoso Valenzuela', 2, 0, 0), (24, 'Cesar Toledo Reynoso', 1, 0, 0), (25, 'Berenice Toledo Reynoso', 2, 0, 0), (26, 'Guillermo Toledo Reynoso', 2, 0, 0), (27, 'Brenda Benavides', 2, 0, 0), (28, 'Maribel Benavides', 2, 0, 0), (29, 'Patricia Benavides', 2, 0, 0), (30, 'Lorena Cervantes Limon', 2, 0, 0), (31, 'Alejandra Cervantes', 2, 0, 0), (32, 'Andrea Cervantes', 2, 0, 0), (33, 'Karina Limon Rios', 2, 0, 0), (34, 'Edna Limon Rios', 2, 0, 0), (35, 'Gustavo Limon Rios', 2, 0, 0), (36, 'Daniela Limon Rios', 2, 0, 0), (37, 'Fabricio Alonso Angulo Galindo', 1, 0, 0), (38, 'Luis Fernando Gomez', 1, 0, 0), (39, 'Angel Adrian Navarro', 1, 0, 0), (40, 'Miguel Angel Ortega Sanchez', 2, 0, 0), (41, 'Fernando Chavez Wong', 2, 0, 0), (42, 'Viridiana Mollinedo Quihuis', 2, 0, 0), (43, 'Jalil Gallegos', 2, 0, 0), (44, 'Alejandra Ortiz', 1, 0, 0), (45, 'Laura Ortiz', 1, 0, 0), (46, 'Maria Guadalupe Gonzalez', 1, 0, 0), (47, 'Melissa Ortiz', 1, 0, 0), (48, 'Paulina Ortiz', 1, 0, 0), (49, 'Amber Cabrales', 1, 0, 0), (50, 'Carlos Ayala', 2, 0, 0), (51, 'Alan Ayala', 1, 0, 0))

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
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cursor.execute("INSERT INTO guests(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cursor.close()
        return 'success'   

    return render_template("home.html",
                           guestId=guestId,
                           guest=guest,
                           guestName=guestName,
                           aditionalGuests=aditionalGuests,
                           confirmed=confirmed,
                           totalGoing=totalGoing)



if __name__ == "__main__":
    app.run(debug=True)