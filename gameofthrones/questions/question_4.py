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
# title_lengths = []                                               
# for person in characters:
#     num_titles = len(person['titles'])
#     title_lengths.append(num_titles)

# record_for_most_titles = max(title_lengths)
# print(record_for_most_titles)

# index_of_record = title_lengths.index()
# person_with_title_record = characters[index_of_record]
# print(person_with_title_record['name'])
    