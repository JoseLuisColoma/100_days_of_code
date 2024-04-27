# dic = { key: value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

programming_dictionary["key3"] = ["value3", 'value4', 'value5']
print(programming_dictionary)

print(programming_dictionary.keys())
print(programming_dictionary.values())
print(programming_dictionary.items())

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

