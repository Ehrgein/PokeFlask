from urllib import response
import requests
import json
import os


class PokeSearch: 

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    type_url = "https://pokeapi.co/api/v2/type/"

    def __init__(self, pokemon):
            self.pokemon = pokemon.lower()
            content = self.__get_pokemon()
            self.pokeid = content['game_indices'][-1]['game_index']
            self.pokename = content['forms'][0]['name']
            self.generation = self.__getgeneration()
            self.hp = content['stats'][0]['base_stat']
            self.attack = content['stats'][1]['base_stat']
            self.defense = content['stats'][2]['base_stat']
            self.specialatk = content['stats'][3]['base_stat']
            self.specialdef = content['stats'][4]['base_stat']
            self.speed = content['stats'][5]['base_stat']   
            self.types = content['types'][0]['type']['name']
            self.sprite = content['sprites']['front_default']
            self.strong = self.__strong()
            self.weak = self.__weak()
            self.nodamageto = self.__nodamageto()
            self.nodamagefrom = self.__nodamagefrom()

    def __get_pokemon(self):

            response = requests.get(self.base_url + self.pokemon)
            content = response.json()
            return content


    def __getgeneration(self):

        gens = ['First', 'Second', 'Third', 'Fourth',
        'Fifth']
        if 1 <= self.pokeid  <= 151:
            return gens[0]
        elif 152 <= self.pokeid <= 251:
            return gens[1]
        elif 252 <= self.pokeid <= 386:
            return gens[2]
        elif 387 <= self.pokeid <= 493:
            return gens[3]
        elif 494 <= self.pokeid <= 649:
            return gens[4]


    def __strong(self):        
        #type_req = open("./weakstrong.json", encoding="utf-8")

        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        strongdata = datatype['damage_relations']['double_damage_to']

        strong = []
        strongclean = ""
        for element in (strongdata):
            strong.append(element['name'])
            strongclean = ' , '.join([str(item)for item in strong])
        return strongclean 

    def __nodamageto(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        strongdata = datatype['damage_relations']['no_damage_to']

        nodamageto= []
        for element in (strongdata):
                nodamageto.append(element['name'])
                nodamagetoclean = ' , '.join([str(item)for item in nodamageto])
                return nodamagetoclean
        else: 
            if nodamageto==[]:
                return " - "

    def __nodamagefrom(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        strongdata = datatype['damage_relations']['no_damage_from']

        nodamagefrom = []
        nodamagefromclean = ""
        for element in (strongdata):
                nodamagefrom.append(element['name'])
                nodamagefromclean = ' , '.join([str(item)for item in nodamagefrom])
                return nodamagefromclean     
        else: 
            if nodamagefrom==[]:
                return " - "


    def __weak(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_from']

        weak = []
        for element in (weakdata):
            weak.append(element['name'])
            weakclean= ' , '.join([str(item)for item in weak])
        return weakclean





