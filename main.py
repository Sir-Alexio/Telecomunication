from numpy import arange, sin

import Factorial
import Telecomunication
import random
import cycle
import matplotlib.pyplot as plt
from numpy import *

size = 100

location = [[0 for j in range(size)] for i in range(size)]  # квадратная область 100*100

population = [[random.randint(1, 10) for j in range(size)] for i in range(size)]  # хранит плотность населения

situationOfTelecom = Telecomunication.inputLocation(location)  # хранит координаты вышек связи

powerArea = [[0 for j in range(size)] for i in range(size)] # хранит максимальную мощность каждой в каждой клетке

print('Колличество абонентов, которые имеют удовлетворительное качество связи: '+
      str(Telecomunication.countPopulation(population, situationOfTelecom, powerArea)))

#Telecomunication.output(powerArea)

#-----------------------------------------------------------------------------------------------------------------------
size = 15

area = [[0 for j in range(size)] for i in range(size)]

area[2][1] = 555
area[2][12] = 555
area[4][12] = 555
area[4][14] = 555
area[9][14] = 555
area[9][1] = 555
area[2][1] = 555

# Telecomunication.output(area)

# print(cycle.findCoordinats(area))


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


fig, ax = plt.subplots()

x = [i for i in range(100)]
y = [i for i in range(100)]

plt.plot(x,y,'r')
plt.show()