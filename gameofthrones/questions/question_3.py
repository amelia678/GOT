#how many characters are dead?

from characters import *

dead_list = []

for key in range(len(characters)):
    if characters[key]['died'] != "": # if character doesn't have death date, add to list
        dead_list.append(characters[key]['name'])


# print(dead_list)
print(len(dead_list))        