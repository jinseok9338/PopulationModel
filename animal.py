from random import choice, randint,getrandbits
from map import Map



class Animal:
    class_counter = 0
    def __init__(self,map):
        self.hunger = 0
        self.thirst = 0
        self.day = 0
        self.age = int(0/365)
        self.sex = bool(getrandbits(1))
        self.sexual_drive = 0
        self.map = map
        self.id = Animal.class_counter
        Animal.class_counter += 1

    def a_day_passes(self,animal_pos):
        self.day += 1
        self.thirst += 10
        self.hunger += 5
        if self.age >= 0.5 and self.sexual_drive < 100:
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



    def give_birth(self):
        pass


class Bunny(Animal):

    def __init__(self,map):
        Animal.__init__(self,map)
        self.bunny = "B"
        self.bunny_pos = (0, 0)
        self.bunny_object = {
            "Symbol" : "B",
            "Position" : self.bunny_pos,
            "Sex" : self.sex,
            "ID" : self.id,
            "Day": self.day,
            "Age": self.age,
            "Sexual_Drive": self.sexual_drive,
        }
        self.create_bunny()


    def create_bunny(self):
        random_num_x = randint(0, 9)
        random_num_y = randint(0, 9)
        if self.map[random_num_x][random_num_y] == "E":
            self.map[random_num_x][random_num_y] = self.bunny
            self.bunny_pos = (random_num_x,random_num_y)
            self.bunny_object["Position"] = self.bunny_pos
        else:
            self.create_bunny()

    def randomly_move(self):
        movable_tile_list =[]
        try:
            for a in range(-1,2):
                for b in range(-1,2):
                    if self.map[self.bunny_object["Position"][0]+a][self.bunny_object["Position"][1]+b] == "E":
                        new_pos_x = self.bunny_object["Position"][0]+a
                        new_pos_y = self.bunny_object["Position"][1]+b
                        if self.bunny_object["Position"][0]+a < 0:
                            new_pos_x += 10
                        if self.bunny_object["Position"][1] + b < 0:
                            new_pos_y += 10
                        movable_tile_list.append((new_pos_x,new_pos_y))
        except IndexError:
            pass
        if not movable_tile_list:
            movable_tile_pos = self.bunny_object["Position"]
        else:
            movable_tile_pos = choice(movable_tile_list)

        self.map[self.bunny_object["Position"][0]][self.bunny_object["Position"][1]] = "E"
        self.map[movable_tile_pos[0]][movable_tile_pos[1]] = self.bunny_object["Symbol"]
        self.bunny_object["Position"] = movable_tile_pos

    def bunny_move(self):

        if self.thirst >= 40:
            self.find_water()
        elif self.hunger >= 40:
            self.find_grass()
        elif self.sexual_drive >=80:
            self.find_opposite_sex()
        else:
            self.randomly_move(self.bunny_pos,self.bunny)



    def find_grass_and_eat(self,attempt =3):
        while attempt != 0:
            grass_pos_list = []
            for a in range(-1,2):
                for b in range(-1,2):
                    try:
                        if self.map[self.bunny_object["Position"][0] + a][self.bunny_object["Position"][1] + b] == "G":
                            new_pos_x = self.bunny_object["Position"][0] + a
                            new_pos_y = self.bunny_object["Position"][1] + b
                            if self.bunny_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.bunny_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            grass_pos_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
            if not grass_pos_list:
                self.randomly_move()
                print(self.bunny_object["Position"])
                attempt -=1
                self.find_grass_and_eat(attempt)
            else:
                grass_pos = choice(grass_pos_list)
                self.map[self.bunny_object["Position"][0]][self.bunny_object["Position"][1]] = "E"
                self.map[grass_pos[0]][grass_pos[1]] = self.bunny_object["Symbol"]
                self.bunny_object["Position"] = grass_pos
                print(self.bunny_object["Position"])

            break



    def find_water_and_drink(self,attempt = 3):
        while attempt != 0:
            water_pos_list = []
            for a in range(-1,2):
                for b in range(-1,2):
                    try:
                        if self.map[self.bunny_object["Position"][0] + a][self.bunny_object["Position"][1] + b] == "W":
                            new_pos_x = self.bunny_object["Position"][0] + a
                            new_pos_y = self.bunny_object["Position"][1] + b
                            if self.bunny_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.bunny_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            water_pos_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
            if not water_pos_list:
                self.randomly_move()
                print(self.bunny_object["Position"])
                attempt -=1
                self.find_water_and_drink(attempt)
            else:
                print(self.bunny_object["Position"])
            break




