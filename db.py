import mysql.connector
from datetime import datetime
import requests
import search

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdwow123",
    database="pokedb"
    )


mycursor = db.cursor()




#mycursor.execute("CREATE TABLE ownedpokemon (pokedexid smallint PRIMARY KEY, name VARCHAR(15), type VARCHAR(12), generation VARCHAR(15))")

#mycursor.execute("INSERT INTO Person(name, age) VALUES (%s, %s)", ("tim", 19))
#db.commit()

#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)", ("ADAM", datetime.now(), "M"))
#db.commit()

        #poke_form = PokeForm(request.form)
        #newpoke = poke_form.searchresult.data
        #retrieve_search = PokeSearch(newpoke)
#   mycursor = db.cursor()
        #mycursor.execute("INSERT INTO ownedpokemon(pokedexid, name, type, generation) VALUES (%s, %s,  %s, %s)", (retrieve_search.pokeid, retrieve_search.pokemon, retrieve_search.types, retrieve_search.generation)) """
    #return render_template('collect.html') """