people = {
    "stan": 21,
    "robert": 25,
    "jon": 20,
    "steve": 30,
    "bob": 19
}

# [ "stan", "robert", "steve" ]
def min_age(group):
    '''return an list with the name of every person that is 21 or above'''
    results = []

    for key in group.keys():
        if group[key] >= 21:
            results.append(key)
    
    return results

print('these people are 21 and above', min_age(people))

# dictionary = { 
#    'Novel': 'Pride and Prejudice', 
#    'year': '1813', 
#    'author': 'Jane Austen', 
#    'character': 'Elizabeth Bennet' 
# }

# for key, value in dictionary.items(): 
#    print(key ,value)

# word_freq = {
#     'Hello' : 56,
#     'at'    : 23,
#     'test'  : 43,
#     'This'  : 78,
#     'Why'   : 11
# }

# for value in word_freq.values():
#     print(value)

# mydict = {
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
# }
# for key in mydict.keys():
#     print(key)