#What actor plays "Hot Pie'
from characters import *

for key in range(len(characters)):
    if characters[key]['name'] == 'Hot Pie':
        print(characters[key]['playedBy'][0])