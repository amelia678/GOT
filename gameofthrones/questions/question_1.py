from  characters import *

def how_many_starts_with(letter):
    names = []
    for key in range(len(characters)): #for person in characters
        if characters[key]['name'][0] == letter: #person['name'][0]
            names.append(characters[key]['name'])
    print(len(names))  

how_many_starts_with('A')
how_many_starts_with('Z')

# print(a_names) 

# print(characters[0])

# {'url': 'https://www.anapioficeandfire.com/api/characters/2', 'name': 'Walder', 'gender': 'Male', 'culture': '', 'born': '', 'died': '', 'titles': [''], 'aliases': ['Hodor'], 'father': '', 'mother': '', 'spouse': '', 'allegiances': ['https://www.anapioficeandfire.com/api/houses/362'],  'books': ['https://www.anapioficeandfire.com/api/books/1', 'https://www.anapioficeandfire.com/api/books/2', 'https://www.anapioficeandfire.com/api/books/3', 'https://www.anapioficeandfire.com/api/books/5', 'https://www.anapioficeandfire.com/api/books/8'], 'povBooks': [], 'tvSeries': ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 6'], 'playedBy': ['Kristian Nairn']}