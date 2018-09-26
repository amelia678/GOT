#Create a histogram of the houses (it's the "allegiances" key)

from characters import *

allegiance_list = []

for key in range(len(characters)):
    if characters[key]['allegiances'] != []:
        allegiance_list.append(characters[key]['allegiances'])

print(allegiance_list)        