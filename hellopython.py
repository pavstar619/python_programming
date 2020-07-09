import random
import sys
import os

###No New Lines###
""" print("I don't like ", end="")
print("newlines")
print("5 new lines \n" *5) """

###Lists###
""" grocery_list = ['Juice','Banana','Mango']

print('First item',grocery_list[0])

grocery_list[0] = 'Green Juice'
print('Items',grocery_list[0:3])

other_events = ['Wash hands','Clean car','Drive by']

to_do_list = [other_events,grocery_list]
print(to_do_list)

print(to_do_list[0][1])

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1,'Pickle')

grocery_list.remove('Pickle')

grocery_list.sort()

grocery_list.reverse()

del grocery_list[3]
print(to_do_list)

to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2)) """

###Tuples###
""" pi_tuple = (3,1,4,5,9)
print('Tuple',pi_tuple)

new_tuple = list(pi_tuple)

new_tuple.sort()
print('List',new_tuple)

new_list = tuple(new_tuple)
print('Sorted tuple',new_list) """

###Dictionary###
""" super_hero = {'Hero1' : 'Superman',
			  'Hero2' : 'Batman',
			  'Hero3' : 'Spiderman', }

print(super_hero)

del super_hero['Hero1']
print(super_hero)

print(len(super_hero))
print(super_hero.keys())
print(super_hero.values()) """

###If else statements###
""" age = 21

if age>16:
	print('You can drive')
else:
	print('You cant drive')

if age >= 21 :
	print('Pro driver')
elif age>=16 :
	print('Noob driver')
else :
	print('Cant drive') """

###For Loops###
""" for x in range(0,10):
	print(x,' ', end='')

print('\n')

grocery_list = ['Juice','Banana','Mango']

for y in grocery_list:
	print(y)

print('\n')

x = [2,4,5,67,8,88,6]
x.sort()
for d in x:
	print(d)

num_list = [[1,2,3],[4,5,6],[7,8,9]]

for x in range(0,3):
	for y in range(0,3):
		print(num_list[x][y]) """

###While loops###
""" i = random.randrange(0,100)

while(i != 10):
	print(i)
	i = random.randrange(0,100) """

###Functions###
""" def add(a,b):
	sum = a + b
	return sum

print('Added number',add(1,5)) """

###Inputs###
""" print('Name?')

name = sys.stdin.readline()

print('Hello', name) """

###Strings###
""" string = "I'll be there for you"

print('First 4 chars:',string[0:4])
print('Last 5 chars:',string[-5:])
print('Contatenate:',string[:4] + " be there")

print("Number %d letter %c float %f" %(15,'a',123.444))

print(string.capitalize())
print(len(string))
print(string.replace("be","forrrrrr"))
print(string.strip())

quote_list = string.split(" ")
print(quote_list) """

###Files###
""" test_file = open("text.txt","wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("hello world","UTF-8"))

test_file.close()

test_file = open("text.txt","r+")

text_in_file = test_file.read()
print(text_in_file)

#os.remove("text.txt") """


###Objects - Encapsulation/ Polymorphism/ Inheritance###
class Animal:
	__name = ""
	__height = 0
	__weight = 0
	__sound = 0

	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound

	def set_name(self,name):
		self.__name = name

	def get_name(self):
		return self.__name
	
	def set_height(self,height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_weight(self,weight):
		self.__weight = weight

	def get_weight(self):
		return self.__weight
	
	def set_sound(self,sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kg and say {}".format(self.__name,self.__height,self.__weight,self.__sound)

cat = Animal('Whiskers',33,10,'Meow')

print(cat.toString())

class Dog(Animal):
	__owner = ""

	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner
		super(Dog,self).__init__(name,height,weight,sound)

	def set_owner(self,owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString(self):
		return "{} is {} cm tall and {} kg and say {} and Owner is {}".format(self.get_name(),self.get_height(),self.get_weight(),self.get_sound(),self.__owner)

dog = Dog('Spike',53,15,'Woof','Harru')

print(dog.toString())

#Polymorph
test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)	