class Wolf(Animal):

    def __init__(self,map):
        Animal.__init__(self,map)
        self.wolf = "F"
        self.wolf_pos = (0, 0)
        self.wolf_object = {
            "Symbol" : "F",
            "Position" : self.wolf_pos,
            "Sex" : self.sex,
            "ID" : self.id,
            "Day": self.day,
            "Age": self.age,
            "Sexual_Drive": self.sexual_drive,
        }
        self.create_wolf()

    def create_wolf(self):
        random_num_x = randint(0, 9)
        random_num_y = randint(0, 9)
        if self.map[random_num_x][random_num_y] == "E":
            self.map[random_num_x][random_num_y] = self.wolf
            self.wolf_pos = (random_num_x,random_num_y)
            self.wolf_object["Position"] = self.wolf_pos
        else:
            self.create_wolf()


    def randomly_move(self):
        movable_tile_list =[]
        try:
            for a in range(-1,2):
                for b in range(-1,2):
                    if self.map[self.wolf_object["Position"][0]+a][self.wolf_object["Position"][1]+b] == "E":
                        new_pos_x = self.wolf_object["Position"][0]+a
                        new_pos_y = self.wolf_object["Position"][1]+b
                        if self.wolf_object["Position"][0]+a < 0:
                            new_pos_x += 10
                        if self.wolf_object["Position"][1] + b < 0:
                            new_pos_y += 10
                        movable_tile_list.append((new_pos_x,new_pos_y))
        except IndexError:
            pass
        if not movable_tile_list:
            movable_tile_pos = self.wolf_object["Position"]
        else:
            movable_tile_pos = choice(movable_tile_list)

        self.map[self.wolf_object["Position"][0]][self.wolf_object["Position"][1]] = "E"
        self.map[movable_tile_pos[0]][movable_tile_pos[1]] = self.wolf_object["Symbol"]
        self.wolf_object["Position"] = movable_tile_pos


    def find_bunny_and_eat(self,attempt =3):
        while attempt != 0:
            bunny_pos_list = []
            for a in range(-2,3):
                for b in range(-2,3):
                    try:
                        if self.map[self.wolf_object["Position"][0] + a][self.wolf_object["Position"][1] + b] == "G":
                            new_pos_x = self.wolf_object["Position"][0] + a
                            new_pos_y = self.wolf_object["Position"][1] + b
                            if self.wolf_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.wolf_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            bunny_pos_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
            if not bunny_pos_list:
                self.randomly_move()
                print(self.wolf_object["Position"])
                attempt -=1
                self.find_bunny_and_eat(attempt)
            else:
                bunny_pos = choice(bunny_pos_list)
                self.map[self.wolf_object["Position"][0]][self.wolf_object["Position"][1]] = "E"
                self.map[bunny_pos[0]][bunny_pos[1]] = self.wolf_object["Symbol"]
                self.wolf_object["Position"] = bunny_pos
                print(self.wolf_object["Position"])

            break

    def find_water_and_drink(self,attempt = 3):
        while attempt != 0:
            water_pos_list = []
            for a in range(-1,2):
                for b in range(-1,2):
                    try:
                        if self.map[self.wolf_object["Position"][0] + a][self.wolf_object["Position"][1] + b] == "W":
                            new_pos_x = self.wolf_object["Position"][0] + a
                            new_pos_y = self.wolf_object["Position"][1] + b
                            if self.wolf_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.wolf_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            water_pos_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
            if not water_pos_list:
                self.randomly_move()
                print(self.wolf_object["Position"])
                attempt -=1
                self.find_water_and_drink(attempt)
            else:
                print(self.wolf_object["Position"])
            break



    def wolf_move(self):

        if self.thirst >= 40:
            self.find_water()
        elif self.hunger >= 40:
            self.bunny()
        elif self.sexual_drive >= 80:
            self.find_opposite_sex()
        else:
            self.randomly_move(self.wolf_pos, self.wolf)


