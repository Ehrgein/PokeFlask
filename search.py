
from types import NoneType
import types
from urllib import response
import requests
import json
import os


class PokeSearch: 

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    type_url = "https://pokeapi.co/api/v2/type/"
    species_url = "https://pokeapi.co/api/v2/pokemon-species/"

    def __init__(self, pokemon):
        try:
            self.pokemon = pokemon.lower()
            content = self.__get_pokemon()
            self.newspeciesid = self.__newid()
            self.newname = self.__newname()
            self.speciesfind = 'species'
            self.triggerevo = 'trigger'
            self.levelgen= 'min_level'
            self.helditem = 'held_item'
            self.useitem = 'item'
            self.evodetails = 'evolution_details'
            self.evochaindata = self.__getevochain()
            self.evochainjson = self.__evochainjson()
            self.triggergenerator = self.__triggergenerator(self.evochainjson, self.triggerevo)
            self.allspeciesdata= self.__evo_generator(self.evochainjson, self.speciesfind)
            self.listofevolvl = self.__getlevels()
            self.listofitems = self.__getitems()
            self.gettradeitems = self.__gettrade()
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
            self.evochaindata = self.__getevochain()
            self.evochainjson = self.__evochainjson()
            self.sameskill = self.__checksameksill()
            self.strong = self.__strong()
            self.weak = self.__weak()
            self.nodamageto = self.__nodamageto()
            self.nodamagefrom = self.__nodamagefrom()
            self.colourone = self.__firstcolour()
            self.colourtwo = self.__secondcolour()
            self.colourthree = self.__thirdcolour()
            self.typetwocolour = self.__typetwoborder()
            self.weakone = self.__doubledamagetoone()
            self.weaktwo = self.__doubledamagetotwo()   
            self.weakthree = self.__doubledamagetothree()
            self.firstform = self.__firstform()
            self.secondform = self.__secondform()
            self.lastform = self.__lastform()
            self.fourthform = self.__fourthform()
            self.spriteevoone = self.__spriteevoone()
            self.spriteevotwo = self.__spriteevotwo()
            self.spriteevothree = self.__spriteevothree()
            self.spritefourthform = self.__spriteevofour()
            self.noevolve = self.__noevolve()
            self.secondside = self.__secondside()
            self.getsecondevosprite = self.__getsideevosprite()
            self.listofevolvl = self.__getlevels()
            self.listofitems = self.__getitems()
            self.gettradeitems = self.__gettrade()
            self.getspecies = self.__getspecies()
            self.firsttrigger = self.__getfirsttrigger()
            self.secondtrigger = self.__getsecondtrigger()
            self.thirdtrigger = self.__getthirdtrigger()
            self.firsttriggervalue = self.__firsttriggervalue()
            self.secondtriggervalue = self.__secondtriggervalue()
            self.sideevocheck = self.__getevolen()
            self.twobranchfirst = self.__ifbase2branchgetfirst()
            self.twobranchsecond = self.__ifbase2branchgetsecond()
            self.twobranchspriteone = self.__twobranchgetspriteone()
            self.twobranchspritetwo = self.__twobranchgetspritetwo()
            self.twobranchtrigger = self.__basetwobranchtrigger()
            self.twobranchtriggervalue = self.__branchtriggervalue()


        except AttributeError:
            pass

    def __newid(self):

        response = requests.get(self.species_url + self.pokemon)
        species = response.json()
        intid = int(species['id'])
        return intid

    def __newname(self):
        response = requests.get(self.species_url + self.pokemon)
        species = response.json()
        return species['name']

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

    def __getevochain(self):

        response = requests.get(self.species_url + str(self.newspeciesid))
        evochaindata = response.json()
        return evochaindata

    def __evochainjson(self):

        response = requests.get(self.species_url + str(self.newspeciesid))
        evochaindata = response.json()
        geturl = evochaindata['evolution_chain']['url']
        evochainjson = requests.get(geturl)
        evochainjsonclean = evochainjson.json()    
        return evochainjsonclean
    
    def __firstform(self):
        
        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlist = []

        if self.evochainjson['chain']['evolves_to'] == []:
            return " This pokemon does not evolve "
        else:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1

            return newlist[-1]

    def __secondform(self):

        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlist = []

        evolen = len(self.evochainjson['chain']['evolves_to'])


        if evolen == 2:
            return ""
        elif self.evochainjson['chain']['evolves_to'] == []:
            return ""

        elif length == 1:
            return ""

        elif length == 2:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
            return newlist[-2]
            
        elif length == 3:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
            return newlist[-2]
        elif length == 4:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
            return newlist[-2]

    def __lastform(self):

        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlist = []

        evolen = len(self.evochainjson['chain']['evolves_to'])

        if self.evochainjson['chain']['evolves_to'] == []:
            return ""
        if evolen == 2:
            return ""
        elif length < 2:
            return ""
        elif length == 3:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
            return newlist[-3]
        elif length == 4:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
            return newlist[-4]

    def __fourthform(self):

        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlst = []

        if length == 4:
            return lst[1]['name']
        else:
            return ""
    
    def __strong(self):        

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

        if len(datatype['damage_relations']['double_damage_to'])== 0:
            return ""
        else:
            return datatype['damage_relations']['double_damage_to'][0]['name']

    def __doubledamagetotwo(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()


        if len(datatype['damage_relations']['double_damage_to']) < 2 :
            return ""
        else:
            return datatype['damage_relations']['double_damage_to'][1]['name']
    
    def __doubledamagetothree(self):
        response = requests.get(self.type_url + self.types)
        datatype = response.json()

        try:
            return datatype['damage_relations']['double_damage_to'][2]['name']
        except IndexError:
            return ""

    def __weak(self):
        
        response = requests.get(self.type_url + self.types)
        datatype = response.json()
        weakdata = datatype['damage_relations']['double_damage_from']

        weak = []
        for element in (weakdata):
            weak.append(element['name'])
            weakclean= ' , '.join([str(item)for item in weak])
        return weakclean

    def __firstcolour(self):
        
        innercolour = {'normal': '#a0a0a0',
        'dragon' : '#3c64c8',
        'water' : '#0094e5',
        'fire' : '#ff3700',
        'ground' : '#cca142',
        'rock' : '#a07850',
        'electric' : '#e4b700',
        'fairy': '#ff7eb8',
        'fighting': '#D67873',
        'flying' : '#79bcd7',
        'ghost' : '#705898',
        'grass' : '#36d10a',
        'ice' : '#00b7ee',
        'poison' : '#be78be',
        'psychic' : '#dc78c8',
        'steel' : '#B8B8D0',
        'dark' : '#646464',
        'bug' : '#32b432',
        }


        for key, value in innercolour.items():
            if self.types in key:
                return value

    def __secondcolour(self):
        
        innerborders = {'normal' : '#dcdcdc',
        'water': '#14b9ff',
        'ice':'#14f5ff',
        'ghost' : '#A292BC',
        'fire' : '#ff6900',
        'ground' : '#fac85a',
        'rock' : '#b48c64',
        'electric' : '#ffe100',
        'fairy' : '#ffafdc',
        'grass' : '#1ce700',
        'dragon' : '#5078dc',
        'fighting' : '#D67873',
        'flying' : '#78dcff',
        'poison' : '#d28cd2',
        'psychic' : '#f08cdc',
        'steel' : '#ab9fa8',
        'dark' : '#A29288',
        'bug' : '#46c846',
        }

        for key, value in innerborders.items():
            if self.types in key:
                return value

    def __thirdcolour(self):


        thirdcolour = {'normal': '#A8A878',
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


        for key, value in thirdcolour.items():
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
        'steel' : '#7a7a8b',
        'dark' : '#705848',
        'bug' : '#C6D16E',
        }

        for key, value in backgroundtwo.items():
            if self.typestwo in key:
                return value

    def __checksameksill(self):

        emptyability = ""
        if self.abilityone == self.abilitytwo:
            return emptyability
        else:
            return self.abilitytwo

    def __spriteevoone(self):

        if self.firstform is None:
            return ""
        elif self.firstform == "":
            return "" 
        try:
            response = requests.get(self.species_url + str(self.firstform))
            content = response.json()
            idspriteone = content['id']
            spritebyidone = requests.get(self.base_url + str(idspriteone))
            spritebyidoneread = spritebyidone.json()
            return spritebyidoneread['sprites']['other']['official-artwork']['front_default']
        except:
            return ""

    def __spriteevotwo(self):

        if self.secondform is None:
            return ""
        elif self.secondform == "":
            return "" 
        else:
            response = requests.get(self.species_url + str(self.secondform))
            content = response.json()
            idspritetwo = content['id']
            spritebyidtwo = requests.get(self.base_url + str(idspritetwo))
            spritebyidtworead = spritebyidtwo.json()

            return spritebyidtworead['sprites']['other']['official-artwork']['front_default']

    def __spriteevothree(self):

        try:
            if self.lastform == "":
                return ""
            else: 
                response = requests.get(self.species_url + str(self.lastform))
                content = response.json()
                idspritethree = content['id']
                spritebyidthree = requests.get(self.base_url + str(idspritethree))
                spritebyidthreread = spritebyidthree.json()
                return spritebyidthreread['sprites']['other']['official-artwork']['front_default']
        except json.JSONDecodeError:
            return ""
    
    #def __noevolve(self):

        newevochain= self.evochaindata['evolution_chain']['url']
        getnoevolve = requests.get(newevochain)
        getnoevolveempty = getnoevolve.json()

        
        if getnoevolveempty['chain']['evolves_to'] == []:
            return "this pokemon does not evolve"
        else:
            return ""

    def __spriteevofour(self):

        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlst = []

        if length == 4:
            response = requests.get(self.species_url + str(self.fourthform))
            content = response.json()
            idspriteside = content['id']
            spritebyidside = requests.get(self.base_url + str(idspriteside))
            spritebyidsideread = spritebyidside.json()
            return spritebyidsideread['sprites']['other']['official-artwork']['front_default']
        else: 
            return ""
        
    def __noevolve(self):

        checknoevolve = self.evochainjson
        noevolvedata = checknoevolve['chain']['evolves_to']

        if noevolvedata == []:
            return "This pokemon doesn't have a known evolution"
    
    def __secondside(self):

        evodata= self.evochaindata['evolution_chain']['url']
        allevo = requests.get(evodata)
        allevodata = allevo.json()

        if allevodata['chain']['evolves_to'] == []:
            return  ""
        else:
            try:
                return allevodata['chain']['evolves_to'][0]['evolves_to'][1]['species']['name']
            except IndexError:
                return ""

    def __getsideevosprite(self):

        if self.secondside == "":
             return ""
        else: 
            response = requests.get(self.species_url + str(self.secondside))
            content = response.json()
            idspritesidetwo = content['id']
            spritebyidsidetwo = requests.get(self.base_url + str(idspritesidetwo))
            spritebyidsidereadtwo = spritebyidsidetwo.json()
            return spritebyidsidereadtwo['sprites']['other']['official-artwork']['front_default']      

    def __evo_generator(self, json, key):


        if isinstance(json, dict):
            for k, v in json.items():
                if k == key:
                    yield v
                else:
                    yield from self.__evo_generator(v, key)
        elif isinstance(json, list):
            for item in json:
                yield from self.__evo_generator(item, key)
                    
    def __triggergenerator(self, json, key):

        if isinstance(json, dict):
            for k, v in json.items():
                if k == key:
                    yield v
                else:
                    yield from self.__evo_generator(v, key)
        elif isinstance(json, list):
            for item in json:
                yield from self.__evo_generator(item, key)
                    
    def __getthirdtrigger(self):
   
        lst = list(self.__evo_generator(self.evochainjson, self.triggerevo))
        length = len(lst)
        newlist = []

        try:
            if self.evochainjson['chain']['evolves_to'] == []:
                return ""
            elif length == 3:
                i = 0
                while (i < length):
                    newlist.append(lst[i]['name'])
                    i = i + 1
                if len(newlist) == 3:
                    if newlist[-1] == 'level-up':
                        levellist = "Level +"
                        return levellist
                    elif newlist[-1] == 'trade':
                        tradelist = 'Trade'
                        return tradelist
                    elif newlist[-1] == 'use-item':
                        useitem = 'Use '
                        return useitem
                    else:
                        return ""
            else:
                return ""
        except IndexError:
            return ""
    
    def __getfirsttrigger(self):

        lst = list(self.__evo_generator(self.evochainjson, self.triggerevo))
        length = len(lst)
        newlist = []


        if self.evochainjson['chain']['evolves_to'] == []:
            return ""
        elif newlist == []:
            i = 0
            while (i < length):
                newlist.append(lst[i]['name'])
                i = i + 1
                if newlist[0] == 'level-up':
                    levellist = "Level +"
                    return levellist
                elif newlist[0] == 'trade':
                    tradelist = 'Trade'
                    return tradelist
                elif newlist[0] == 'use-item':
                    useitem = 'Use '
                    return useitem
                else:
                    return ""
            
    def __getsecondtrigger(self):

        lst = list(self.__evo_generator(self.evochainjson, self.triggerevo))
        length = len(lst)
        newlist = []
        evolen = len(self.evochainjson['chain']['evolves_to'])

        try:
            if self.evochainjson['chain']['evolves_to'] == []:
                return ""
            elif evolen == 2:
                return ""

            else:
                i = 0
                while (i < length):
                    newlist.append(lst[i]['name'])
                    i = i + 1
                if newlist[1] == 'level-up':
                    levellist = "Level +"
                    return levellist
                elif newlist[1] == 'trade':
                    tradelist = 'Trade'
                    return tradelist
                elif newlist[1] == 'use-item':
                    useitem = 'Use '
                    return useitem

            return newlist[1]
        except IndexError:
            return ""

    def __getevolen(self):

        checkforsideevo = len(self.evochainjson['chain']['evolves_to'])
        return checkforsideevo

    def __getlevels(self):

        lst = list(self.__evo_generator(self.evochainjson, self.levelgen))
        length = len(lst)
        newlst = []

        for val in lst:
            if val != None:
                newlst.append(val)
        return newlst
        
    def __getitems(self):

        lst = list(self.__evo_generator(self.evochainjson, self.useitem))
        length = len(lst)
        newlst = []

        for val in lst:
            if val != None:
                newlst.append(val)
        return newlst

    def __gettrade(self):
        
        lst = list(self.__evo_generator(self.evochainjson, self.helditem))
        length = len(lst)
        newlst = []

        for val in lst:
            if val != None:
                newlst.append(val)
        return newlst
    
    def __getspecies(self):
        
        lst = list(self.__evo_generator(self.evochainjson, self.speciesfind))
        length = len(lst)
        newlst = []

        for val in lst:
            if val != None:
                newlst.append(val)
        return newlst

    def __firsttriggervalue(self):

        evolen = len(self.evochainjson['chain']['evolves_to'])

        try: 
            if self.firsttrigger == 'Level +':
                return self.listofevolvl[0]
            elif self.firsttrigger == 'Use ':
                newitem = str(self.listofitems[0]['name'])
                return newitem.replace('-', ' ').title()
            elif self.firsttrigger == 'Trade':
                newitem = str(self.gettradeitems[0]['name'])
                return newitem.replace('-', ' ').title()
            else:
                if self.firsttrigger == "":
                    return ""
        except IndexError:
            return ""

    def __secondtriggervalue(self):

        evolen = len(self.evochainjson['chain']['evolves_to'])
        if evolen == 2:
            return ""
        if self.secondtrigger == 'Level +':
            return str(self.listofevolvl[1])
        elif self.secondtrigger == 'Use ':
            newitem = str(self.listofitems[0]['name'])
            newitem2 = newitem.replace('-', ' ').title()
            if newitem2 == self.firsttriggervalue:
                return ""
            else:
                return newitem.replace('-', ' ').title()
        elif self.secondtrigger == 'Trade':
            try: 
                newitem = str(self.gettradeitems[0]['name'])
                return newitem.replace('-', ' ').title()
            except IndexError:
                return ""
        else: 
            return ""
    
    def __ifbase2branchgetfirst(self):

        evolen = len(self.evochainjson['chain']['evolves_to'])
        if evolen == 2:
            return self.evochainjson['chain']['evolves_to'][0]['species']['name']

    def __ifbase2branchgetsecond(self):
        evolen = len(self.evochainjson['chain']['evolves_to'])
        if evolen == 2:
            return self.evochainjson['chain']['evolves_to'][1]['species']['name']

    def __twobranchgetspriteone(self):

        if self.firstform is None:
            return ""
        elif self.firstform == "":
            return "" 
        try:
            response = requests.get(self.species_url + str(self.twobranchfirst))
            content = response.json()
            idspriteone = content['id']
            spritebyidone = requests.get(self.base_url + str(idspriteone))
            spritebyidoneread = spritebyidone.json()
            return spritebyidoneread['sprites']['other']['official-artwork']['front_default']
        except:
            return ""
    
    def __twobranchgetspritetwo(self):

        if self.firstform is None:
            return ""
        elif self.firstform == "":
            return "" 
        try:
            response = requests.get(self.species_url + str(self.twobranchsecond))
            content = response.json()
            idspriteone = content['id']
            spritebyidone = requests.get(self.base_url + str(idspriteone))
            spritebyidoneread = spritebyidone.json()
            return spritebyidoneread['sprites']['other']['official-artwork']['front_default']
        except:
            return ""

    def __basetwobranchtrigger(self):

        lst = list(self.__evo_generator(self.evochainjson, self.triggerevo))
        length = len(lst)
        newlist = []
        evolen = len(self.evochainjson['chain']['evolves_to'])

        if evolen == 2:
            try:
                if self.evochainjson['chain']['evolves_to'] == []:
                    return ""
                else:
                    i = 0
                    while (i < length):
                        newlist.append(lst[i]['name'])
                        i = i + 1
                    if newlist[-1] == 'level-up':
                        levellist = "Level +"
                        return levellist
                    elif newlist[-1] == 'trade':
                        tradelist = 'Trade'
                        return tradelist
                    elif newlist[-1] == 'use-item':
                        useitem = 'Use '
                        return useitem
            except IndexError:
                return ""
        else:
            return ""
        
    def __branchtriggervalue(self):

        evolen = len(self.evochainjson['chain']['evolves_to'])

        if evolen != 2:
            return ""
        if self.twobranchtrigger == 'Level +':
            return str(self.listofevolvl[-1])
        elif self.twobranchtrigger == 'Use ':
            newitem = str(self.listofitems[-1]['name'])
            newitem2 = newitem.replace('-', ' ').title()
            return newitem2.replace('-', ' ').title()
        elif self.twobranchtrigger == 'Trade':
            try: 
                newitem = str(self.gettradeitems[0]['name'])
                return newitem.replace('-', ' ').title()
            except IndexError:
                return ""
        else: 
            return ""


