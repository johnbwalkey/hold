# example functions and syntax
print ("Hello World")
age =20
print (age)
age = 30
print (age)
price =19.95
first_name = "John"
last_name='Walkey'
print ("Hello " + first_name)

is_available= True

# so 3 types of dat - numbers, strings & boolean
# convert - error type - year= input('what year you born ') so...
year= input('what year you born? ')
age = 2024 -int(year)
print (age)

# calc (input returns a string)
first=input("first: ")
second = input ("second: ")
sum = int(first) + int(second)
print (sum)

# if float input ( could put flot in front of input)
first = input("first: ")
second = input ("second: ")
sum = float(first) + float(second)
print ("sum: " +str(sum))

# Strings - type a string name - then dot and see methods ... cas, find, replace ==immutablle
course = 'Python'
new = course.upper()
print (new)

## math operators  - + * / and ** is exponent and
print (10+3)
print (10/3) # divide get float
print (10//3) # get integer
print (10 % 3) # get remainder
print (10**3)

# augmented operator
x=10
x=x+3
x+=3 # same as line above - aug assignment  operator/ can do subtract -= AND *= OR /=

# order of operations
x=10+3*2
y=(10+3)*2
print (x)
print (y)
# comparison operators > < >= <= == != (== is compare)

# Boolean
price =25
print (price > 10 and price <30) # get True - could use or and not (logical operators)

# if statements
temp = 30
if temp > 40: # executed if True  -- indentation represent a block of code {curl braces  in C etc}
    print ("It's a hot day")
    print ("drink water")
print ("done...") # could use elif with : at end for second condition (can have many!!!)
# end with else: which gets executed if none of other conditions true

# While loops - repeat a block of code a number of times
# (if do 1_000 it works and makes code more readable)
i=1
while i <=5:
    print(i) # could do print (i * '*')
    i=i+1

# Lists - complex type (beside number, str and boolean)
names = ["jo", "bill", "tom", "jane"] # each has an index 0 is first element
print (names[-2])
# change value - names [0] = "John"
# or print range
print (names[1:2])

# List methods type "a". see list of options example numbers.   see choices like append













