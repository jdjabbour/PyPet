import random
import os

pycat = {
    "photo": "(=^o.o^=)__//",
    'name': "Edgar",
    'age': 2,
    'weight': 9.5,
    'hungry': True,
    'phrases': ["mew...", "I'm hungry...", "I do what I want...", "Is that for me?..."]
}

py_thon = {
    "photo": "~<:<<<<<<<<<>",
    'name': "Fluffy",
    'age': 20,
    'weight': 7,
    'hungry': True,
    'phrases': ["Hissss...", "I'm hungry...", "Is it cold in here?...", "Is that for me?..."]
}


pypet = pycat


def startup_pypet():
    print("Welcome to Pypet.")
    os.system("echo 'Welcome to PyPet'")

def pypet_stats():
    print("Hello, it's {} !".format(pycat['name']))
    print(pycat['photo'])
    print("{} weighs {} pounds.".format(pycat['name'], str(pycat['weight'])))

    if pycat['hungry']:
        print("Your Pet is hungry.")
    else:
        print("Your pet *BURPS* loudly")

terminate = False

while not terminate:
    print("#############################################################")
    startup_pypet()
    user_input = input("> ")

    if user_input == 'quit':
        terminate = True
    elif user_input == 'feed':
        print("OMNOMNOMNOMNOMN...  You fed your pypet")
        pycat['weight'] += 1
        hungry = False
    elif user_input == 'stats':
        pypet_stats()
    elif user_input == 'chat':
        print(random.choice(pycat['phrases']))
    else:
        print("Command not recognized.  Please try again.")

print("You have quit pypet.  Goodye.")

