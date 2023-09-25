# name = 'Janet'
# surname = ' Dansu'
# Names = name + surname
# print(Names)

# numberOne = 2 #camelCase
# NumberOne = 3 #PascalCase
# number_one = 5 #snake_case

# numberOne = 1
# numberTwo = 2.8
# numberThree = 1j
# name = ' Victor name '

# print(name.upper())


# print('Enter your name:')
# name = input()
# print('Hello' + name)


# names = ['David',1, 'John']
# x = 'David'
# check = x not in names
# print(check)

# a = 2
# b = 3

# if a == b:
#     print('Nice one')
# elif b > a:
#     print('Nice two')
# else:
#     print('Bad one')


# print('Hello My gee') if a > b else print('Bye my gee')
# a = 2
# b = 3

# if a > b and b == a:
#     print('Hello')
# else:
#     print('Gbem Gbem')


# fruits = ["apple", "banana", "cherry"]
# myFruits = list(('apple', 'banana', 'cherry'))
# fruits[0] = 'pineapple'
# fruits.append('Mango')
# fruits.insert(1, 'orange')
# fruits.remove('orange')
# fruits.pop(1)
# del fruits[1]
# del fruits

# print(fruits)


# fruits = ('Mango', 'orange', 'Apple','Cherry','Apple')
# print(fruits.count('Apple'))


# fruits = {"apple", "banana", "cherry"}
# x = 'cherry'
# check = x in fruits
# print(check)



# fruits = {"apple", "banana", "cherry"}

# for x in fruits:
#     print(x)

# fruits = set(("apple", "banana", "cherry"))

# print(fruits)


# thisdict = {
#     'name': 'David',
#     'age': 20,
#     'description':'Software developer'
# }
# thisdict.popitem()
# print(thisdict)


# i = 1
# while i < 6:
#     print(i)
#     if i == 4:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# fruits = ['Apple', 'Mango', 'Guva']

# for x in fruits:
#     if x == 'Mango':
#         break
#     print(x)

# for x in range(13):
#    for i in range(13):
#     e = x * i

#     print(e)
   

# thisdict = {
#     'name': 'David',
#     'age': 20,
#     'description':'Software developer'
# }

# for x in thisdict.keys():
#     print(x)

# username = input('Enter username: ')
# password = input('Enter password: ')
# print('Welcome to Login Page')
# username1 = input('Enter username: ')
# password1 = input('Enter password: ')
# if username == username1 and password == password1:
#     print('Login Successfully')
# else:
#     print('Login Failure')


# for i in range(13):
#     for x in range(13):
#         sum = i * x
#         print(f'{i} X {x} = {sum}')


# def my_function(num):
#     sum = num * num
#     print(sum)

# my_function(4)

# myglobal = 'Hehhehehe'

# def my_function():
#     mylocal = 'Hello, world!'
#     print(myglobal, mylocal)

# my_function()
# print(myglobal)
# print(mylocal)

# x = 7
# def my_function():
#     global x
#     x+= 4
#     print(x)
# my_function()
# print(x)

# total_words = 2500
# words_per_page = 300
# print(divmod(total_words, words_per_page))
# print("filter function")
# ages = [5, 12, 17, 18, 24, 32]
# def myFunc(x):
#  if x < 18:
#     return False
#  else:
#     return True
 
# adults = filter(myFunc, ages)
# for x in adults:
#  print(x)

# x = float(3)
# print("float ", x)


# class Shark:
#     def __init__(self,name,age):
#         self.name  = name
#         self.age = age

#     def swim(self):
#         # print(self.name + ' come and swim')
#         print('{} come and swim you are {}yrs old'.format(self.name,self.age))
#         print(f'{self.name} come and swim you are {self.age}yrs old')

#     def be_awesome(self):
#         print('Be awesome')

# our_instance = Shark('David',5)
# our_instance.swim()
# our_instance.be_awesome()


# class Fish:
#     def __init__(self, first_name, last_name = "Fishes",skeleton="bone", eyelids=False):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.skeleton = skeleton
#         self.eyelids = eyelids

#     def swim(self):
#         print("The fish is swimming.")

#     def swim_backwards(self):
#         print("The fish can swim backwards.")


# class Clownfish(Fish):
#     def live_with_anemone(self):
#         print("The clownfish is coexisting with sea anemone.")

# casey = Clownfish("Casey","Fish")
# print(casey.first_name + " " + casey.last_name)
# casey.swim()
# casey.live_with_anemone()

import datetime

now = datetime.datetime.now()

# Format the date using strftime
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# formatted_date = now.strftime("%S")
# print("Formatted Date:", formatted_date)

formatted_time = now.strftime("%Y-%m-%d %I:%M:%S %p")
print("Formatted Time:", formatted_time)