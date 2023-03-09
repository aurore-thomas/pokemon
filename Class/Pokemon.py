from Class.Settings import *
# from Buttons import Button

class Pokemon:
    def __init__(self, name, level):
        self.__name = name
        self.__maxHP = 100
        self.defense = 0
        self.level = level

        with open("Json/Complete_Pokedex.json", "r", encoding='utf-8') as file:
            self.pokedex = json.load(file)

        self.get_data()
        self.calcul_stats()
        self.get_sprite()
        self.get_moves()

    def get_data(self):
        for i in range(1, len(self.pokedex)+1):
            if str(self.get_name()) == str(self.pokedex[str(i)]["name"]["french"]) or str(self.get_name()) == str(self.pokedex[str(i)]["name"]["english"]):
                self.id = self.pokedex[str(i)]["id"]
                self.type = self.pokedex[str(i)]["type"]
                self.base_hp = self.pokedex[str(i)]["base"]["HP"]
                self.attack = self.pokedex[str(i)]["base"]["Attack"]
                self.defense = self.pokedex[str(i)]["base"]["Defense"]
                self.sp_attack = self.pokedex[str(i)]["base"]["Sp. Attack"]
                self.sp_defense = self.pokedex[str(i)]["base"]["Sp. Defense"]
                self.speed = self.pokedex[str(i)]["base"]["Speed"]
                self.__set_pv(int(self.pokedex[str(i)]["base"]["HP"]))
                break

    # We use IV=31 and EV=0 (neutral) to calculate stat, and a neutral status(= 1)
    def calcul_stats(self):
        self.attack = ((2 * self.attack + 31) * self.level/ 100) + 5
        self.defense = ((2 * self.defense + 31) * self.level/ 100) + 5
        self.sp_attack = ((2 * self.sp_attack + 31) * self.level/ 100) + 5
        self.sp_defense = ((2 * self.sp_defense + 31) * self.level/ 100) + 5
        self.speed = ((2 * self.speed + 31) * self.level/ 100) + 5
        hp = ((2 * int(self.get_hp()) + 31) * self.level/ 100) + self.level + 5
        self.modify_pv(hp)

    def get_sprite(self):
        self.front_sprite = pg.image.load("Pictures/Sprites_Pokemon/front/" + str(self.id) + ".png")
        self.back_sprite = pg.image.load("Pictures/Sprites_Pokemon/back/" + str(self.id) + ".png")

    def get_moves(self):
        with open("Json/pokemon_moves.json", "r", encoding='utf-8') as file:
            self.all_moves = json.load(file)
        self.moves = self.all_moves[str(self.id)]
       
    def get_name(self):
        return self.__name
    
    def get_hp(self):
        return self.__maxHP
    
    def modify_pv(self, new_pv):
        return self.__set_pv(new_pv)

    def __set_pv(self, new_pv):
        self.__maxHP = new_pv

    def display(self):
        print(self.attack)
        print(self.defense)
        print(self.moves)

p1 = Pokemon("Florizarre", 100)
p1.display()



# with open("Json/Complete_Pokedex.json", "r", encoding='utf-8') as file:
#     POKEDEX = json.load(file)

# def get_pokemon_data(id,language):
#     return {
#         'id':POKEDEX[str(id)]['id'],
#         'name':POKEDEX[str(id)]['name'][language],
#         'type':POKEDEX[str(id)]['type'],
#         'stats':POKEDEX[str(id)]['base']

#     }

# print(get_pokemon_data(150,'french'))