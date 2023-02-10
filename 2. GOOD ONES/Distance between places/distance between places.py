from geopy.distance import geodesic

'''
# loading the latitude and longitude from two places
first_place = (52.2296756, 21.0122287)
second_place = (52.406374, 16.9251681)


# print distance in km
distance = int(geodesic(first_place, second_place).km)
print(distance, "kilometers") # 279 kilometers

'''
latP1 = float(input("Input the latitude of the first place: "))
longP1 = float(input("Input the longitude of the first place: "))
latP2 = float(input("Input the latitude of the second place: "))
longP2 = float(input("Input the longitude of the second place: "))

first_place = (latP1, longP1)
second_place = (latP2, longP2)

distance = int(geodesic(first_place, second_place).km)
print(distance, "kilometers")

