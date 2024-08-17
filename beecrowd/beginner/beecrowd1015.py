import math

p1 = str(input()).split()
p2 = str(input()).split()
x1, y1 = p1
x2, y2 = p2
distance = math.sqrt((((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)))
print("%.4f" % distance)
