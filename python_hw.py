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

class cart():
    def __init__(self):
        self.shop_list = {}

    def add_item(self):
        item_tobe_added = input("what would you like to add")
        if item_tobe_added in self.shop_list:
            self.shop_list[item_tobe_added] += 1
        else:
            self.shop_list[item_tobe_added] = 1

def delete_item(self):
    item_tobe_deleted = input("What would you like to delete? ")
    if item_tobe_deleted in self.shop_list:
        del self.shop_list[item_tobe_deleted]
    else:
        print("you don't have that in your list.")


def veiw_list(self):
    for key, value in self.shop_list.item():
        print(value," ",key)

def quit_input(self):
    print("Thank you come again")

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