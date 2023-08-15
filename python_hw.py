#declaring (key, value)
d1 = {}

d2 = dict()

print(d1)
print(d2)
print(type(d1))
print(type(d2))

d3 = {
    'name' : "link",
    'age' :9000,
    4 : [1, 2, 3, 4, 5],
    True : {
        'game' : "legend of zelda",
        'character' : ['character1', 'character2', 'character3']
    }
}

print(d3)


#accessing

d3[True]['character'][1]

#in-class exercise 1

truck = {
    'year': 2018,
    'make': 'chevrolet',
    'model': 'silverado' 
}

print(f"{truck['year']} {truck['make']} {truck['model']}")

#adding new pairs

d3['sports'] = ['baseball', 'football']
print(d3['sports'])
d3

#modifying values

d3[True] = None
d3

#removing key, value paris

del d3[True]
d3

#looping a dictionary

for key, val in d3.items():
    print(key, val)


a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

#looping only keys

for key in d3:
    print(key)

#looping only values

for val in d3.values():
    print(val)

#exercise 2

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}

def eye_color(x):
    for name, eyes in people.items():
        print(f'{name} has {eyes} eyes')
eye_color(people)

#sorted

print(sorted(people.items()))
print(sorted(people.keys()))
print(sorted(people.values()))

#list with dictionaries

names = ['link', 'zelda', 'ganon', {"random1": 'dark link', 'random2': 'demon ganon'}]
print(names[3]['random1'])

#dictionaries with list

food = {

}

#exercise 3

def gather_info():
    info_dict = {}

    while True:
        name = input("Enter name (or 'quit' to exit): ")
        
        if name.lower() == 'quit':
            print("all names and addresses:")
            for person, address in info_dict.items():
                print(f"Name: {person}, address: {address}")
            break
        
        address = input("Enter address: ")

        info_dict[name] = address

        gather_info()


#set declaring

s1 = {1,2,3,4}
print(s1)
print(type(s1))

s2 = set()
print(s2)
print(type(s2))

#.add

print(s2)
s2.add(1)
s2.add(23)
s2.add(11)
s2.add(24)
s2.add(31)
print(s2)

#.remove

s2.remove(31)
print(s2)

#.union()

s1 = {1,2,3,4}
s2 = {3,4,5,6}

s3 = s2.union(s1)
print(s3)

s4 = s1 | s2 
print(s4)

#.inersection

s5 = s1.intersection(s2)
print(s5)

s6 = s1 & s2
print(s6)


#.difference()

s7 = s2 - s1
print(s7)

s8 = s1.difference(s2)
print(s6)

#.clear()

s8.clear()
print(s8)

#unique & immutable

frozen = frozenset(s1)
print(frozen)
print(type(frozen))


#importing entire modules

import math

print(math.pi)
print(math.ceil(4.5))
print(math.floor(4.5))

#importing methods only

from math import floor, ceil, pi

print(pi)
print(ceil(4.5))
print(floor(4.5))

#using the 'as' keyword

from math import floor as f

print(pi)
print(ceil(4.5))
print(f(4.5))

#creating a module

from mymodule import add as a
from mymodule import subtract as s

result = a(5, 3)
print(result)

result = s(10, 2)
print(result)


#excercise

def display_cart(cart):
    print("current shopping cart:")
    for item, quantity in cart.items():
        print(f'{item}: {quantity}')

def shopping_cart():
    cart = {}

    while True:
        print("option:")
        print("1 - add item")
        print("2 - delete item")
        print("3 - veiw shopping cart")
        print("4 - quit")

        choice = input("enter your choice")

        if choice == "1":
            item = input("enter item name:")
            quantity = int(input("enter quantity:"))
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
            print(f"{quantity} {item}(s) added to the cart")

        elif choice == "2":
            item = input("enter item name to delete:")
            if item in cart:
                del cart[item]
                print(f"{item} was removed")
            else:
                print(f"{item} is not in cart")
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            display_cart(cart)
            print("thank you come again")
            break
        else:
            print("invalid choice. please select valid option.")


    shopping_cart()
    
#creating moduel

import test_1 

greeting = test_1.greet('luis')
print(greeting)
#excercise 2

import mymodule

length = input('Length')
width = input('Width')

print('')

radius = input('Radius')
mymodule.circ(radius)