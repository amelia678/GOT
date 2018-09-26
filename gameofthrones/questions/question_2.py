#how many characters name start with "Z"
from characters import *

z_names = []

for key in range(len(characters)):
    if characters[key]['name'][0] == 'Z':
        z_names.append(characters[key]['name'])

print(z_names)
print(len(z_names))        