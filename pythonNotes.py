# Notes to reference from Python course
#***********************************************************************************
# Section 3: 28. I/O with Basic Files in Python

# Reading a file from anywhere on computer
# MacOS and Linux
myfile = open("/Users/YourUserName/Foler/myfile.txt", 'read(r)/write(w)/append(a)')

# With Statement
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

# mode values
# mode = 'r' is read only
with open('myfile.txt', mode = 'r') as myfile:
    print(myfile.read())
# mode = 'w' is write only (will overwrite or create new)
with open('myfile.txt', mode = 'w') as myfile:
    myfile.write('ONE ON FIRST')
# mode = 'a' is append
with open('myfile.txt', mode = 'a') as myfile:
    myfile.write('TWO ON SECOND\nTHREE ON THIRD\nFOUR ON FOURTH')
# mode = 'r+' is reading and writing
# mode = 'w+' is writing an dreading (Overwrites existing files or creates new)

#***********************************************************************************
# Section 5: Statements

# if elif and else
# makes use of colons and indentation
# if some_condtion:
    # execute some code
# elif some_other_condition:
    # do something different
# else:
    # do something else

# Examples
hungry = False
if hungry:
    print('Feed me')
else:
    print("I'm not hungry")

loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool')
elif loc == 'Bank':
    print('money is cool')
else:
    print('Idk')

# For loops
#syntax
my_iterable = [1,2,3]
for item_name in my_iterable:
  print(item_name)

#example
myList = [1,2,3,4,5,6,7,8,9,10]
for jelly in myList:
    # output should print every item in the list
    print(jelly)

# print only even numbers in list
for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for each in myList:
    list_sum = list_sum + each

print(list_sum)

hello = 'Hello'
for letter in hello:
    print(letter)

# OR

for letter in 'Hello':
    print(letter)

# if you don't intend to use the variable in for loop
# common practice is to use an '_' as the name

tuple = [(1,2), (3,4)]

for item in tuple:
    print(item)

for a,b in tuple:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2}
for item in d:
    # prints keys: 'k1' 'k2'
    print(item)

for item in d.items():
    #prints key and value ('k1, 1)
    print(item)

for k,v in d.items():
    #prints value only
    print(v)

for v in d.values():
    #same as above
    print(v)

# While Loops
#syntax
# while some_boolean_condition:
#   do something

#Can be combined with else

x = 0
while x < 5:
    print(f'The value of x is {x}')
    x += 1
else:
    print('X is not less than 5')

# keywords for loops
# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: Does nothing

y = [1,2,3]
for item in y:
    pass
# place holder to not deal with a syntax error

name = 'Ryan'
for letter in name:
    if letter == 'a':
        continue
    # this allows you to skip the letter a by continuing to the next iterable in the list
    print(letter)

while x < 5:
    if x == 2:
        break
    print(x)
    x +=1

# Other Useful Operators

# Range
# example:
# range(start, stop, step)
for each in range(0,10,2):
    print(each)
# this would print each number starting at zero up to 10 but not including incrementing by 2 each time

# Enumerate
word = 'abcde'
for item in enumerate(word):
    print(item)
#prints a tupe of (index, value) so (0, 'a')

for index, value in enumerate(word):
    print(index)
    # prints only index 

# Zip
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)  
# prints tuple based on index ex: (1, 'a')
# if lists are uneven in length it will only do the lenght of shortest list in zip

#  In
'x' in ['x', 'y', 'z'] #true
'h' in 'hello' #true

# Min / Max
min(list1) # prints min value of list
max(list1) # prints max value of list

# random imports
from optparse import check_choice
from random import shuffle
randomList = [1,2,3,4,5]
shuffle(randomList)
# only works in place can't assign

from random import randint
randint(0,100)
# returns random int between 1 and 100
myNum = randint(0,10)

#input
result = input('Enter a number: ')
#  results type will be a string because input returns a string
# you can cast to in or float
resultInt = int(input('Number: '))

# List Comprehensions

# A good alrenative to using a loop and the append statment to 
# create a list

