from random import randint
class Map:

    number_of_grass = 25
    number_of_water = 5

    def __init__(self):
        self.day = 0
        self.year = self.day/365 #There is no leap year
        self.map = [["E" for _ in range(10)] for _ in range(10)]
        self.generate_water(self.number_of_water)
        self.generate_grass(self.number_of_grass)



    def generate_water(self,num_of_water):
        for _ in range(num_of_water):
            random_start_point = randint(0, 9)
            try:
                for a in range(random_start_point,random_start_point+2):
                    for b in range(random_start_point,random_start_point+2):
                        if self.map[a][b] != "W":
                            self.map[a][b] = "W"
                            num_of_water -=1
                        else:
                            num_of_water -= 1
                            self.generate_water(num_of_water)
            except IndexError:
                self.generate_water(num_of_water)



    def generate_grass(self,how_many_grass):
        for a in range(how_many_grass):
            while True:
                random_num_x = randint(0,9)
                random_num_y = randint(0,9)
                if self.map[random_num_x][random_num_y] == "E":
                    self.map[random_num_x][random_num_y] = "G"
                    break

    def word_a_day_passes(self):
        self.day += 1
        if self.day%5 ==0:
            self.generate_grass(self.number_of_grass)










