from random import choice
from map import Map

map = Map()

class Animal:

    def __init__(self):
        self.hunger = 0
        self.thirst = 0
        self.day = 0
        self.age = int(0/365)
        self.sex = bool(random.getrandbits(1))
        self.sexual_drive = 0
        self.map = Map()

    def randomly_move(self,animal_pos,animal):
        movable_tile_list =[]
        try:
            for a in range(-2,3):
                for b in range(-2,3):
                    if map[a][b] == "E":
                        movable_tile_list.append((a,b))
        except IndexError:
            pass
        if not movable_tile_list:
            movable_tile_pos = anima_pos
        else:
            movable_tile_pos = choice(movable_tile_list)

        self.map[animal_pos[0]][animal_pos[1]] = "E"
        self.map[movable_tile_pos[0]][movable_tile_pos[1]] = animal

    def a_day_passes(self,animal_pos):
        self.day += 1
        self.thirst += 10
        self.hunger += 5
        if self.age >= 1 and self.sexual_drive < 100:
            self.sexual_drive += 1
        if self.thirst >= 100:
            self.map[animal_pos[0]][animal_pos[1]] = "E"
            del self
        elif self.hunger >= 100:
            self.map[animal_pos[0]][animal_pos[1]] = "E"
            del self
        elif self.age >= 2.5:
            self.map[animal_pos[0]][animal_pos[1]] = "E"
            del self

    def find_water(self):
        pass

    def find_opposite_sex(self):
        pass



class Bunny(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.bunny = "B"
        self.bunny_pos = (0, 0)
        self.create_bunny()


    def create_bunny(self):
        random_num_x = randint(0, 9)
        random_num_y = randint(0, 9)
        if self.map[random_num_x][random_num_x] == "E":
            self.map[random_num_x][random_num_x] = self.bunny
            self.bunny_pos = (random_num_x,random_num_y)
        else:
            self.create_bunny()

    def bunny_move(self):

        if self.thirst >= 40:
            self.find_water()
        elif self.hunger >= 40:
            self.find_grass()
        elif self.sexual_drive >=80:
            self.find_opposite_sex()
        else:
            self.randomly_move(self.bunny_pos,self.bunny)



    def find_grass(self):
        pass







class Wolf(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.wolf = "W"
        self.wolf_pos = (0, 0)
        self.create_wolf()

    def create_wolf(self):
        random_num_x = randint(0, 9)
        random_num_y = randint(0, 9)
        if self.map[random_num_x][random_num_x] == "E":
            self.map[random_num_x][random_num_x] = self.wolf
            self.wolf_pos = (random_num_x,random_num_y)
        else:
            self.create_wolf()

    def find_bunny(self):
        pass

    def wolf_move(self):

        if self.thirst >= 40:
            self.find_water()
        elif self.hunger >= 40:
            self.bunny()
        elif self.sexual_drive >= 80:
            self.find_opposite_sex()
        else:
            self.randomly_move(self.wolf_pos, self.wolf)