myString = 'hello'

mylist = [letter for letter in myString]

# list contains all numbers 0-10
numList = [num for num in range(0,11)]

# squared version of each iterable
numList = [num**2 for num in range(0,11)]
    
# list of even numbers between 0 and 10 squared
modlist = [x**2 for x in range(0,11) if x%2 == 0]

celcius = [0,10,20,30.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

#***********************************************************************************
# Section 6: Methods and Functions

# snake casing for naming of functions
# def keyword
def name_of_function(name='Default'):
    '''
    Docstring explains function.
    '''
    print(f"Hello {name}")

def add_funciton(num1, num2):
    return num1+num2

def even_check(number):
    return number % 2 == 0

def check_even_list(even_list):
    for num in even_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

check_even_list([3,5,7,8]) # returns True


def return_even_list(even_list):
    even_numbers = []
    for num in even_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

# Returning Tupes (Tuple Unpacking)

# Tuple unpacking recap
stock_prices = [('APPL', 200), ('GOOGL', 400), ('MSFT', 100)]
for ticker, price in stock_prices:
    print(ticker)
    print(price)


work_hours = [('Lizzie', 50), ('Ryan', 30), ('Griffin', 30)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

name,hours = employee_check


# Interactions Between Functions

# cup game
from random import shuffle
cups = [' ', 'O', ' ']

def return_shuffled_list(cups):
    shuffle(cups)
    return cups

def player_guess():
    guess=''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2")
    
    return int(guess)

def check_guess(cups, guess):
    if cups[guess] == 'O':
        print('You Win!')
    else:
        print("Sorry not your lucky day.")
        print(cups)

mixedup_list = return_shuffled_list(cups)

guess = player_guess

check_guess(mixedup_list, guess)


# unlimated number of args can be passed 
# and args is a tuple containing them
def myfunc(*args):
    print(args)

# kwargs returns a dictionary
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit is: {}'.format(kwargs['fruit']))
    else:
        print("No fruit")

myfunc(fruit='apple', veggie='lettuce')
# returns: {'fruit': 'apple', 'veggie':  'lettuce'}

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='oragne',food='eggs',animal='dog')
# returns: I would like 10 eggs


# Lamda Expressions Map and Filter

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

list(map(square,my_nums))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['and', 'eve', 'sally']
list(map(splicer,names))


def check_even(num):
    return num%2==0

my_nums = [1,2,3,4,5,6]
list(filter(check_even, my_nums))

for n in filter(check_even,my_nums):
    print(n)


# lamda
lambda num: num ** 2

list(map(lambda num:num**2,my_nums))

list(filter(lambda num : num%2 ==0, my_nums))



# Nested Statements and Scope

#Changing global values locally
x = 50

def func():
    global x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT
    x = 'New Value'
    print(f'I just locally changed global X to {x}')

# dont do this ^ often just pass x as parameter and then set x = func(x)

#***********************************************************************************
# Section 7: Milestone Project

# Displaying information

row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

display(row1,row2,row3)

# User Input and Validation
def take_turn():    
    index = int(input("Choose an index position: "))
    while index.isdigit() == False:
        print('Sorry that is not an integer.')
        index = int(input('Please enter an integer for the index position: '))
    return index


from IPython.display import clear_output
clear_output()

def take_turn():
    acceptable_values = [0,1,2]
    index_flag = False
    index = 'Index'
    while index.isdigit() == False or index_flag == False:
        index = input("Choose an index position (0-2): ")
        
        if index.isdigit() == False:
            clear_output()
            print('Sorry that is not an integer.')
        
        if index.isdigit():
            if int(index) in acceptable_values:
                return int(index)
            else:
                print('Sorry that integer is not in the accepted range!')

from IPython.display import clear_output
clear_output()
def get_index():
    index = 'default'
    acceptable_values = ['0','1','2']
    while index not in acceptable_values:
        index = input('Choose an index position (0-2): ')
        if index not in acceptable_values:
            clear_output()
            print('You did not enter 0, 1, or 2')
    return int(index)

