import Telecomunication

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