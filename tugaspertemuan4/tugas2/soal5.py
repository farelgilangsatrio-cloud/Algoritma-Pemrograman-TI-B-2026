# soal 5
import math

def jarak(x1, y1, x2, y2):
    bagian_x = math.pow(x2 - x1, 2)
    bagian_y = math.pow(y2 - y1, 2)
    d = math.sqrt(bagian_x + bagian_y)
    return d

print("Jarak =", jarak(0, 0, 3, 4))