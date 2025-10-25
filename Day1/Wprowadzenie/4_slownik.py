my_dictionary = {
    "apples": 5,
    "bananas": 10,
    "oranges": 7,
    "grapes": 4,
    "pineapple": 2,
    "peach": 3,
    "pear": 5
}

my_dictionary.update({
    "cherries": 24
})

my_dictionary["cherries"] = 20

print(my_dictionary)
print(sum(my_dictionary.values()))
