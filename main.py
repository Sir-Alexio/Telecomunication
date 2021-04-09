
import Factorial
import Telecomunication
import random
import cycle

import matplotlib.pyplot as plt


size = 100

location = [[0 for j in range(size)] for i in range(size)]  # квадратная область 100*100

population = [[random.randint(1, 10) for j in range(size)] for i in range(size)]  # хранит плотность населения

situationOfTelecom = Telecomunication.inputLocation(location)  # хранит координаты вышек связи

powerArea = [[0 for j in range(size)] for i in range(size)] # хранит максимальную мощность каждой в каждой клетке

print('Колличество абонентов, которые имеют удовлетворительное качество связи:  '+
      str(Telecomunication.countPopulation(population, situationOfTelecom, powerArea)))

fig, ax = plt.subplots()  # визуализируем данные

Telecomunication.makePlot(powerArea, plt)

plt.show()

# -----------------------------------------------------------------------------------------------------------------------

size = 15

area = [[0 for j in range(size)] for i in range(size)]
print("Введите координаты точки")
#while(True):
 #   print("x:",end=' ')
  #  x = input()
   # print("y:",end=' ')
    #y = input()
    #if x or y <0:
     #   print("Введены неверные данные")
      #  continue
    #area[x][y] = 555

area[2][1] = 555
area[2][12] = 555
area[4][12] = 555
area[4][14] = 555
area[9][14] = 555
area[9][1] = 555
area[2][1] = 555

#Telecomunication.output(area)

#print(cycle.printCoordinates(area))

