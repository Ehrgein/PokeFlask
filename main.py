from urllib import response
import requests
import json
import os
from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, validators
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

    @app.route("/", methods=["GET","POST"])
    def get():



        poke_form = request.form["nm"]
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
        poketype = retrieve_search.types.capitalize(),
        pokestrong = retrieve_search.strong,
        pokeweak = retrieve_search.weak,
        pokeimmuneto = retrieve_search.nodamageto,
        pokeimmunefrom = retrieve_search.nodamagefrom,
        sprite = retrieve_search.sprite,
        )

    def save_pokemon():
        print("pepe")

   


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.add_url_rule('/caught', view_func=HomePage.as_view('catch_em_all'))

app.run(debug=True)


    




