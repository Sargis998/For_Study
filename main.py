''' 
name = input("Enter Your name: ")
print(f"Hello, {name}")
'''
'''my_string = "Barev Sargis"
print(my_string .lower())
print(my_string .upper())'''

'''greetiing = "hello" + " " "sargis"
print(greetiing)
repeated="Ha" "  " * 3
print(repeated)'''

'''Father = "Alex"
Mother = "Mary"
Formated = f"Elens father name is {Father} and Her mothers name is {Mother}"
print(Formated)'''

''' 
name = input("Enter Your name: ")
The_text= f" Hello My name is, {name}."
print(The_text)
'''
''' 
user_input = input("Enter Your string: ")
hetntac_input = user_input[::-1]
print(hetntac_input)
'''
''' 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
'''
''' 
numbers = list(range(1,11))
total = sum(numbers)
print(total)
'''

''' 
greeting = "Hello, World"
count_o = 0
for char in greeting:
    if char == "o":
        count_o = count_o + 1
        print(char)
print(count_o)'''

''' 
this_tuple = ("orange", "banan","kiwi")
del this_tuple
print(this_tuple)
'''
''' 
numbers_1 = [1,2,3,4,5]
numbers_2 = [6,7,8,9,10]

def find_average (numbers):
     average = sum(numbers) / len(numbers)
     return average



average_1 = find_average(numbers_1)
print(average_1)
'''
''' 
#Math
import datetime



x = datetime.datetime(2015, 5, 12)

print(x)'''



''' 
#JSON
import json

book =  {
    'title': '1958',
    'author': 'Eric',
    'isd':'qwfW',
    'UGDQ':'qwfrf',
}

json_string= json.dumps(book)

print(type(json_string))
print(json_string)
'''
''' 
import random

list = [1,2,3,4,5,80]

print(random.choice(list))
print(globals().keys())
'''

#Polymorphism
'''
dict = {
    'mercedes':"a180",
    'bmw':530,
    'Toyota':'Camry',
    'audi':"a6"
}

print(len(dict))
''' 
''' 
class Dog:
    def speak (self):
        return "Haf, haf"
    
class Cat:
    def speak (self):
        return "Meow !!"

def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()


animal_sound(dog)
animal_sound(cat)
'''



#polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Haf-Haf"

class Cat(Animal):
    def speak(self):
        return "Meow !"


cat = Cat()
dog = Dog()
print(cat.speak())
print(dog.speak())