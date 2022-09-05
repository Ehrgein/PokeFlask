from urllib import response
import requests
import json
import os
from flask.views import MethodView
from flask import Flask, render_template, request
from search import PokeSearch
import mysql.connector
from datetime import datetime




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
            firstcolour = retrieve_search.colourone,
            secondcolour = retrieve_search.colourtwo,
            twotypecolour = retrieve_search.typetwocolour,
            abilityone = retrieve_search.abilityone,
            abilitytwo = retrieve_search.abilitytwo,
            weakone = retrieve_search.weakone,
            weaktwo = retrieve_search.weaktwo,
            emptyskill = retrieve_search.sameskill,
            weakthird = retrieve_search.weakthree,
            evolvefirstform = retrieve_search.firstform,
            evolvesecondform = retrieve_search.secondform,
            evolvelastform= retrieve_search.lastform,
            evolvefourthform = retrieve_search.fourthform, 
            spriteevoone = retrieve_search.spriteevoone,
            spriteevotwo = retrieve_search.spriteevotwo,
            spriteevothree = retrieve_search.spriteevothree,
            spriteevofour = retrieve_search.spritefourthform,
            noevolve = retrieve_search.noevolve,
            newspeciesid = retrieve_search.newspeciesid,
            newname = retrieve_search.newname.capitalize(),
            secondsideevo = retrieve_search.secondside,
            secondevosprite = retrieve_search.getsecondevosprite,
            allspecieslist = retrieve_search.allspeciesdata,
            listofevolvl = retrieve_search.listofevolvl,
            firsttrigger = retrieve_search.firsttrigger,
            secondtrigger = retrieve_search.secondtrigger,
            thirdtrigger = retrieve_search.thirdtrigger,
            firsttriggervalue = retrieve_search.firsttriggervalue,
            secondtriggervalue = retrieve_search.secondtriggervalue,
            tradeitems = retrieve_search.gettradeitems,
            getspecies = retrieve_search.getspecies,
            sideevocheck = retrieve_search.sideevocheck,
            ifbranch = retrieve_search.twobranchfirst,
            twobranchspriteone = retrieve_search.twobranchspriteone,
            twobranchspritetwo = retrieve_search.twobranchspritetwo,
            twobranchtrigger = retrieve_search.twobranchtrigger,
            twobranchtriggervalue = retrieve_search.twobranchtriggervalue
            )


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.run(debug=True)


    




