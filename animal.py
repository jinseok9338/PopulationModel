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
        self.pregnant = False
        self.conceived_period =0
        Animal.class_counter += 1 # class counter increments when the object is added


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
            "Pregnant":self.pregnant,
            "Conceived_Period":self.conceived_period,
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

    def a_day_passes(self):
        self.bunny_object["Day"] += 1
        if self.bunny_object["Day"]%365 == 0:
            self.bunny_object["Age"] += 1
        self.bunny_object["Thirst"] += 10
        self.bunny_object["Hunger"] += 5
        if self.bunny_object["Age"] >= 1 and self.bunny_object["Sexual_Drive"] < 100:
            self.bunny_object["Sexual_Drive"] += 1
        if self.bunny_object["Pregnant"] == True:
            self.bunny_object["Conceived_Period"] +=1
            if self.bunny_object["Conceived_Period"] == 100:
                self.reproduce()
        if self.bunny_object["Thirst"] >= 100:
            self.map[self.bunny_object["Position"][0]][self.bunny_object["Position"][1]] = "E"
            del self
        elif self.hunger >= 100:
            self.map[self.bunny_object["Position"][0]][self.bunny_object["Position"][1]] = "E"
            del self
        elif self.age >= 3:
            self.map[self.bunny_object["Position"][0]][self.bunny_object["Position"][1]] = "E"
            del self

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

        if self.bunny_object["Thirst"] >= 40:
            self.find_water_and_drink()
        elif self.bunny_object["hunger"] >= 40:
            self.find_grass_and_eat()
        elif self.bunny_object["Sexual_Drive"] >=80:
            self.find_mate_and_mate()
        else:
            self.randomly_move()
        self.a_day_passes()


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
                self.bunny_object["Hunger"] =0
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
                self.bunny_object["Thirst"] =0
            break


    def find_mate_and_mate(self,attempt =3,bunny_list = None):
        while attempt != 0:
            opposite_sex_list = []
            opposite_sex_list_final = []
            for a in range(-1,2):
                for b in range(-1,2):
                    try:
                        if self.map[self.bunny_object["Position"][0] + a][self.bunny_object["Position"][1] + b] == "B":
                            new_pos_x = self.bunny_object["Position"][0] + a
                            new_pos_y = self.bunny_object["Position"][1] + b
                            if self.bunny_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.bunny_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            opposite_sex_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
                    for bunny in bunny_list:
                        for opposite_sex_pos in opposite_sex_list:
                            if bunny.bunny_object["Position"] == opposite_sex_pos and bunny.bunny_object["Sex"] != self.bunny_object["Sex"]:
                                opposite_sex_list_final.append(opposite_sex_pos)

            if not opposite_sex_list_final:
                self.randomly_move()
                print(self.bunny_object["Position"])
                attempt -=1
                self.find_mate_and_mate(attempt)
            else:
                print(self.bunny_object["Position"])
                self.bunny_object["Sexual_drive"] =0
                if self.bunny_object["Sex"] == False:
                    self.bunny_object["Pregnant"] = True
            break



    def reproduce(self):
        self.create_bunny()
        self.create_bunny()
        self.bunny_object["Pregnant"] = False
        self.bunny_object["Conceived_Period"] = 0



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
            "Pregnant":self.pregnant,
            "Conceived_Period":self.conceived_period,
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


    def find_bunny_and_eat(self,attempt =3,bunny_list = None): # I need to delete bunny object.
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
                for bunny in bunny_list:
                    if bunny.bunny_object["Position"] == bunny_pos:
                        del bunny
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

    def a_day_passes(self):
        self.wolf_object["Day"] += 1
        if self.wolf_object["Day"]%365 == 0:
            self.wolf_object["Age"] += 1
        self.wolf_object["Thirst"] += 10
        self.wolf_object["Hunger"] += 5
        if self.wolf_object["Age"] >= 1 and self.wolf_object["Sexual_Drive"] < 100:
            self.wolf_object["Sexual_Drive"] += 1
        if self.wolf_object["Pregnant"]:
            self.wolf_object["Conceived_Period"] +=1
            if self.wolf_object["Conceived_Period"] == 100:
                self.reproduce()
        if self.wolf_object["Thirst"] >= 100:
            self.map[self.wolf_object["Position"][0]][self.wolf_object["Position"][1]] = "E"
            del self
        elif self.hunger >= 100:
            self.map[self.wolf_object["Position"][0]][self.wolf_object["Position"][1]] = "E"
            del self
        elif self.age >= 3:
            self.map[self.wolf_object["Position"][0]][self.wolf_object["Position"][1]] = "E"
            del self

    def reproduce(self):
        self.create_wolf()
        self.create_wolf()
        self.wolf_object["Pregnant"] = False
        self.wolf_object["Conceived_Period"] = 0

    def find_mate_and_mate(self,attempt =3,wolf_list = None):
        while attempt != 0:
            opposite_sex_list = []
            opposite_sex_list_final = []
            for a in range(-1,2):
                for b in range(-1,2):
                    try:
                        if self.map[self.wolf_object["Position"][0] + a][self.wolf_object["Position"][1] + b] == "F":
                            new_pos_x = self.wolf_object["Position"][0] + a
                            new_pos_y = self.wolf_object["Position"][1] + b
                            if self.wolf_object["Position"][0] + a < 0:
                                new_pos_x += 10
                            if self.wolf_object["Position"][1] + b < 0:
                                new_pos_y += 10
                            opposite_sex_list.append((new_pos_x, new_pos_y))
                    except IndexError:
                        pass
                    for wolf in wolf_list:
                        for opposite_sex_pos in opposite_sex_list:
                            if wolf.wolf_object["Position"] == opposite_sex_pos and wolf.wolf_object["Sex"] != self.wolf_object["Sex"]:
                                opposite_sex_list_final.append(opposite_sex_pos)

            if not opposite_sex_list_final:
                self.randomly_move()
                print(self.wolf_object["Position"])
                attempt -=1
                self.find_mate_and_mate(attempt)
            else:
                print(self.wolf_object["Position"])
                self.wolf_object["Sexual_drive"] =0
                if self.wolf_object["Sex"] == False:
                    self.wolf_object["Pregnant"] = True
            break

    def wolf_move(self):
        if self.wolf_object["Thirst"] >= 40:
            self.find_water_and_drink()
        elif self.wolf_object["hunger"] >= 40:
            self.find_bunny_and_eat()
        elif self.wolf_object["Sexual_Drive"] >=80:
            self.find_mate_and_mate()
        else:
            self.randomly_move()
        self.a_day_passes()


