import random


def output(list):
    for i in list:
        for j in i:
            print(j, end="   ")
        print()
    print()


def inputLocation(location):
    low = 5
    middle = 3
    high = 2
    situation = []

    for i in range(low):
        first = random.randint(0, len(location) - 1);
        second = random.randint(0, len(location) - 1)
        location[first][second] = 1
        situation.append([first, second])

    for i in range(middle):
        first = random.randint(0, len(location) - 1);
        second = random.randint(0, len(location) - 1)
        location[first][second] = 2
        situation.append([first, second])

    for i in range(high):
        first = random.randint(0, len(location) - 1);
        second = random.randint(0, len(location) - 1)
        location[first][second] = 3
        situation.append([first, second])

    return situation


def maxPower(first, second, situation, areaPower):
    max = 0
    power = 0
    for i in range(len(situation)):

        if first == situation[i][0] and second == situation[i][1]: continue

        if 0 <= i <= 4:
            power = 100
        elif 5 <= i <= 7:
            power = 200
        elif 8 <= i <= 9:
            power = 300

        powerPoint = power / (abs(situation[i][0] - first) ** 2 + abs(situation[i][1] - second) ** 2)

        if max < powerPoint:
            max = powerPoint
    areaPower[first][second] = max
    return max


def countPopulation(population, situation, powerArea):
    total = 0
    for i in range(len(population)):
        for j in range(len(population)):
            if maxPower(i, j, situation, powerArea) > 1: total += population[i][j]
    return total

def makePlot(powerArea):
    for i in range(len(powerArea)):
        for j in range(len(powerArea)):
            if <powerArea[i][j]
