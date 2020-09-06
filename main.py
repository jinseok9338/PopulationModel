from map import Map
from pprint import pprint
from animal import Bunny,Animal,Wolf

map = Map()

bunny =Bunny(map.map)
bunny2 = Bunny(map.map)
wolf = Wolf(map.map)
print(wolf.wolf_object)
bunny.randomly_move()
pprint(bunny.bunny_object["Position"])
pprint(map.map)
bunny.find_water_and_drink()
bunny.find_grass_and_eat()


pprint(map.map)
print(sum(list.count("G") for list in map.map))
