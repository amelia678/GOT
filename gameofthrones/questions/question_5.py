# how many are Valerian?
from characters import *

valerian_list = []

for key in range(len(characters)):
    if characters[key]['culture'] == "Valyrian":
        valerian_list.append(characters[key]['name'])

# print(valerian_list)        
print(len(valerian_list))
