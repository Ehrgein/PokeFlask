import types
from urllib import response
import requests
import json
import os
from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, validators
from search import PokeSearch

app = Flask(__name__)


class PokeForm(Form):
    style={'style': 'font-size: 12px'}
    searchresult = StringField("Search for a pokemon: ", default="ditto")

class HomePage(MethodView):

    @app.route("/", methods=["GET", "POST"])
    def get():
        poke_form = PokeForm(request.form)
        newpoke = poke_form.searchresult.data
        retrieve_search = PokeSearch(newpoke)

        print(newpoke)
        return render_template('index.html',pokeform=poke_form,
        pokename=newpoke.capitalize(),
        pokehp=retrieve_search.hp,
        pokeatk = retrieve_search.attack,
        pokedef = retrieve_search.defense,
        pokespecialatk = retrieve_search.specialatk,
        pokespecialdef = retrieve_search.specialdef,
        pokespd = retrieve_search.speed,
        poketype = retrieve_search.types,
        pokestrong = retrieve_search.strong,
        pokeweak = retrieve_search.weak,
        pokeimmuneto = retrieve_search.nodamageto,
        pokeimmunefrom = retrieve_search.nodamagefrom,
        sprite = retrieve_search.sprite 
        )

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))


app.run(debug=True)


    




