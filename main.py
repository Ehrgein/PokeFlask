from urllib import response
import requests
import json
import os
from flask.views import MethodView
from flask import Flask, render_template, request
from search import PokeSearch
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdwow123",
    database="pokedb"
    )



app = Flask(__name__, static_folder="static")


class HomePage(MethodView):


    @app.route("/", methods=["GET"])
    def basepage():

        return render_template('base.html')

    @app.route("/", methods=["GET", "POST"])
    def get():

            
            poke_form = request.form["name"]
            newpoke = poke_form
            retrieve_search = PokeSearch(newpoke)

            return render_template('pokedex.html',pokeform=poke_form.lower(),
            namepokemonbystr = retrieve_search.pokemon.capitalize(),
            namepokemonbyid=retrieve_search.pokename.capitalize(),
            pokeid = retrieve_search.pokeid,
            generation = retrieve_search.generation,
            pokehp=retrieve_search.hp,
            pokeatk = retrieve_search.attack,
            pokedef = retrieve_search.defense,
            pokespecialatk = retrieve_search.specialatk,
            pokespecialdef = retrieve_search.specialdef,
            pokespd = retrieve_search.speed,
            poketype = retrieve_search.types,
            poketypetwo = retrieve_search.typestwo,
            poketypelast = retrieve_search.typelast,
            pokestrong = retrieve_search.strong,
            pokeweak = retrieve_search.weak,
            pokeimmuneto = retrieve_search.nodamageto,
            pokeimmunefrom = retrieve_search.nodamagefrom,
            sprite = retrieve_search.sprite,
            pokebg = retrieve_search.bgcolour,
            pokeborder = retrieve_search.bordercolour,
            innerborder = retrieve_search.innerborder,
            twotypeborder = retrieve_search.typetwoborder,
            abilityone = retrieve_search.abilityone,
            abilitytwo = retrieve_search.abilitytwo,
            weakone = retrieve_search.weakone,
            weaktwo = retrieve_search.weaktwo,
            weakthree = retrieve_search.weakthree,
            )


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.run(debug=True)


    




