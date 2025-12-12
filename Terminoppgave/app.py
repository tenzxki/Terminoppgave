from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html', title ="Min nettside")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect(host="10.200.14.26",user="talhaa",password="Fotball2008",database="spillanmeldelse")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        existing_user = mycursor.fetchone()

        if existing_user:
            mycursor.close()
            mydb.close()
            return render_template("register.html", error="Username already taken!")
        
        mycursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        mydb.commit()
        mycursor.close()
        mydb.close()

        return redirect("/login")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect(host="10.200.14.26", user="talhaa", password="Fotball2008",database="spillanmeldelse")
        mycursor = mydb.cursor()
        mycursor.execute( "SELECT id, password FROM users WHERE username = %s", (username,))
        user = mycursor.fetchone()

        mycursor.close()
        mydb.close()

        if not user:
            return render_template("login.html", error="User does not exist!")

        user_id, stored_password = user

        if password != stored_password:
            return render_template("login.html", error="Incorrect password!")

        return redirect("/home")  

    return render_template("login.html")

@app.route("/home")
def home():
    mydb = mysql.connector.connect(host="10.200.14.26", user="talhaa", password="Fotball2008", database="spillanmeldelse")
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("""
        SELECT 
            g.id,
            g.name,
            g.description,
            g.genre,
            g.developer,
            g.release_year,
            g.cover_url,
            AVG(r.rating) AS avg_rating
        FROM games g
        LEFT JOIN reviews r ON g.id = r.game_id
        GROUP BY g.id, g.name, g.description, g.genre, g.developer, g.release_year, g.cover_url;
    """)

    games = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return render_template("home.html", games=games)



@app.route("/addgame", methods=["GET", "POST"])
def addgame():

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        genre = request.form["genre"]
        developer = request.form["developer"]
        release_year = request.form["release_year"]
        cover_url = request.form["cover_url"]
        mydb = mysql.connector.connect( host="10.200.14.26", user="talhaa", password="Fotball2008", database="spillanmeldelse" )
        mycursor = mydb.cursor()
        mycursor.execute(
            "INSERT INTO games (name, description, genre, developer, release_year, cover_url) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, description, genre, developer, release_year, cover_url)
        )

        mydb.commit()
        mycursor.close()
        mydb.close()

        return redirect("/home")

    return render_template("addgame.html")

@app.route("/game/<int:game_id>", methods=["GET", "POST"])
def game_detail(game_id):
    mydb = mysql.connector.connect(host="10.200.14.26", user="talhaa", password="Fotball2008", database="spillanmeldelse")
    mycursor = mydb.cursor(dictionary=True)
    if request.method == "POST":
        username = request.form["username"]
        rating = request.form["rating"]
        comment = request.form["comment"]
        mycursor.execute(
            "INSERT INTO reviews (game_id, username, rating, comment) VALUES (%s, %s, %s, %s)",
            (game_id, username, rating, comment)
        )
        mydb.commit()
        return redirect(f"/game/{game_id}")

    mycursor.execute("SELECT * FROM games WHERE id = %s", (game_id,))
    game = mycursor.fetchone()

    mycursor.execute("SELECT * FROM reviews WHERE game_id = %s ORDER BY id DESC", (game_id,))
    reviews = mycursor.fetchall()

    mycursor.execute("SELECT AVG(rating) AS avg_rating FROM reviews WHERE game_id = %s", (game_id,))
    avg_rating = mycursor.fetchone()["avg_rating"]

    mycursor.close()
    mydb.close()

    return render_template("review.html", game=game, reviews=reviews, avg_rating=avg_rating)
