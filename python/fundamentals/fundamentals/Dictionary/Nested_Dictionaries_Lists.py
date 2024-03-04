# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Change the value 10 in x to 15
x[1][0] = 15

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# Change the value 20 in z to 30
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)


# Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for item in some_list:
        result = ""
        for key, value in item.items():
            result += f"{key} - {value}, "
        print(result[:-2])  # to remove the last comma and space


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for item in value:
            print(item)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
