from urllib import response
import requests
import json
import os


class PokeSearch: 

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    type_url = "https://pokeapi.co/api/v2/type/"

    def __init__(self, pokemon):
            self.pokemon = pokemon
            content = self.__get_pokemon()
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






