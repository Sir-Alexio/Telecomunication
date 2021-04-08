import Factorial
import Telecomunication
import random
import cycle


size = 100

location = [[0 for j in range(size)] for i in range(size)]  # квадратная область 100*100

population = [[random.randint(1, 10) for j in range(size)] for i in range(size)]  # хранит плотность населения

situation = Telecomunication.inputLocation(location)  # хранит координаты вышек связи

print(Telecomunication.countPopulation(population, situation))

size = 15

area = [[0 for j in range(size)] for i in range(size)]

area[2][1] = 555
area[2][12] = 555
area[4][12] = 555
area[4][14] = 555
area[9][14] = 555
area[9][1] = 555
area[2][1] = 555


Telecomunication.output(area)

print(cycle.findCoordinats(area))