import Factorial
import Telecomunication
import random

size = 100

location = [[0 for j in range(size)] for i in range(size)]  # квадратная область 100*100

population = [[random.randint(1, 10) for j in range(size)] for i in range(size)]  # хранит плотность населения

situation = Telecomunication.inputLocation(location)  # хранит координаты вышек связи

print(Telecomunication.countPopulation(population, situation))
