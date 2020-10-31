import math

def area_of_cone(height, radius):
    return math.pi*(radius)*math.sqrt(radius**2+height**2)

surface_area = area_of_cone(5,10)
print(surface_area)
surface_area = area_of_cone(5.0,10.0)
print(surface_area)
surface_area = area_of_cone(0,10)
print(surface_area)
surface_area = area_of_cone(5,0)
print(surface_area)