#who has most titles?

from characters import *

title_list = []

for key in range(len(characters)): #figure out who has titles
    if len(characters[key]['titles']) > 6: 
        title_list.append(characters[key]['name'])

print(title_list) 
# print(characters[key]['name': 'Balon Greyjoy']['titles'])
# print(len(title_list))
# print(max(len(characters[key]['titles']))) #use max function to find most titles
                                                
