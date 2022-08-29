from inspect import Attribute
from types import NoneType
from urllib import response
import requests
import json
import os


class PokeSearch: 

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    type_url = "https://pokeapi.co/api/v2/type/"

    def __init__(self, pokemon):
        try:
            self.pokemon = pokemon.lower()
            content = self.__get_pokemon()
            self.pokeid = content['game_indices'][-1]['game_index']
            self.pokename = content['name']
            self.generation = self.__getgeneration()
            self.hp = content['stats'][0]['base_stat']
            self.attack = content['stats'][1]['base_stat']
            self.defense = content['stats'][2]['base_stat']
            self.specialatk = content['stats'][3]['base_stat']
            self.specialdef = content['stats'][4]['base_stat']
            self.speed = content['stats'][5]['base_stat']   
            self.types = content['types'][0]['type']['name']
            self.typelast = content['types'][-1]['type']['name']
            self.typestwo = self.__typetwo()
            self.sprite = content['sprites']['other']['official-artwork']['front_default']
            self.abilityone = content['abilities'][0]['ability']['name']
            self.abilitytwo = content['abilities'][-1]['ability']['name']
            self.strong = self.__strong()
            self.weak = self.__weak()
            self.nodamageto = self.__nodamageto()
            self.nodamagefrom = self.__nodamagefrom()
            self.bgcolour = self.__backgroundtype()
            self.bordercolour = self.__bordertype()
            self.innerborder = self.__innerborder()
            self.typetwoborder = self.__typetwoborder()
            self.weakone = self.__doubledamagetoone()
            self.weaktwo = self.__doubledamagetotwo()
            self.weakthree = self.__doubledamagetothree()


        except AttributeError:
            pass

    def __typetwo(self):

        response = requests.get(self.base_url + self.pokemon)
        content = response.json()
        contentlast = content['types'][-1]['type']['name']
        
        value = ""
        if self.typelast == self.types:
            return value 
        else:
            return contentlast

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
    
    def __doubledamagetoone(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_to'][0]['name']
        return weakdata

    def __doubledamagetotwo(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_to'][1]['name']
        return weakdata
    
    def __doubledamagetothree(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_to'][-1]['name']
        return weakdata

    def __weak(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_from']

        weak = []
        for element in (weakdata):
            weak.append(element['name'])
            weakclean= ' , '.join([str(item)for item in weak])
        return weakclean

    def __backgroundtype(self):
        
        innercolour = {'normal': '#A8A878',
        'dragon' : '#7038F8',
        'water' : '#6890f0',
        'fire' : '#F08030',
        'ground' : '#B8A038',
        'rock' : '#E0C068',
        'electric' : '#F8D030',
        'fairy': '#EE99AC',
        'fighting': '#D67873',
        'flying' : '#A8A878',
        'ghost' : '#705898',
        'grass' : '#A7DB8D',
        'ice' : '#BCE6E6',
        'poison' : '#A040A0',
        'psychic' : '#F85888',
        'steel' : '#B8B8D0',
        'dark' : '#705848',
        'bug' : '#C6D16E',
        }


        for key, value in innercolour.items():
            if self.types in key:
                return value

    def __bordertype(self):
                
                
        colourborders= {'normal': '#6D6D4E;',
        'dragon': '#A890F0;',
        'water': '#445E9C',
        'fire': '#EB5353',
        'ground': '#E0C068',
        'rock': '#E0C068',
        'electric': '#A1871F',
        'fairy': '#9B6470',
        'fighting': '#7D1F1A',
        'flying': '#A890F0',
        'ghost' : '#682A68',
        'grass' : '#A040A0',
        'ice' : '#A890F0',
        'poison' : '#682A68',
        'psychic' : '#A13959',
        'steel' : '#E0C068',
        'dark' : '#49392F',
        'bug' : '#6D7815',
        }

          
        for key, value in colourborders.items():
            if self.types in key:
                return value

    def __innerborder(self):
        
        innerborders = {'normal' : '#C6C6A7',
        'water': '#9db7f5',
        'ice':'#98D8D8',
        'ghost' : '#A292BC',
        'fire' : '#F5AC78',
        'ground' : '#D1C17D',
        'rock' : '#D1C17D',
        'electric' : '#FAE078',
        'fairy' : '#F4BDC9',
        'grass' : '#A7DB8D',
        'dragon' : '#A27DFA',
        'fighting' : '#D67873',
        'flying' : '#C6C6A7',
        'poison' : '#C183C1',
        'psychic' : '#FA92B2',
        'steel' : '#1D1E0',
        'dark' : '#A29288',
        'bug' : '#C6D16E',
        }

        for key, value in innerborders.items():
            if self.types in key:
                return value

    def __typetwoborder(self):

        backgroundtwo = {'normal': '#A8A878',
        'dragon' : '#7038F8',
        'water' : '#6890f0',
        'fire' : '#F08030',
        'ground' : '#B8A038',
        'rock' : '#E0C068',
        'electric' : '#F8D030',
        'fairy': '#EE99AC',
        'fighting': '#D67873',
        'flying' : '#A8A878',
        'ghost' : '#705898',
        'grass' : '#A7DB8D',
        'ice' : '#BCE6E6',
        'poison' : '#A040A0',
        'psychic' : '#F85888',
        'steel' : '#D1D1E0',
        'dark' : '#705848',
        'bug' : '#C6D16E',
        }

        for key, value in backgroundtwo.items():
            if self.typestwo in key:
                return value


