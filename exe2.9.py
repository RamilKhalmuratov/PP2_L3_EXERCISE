import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

r = float(input("Radius: "))
print("Volume:", sphere_volume(r))
