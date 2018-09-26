#Produce a list characters with the last name "Targaryen"

from characters import *

targaryen_list = []

for key in range(len(characters)):
    if "Targaryen" in characters[key]['name'] :
        targaryen_list.append(characters[key]['name'])

# print(targaryen_list)
print(len(targaryen_list))        