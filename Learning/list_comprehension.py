# Exercise 1 / Filter only negative and zero in the list using list comprehension

'''numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg = [i for i in numbers if i <= 0]
print(neg)
'''
# Exercise 2  / Flatten
'''countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Transform the list
flattened = [
    [country.upper(), country[:3].upper(), capital.upper()] 
    for sublist in countries 
    for country, capital in sublist
]

print(flattened)'''

# Exercise 3 

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]


concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]

print(concatenated_names)
