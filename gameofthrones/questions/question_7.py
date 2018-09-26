#how many characters are not in tv show
from characters import *

not_in_show = []

for key in range(len(characters)):
    if characters[key]['tvSeries'] == [""]:
        not_in_show.append(characters[key]['name'])

# print(not_in_show)
print(len(not_in_show))        