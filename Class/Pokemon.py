from Class.Settings import *
from Class.Buttons import Button

class Pokemon:
    def __init__(self, name, level):
        self.__name = name
        self.level = level
        self.id = 0
        self.type = []
        self.__pv = 100
        self.atk = 0
        self.defense = 10
        self.sp_atk = 0
        self.sp_def = 0
        self.speed = 0
        
        # We use the API to calculate the stats :
        # response = requests.get(f'{url_api}/pokemon/{str(self.get_name())}')
        # self.json = response.json()

        with open("../Json/Complete_Pokedex.json", "r") as file:
            self.data = json.load(file)

        for id in range(0, len(file)):
            if str(self.get_name()) == file[id]["name"]["french"] or file[id]["name"]["english"]:
                self.type = file[id]["type"]

    def get_name(self):
        return self.__name
    
    def get_pv(self, new_pv):
        return self.set_pv(new_pv)

    def __set_pv(self, new_pv):
        self.__pv = new_pv