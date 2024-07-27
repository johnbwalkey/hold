# Course files can be found here:

# https://drive.google.com/drive/folders/1Ybdk2XBc4wL2poXu3LJBmWEEl8kFZ93C?usp=sharing

#%% how to restart the kernel if you have problems
# klick the restart arrow on the right
# this clears the environment with variables
# then you have to run all code again

#%% we are making cells by typing "#%%" 
# we can run the cell by pressing Ctrl and Enter
# the result is then shown in the interactive window on the right
# if you are not using vscode with the interactive window, then you must use the print
# function to see the output in the console

#%%  show the different ways to import modules
# this does not work because base Python does not have a log function:
# the log function can be found in the "math" module
a = log(3)

#%% there are 4 ways to import a module
# a module is a collection of functions you can use, after importing the module

# import the module as a shorthand
# must write the shorthand before the function name
# RECOMMENDED
import math as m
a = m.log(3)
a

#%% import the module without a shorthand
# must write the module name before each function call
# safe, but incurrs extra typing, especially for modules with long names
import math
a = math.log(10)
a

#%% import separate functions
# safe but you have to keep in mind if any functions with the same name is loaded
from math import log
a = log(20)
a

#%% import all functions from the module
# a module might contain hundreds of functions
# this is not recommended as it crowds the namespace
# that is, you are not sure from which module the function you run actually is
# AVOID!
from math import *

#%% if you need to print several values, put them into print statements
# otherwise you only print the last evaluation
a = m.log(100)
b = m.exp(30)

print(a)
print(b)

#%% install modules which is not currently installed
# open the "Terminal" tab at the bottom of vscode and write:
# py -m pip install module_name

# you can also install modules from the command window
# in windows: on the start menu, search for "cmd"
# now you see the command window app, click it
# type py - m pip install module_name in the command window and hit enter

#%% import modules so we can use the functions stored within them

#%% generate data
# import the numpy module, which you installed by writing
# py -m pip install numpy
import numpy as np

# now you can use the functions within the numpy module by writing "np." followed by the function name
my_random_numbers = np.random.randn(10)
my_sequence = np.arange(1,11)

#%% print out the sequences
print(my_random_numbers)
print(my_sequence)

#%% make a figure with the plot() function
import matplotlib.pyplot as plt

plt.plot(my_sequence,my_random_numbers)
plt.show()

#%%
plt.plot(my_sequence,my_random_numbers,"o")
plt.show()

#%% make a figure with the scatter() function
plt.scatter(my_sequence,my_random_numbers)
plt.show()

#%% save a figure
# if you would like to enhance your figure with labels, legends, and so on...
# or if you would like to save your figure...
# it is beneficial to split the figure into a figure object and an axis object
# this means that you should do this whenever you are making a figure, just by habit
# to save the figure, use .svg format, as your figure then can be resized without loss

fig, ax = plt.subplots()
plt.scatter(my_sequence,my_random_numbers)
fig.savefig('my_figure.svg', format='svg')
plt.show()

#%% variables
# numbers, integers
my_number = 1
print(my_number)
type(my_number)

#%% numbers, decimal numbers
my_decimal_number = 2.3
print(my_decimal_number)
type(my_decimal_number)

#%% text
my_string = 'pizza'
print(my_string)
type(my_string)

#%% boolean values can either be True or False
# remember to not put the value in quotes
my_boolean = True
print(my_boolean)
type(my_boolean)

#%% vectors
# lists are made by square brackets []
integers = [2, 3, 4, 5]
print(integers)

decimal_numbers = [3.4, 2.1, 6.9]
print(decimal_numbers)

names = ['Eddie', 'Sarah', 'Emma']
print(names)


#%% select one element
# remember that indexing in Python starts at zero (0)
print(names[0])
print(names[1])
print(names[2])

#%% tuples are made by parenthesis ()
# tuples cannot be changed after generation 
# (no adding, changing or removing elements)
integers_tuple = (2, 3, 4, 5)
print(integers_tuple)

#%% get text user input, hit Enter to exit
user_name = input('Please provide a name: ')
print(user_name)

#%% get numerical user input, hit Enter to exit
user_integer = int(input('Please provide an integer: '))
print(user_integer)

#%% get decimal number user input, hit Enter to exit
user_float = float(input('Please provide a decimal number: '))
print(user_float)

#%% read csv file
# the file content will be placed in the "data" dataframe
# a dataframe is a variable which resembles a sheet in Excel
# it has column headers and the columns can be numbers, boolean or strings
# now we must import the module pandas, in order to use the read_csv() function

import pandas as pd
data = pd.read_csv('data_house_prices.csv')

#%% read txt file
data2 = pd.read_csv('data_house_prices.txt', sep='\t')

#%% read excel file
data3 = pd.read_excel('data_house_prices.xlsx')

#%% see the first 6 rows of data
print(data.head(6))

#%% see the last 6 rows of data
print(data.tail(6))

#%% can print one of the columns
print(data['price'])

#%% get a summary of the different columns
# note that the describe function only gives summary of numerical variables
print(data.describe())

#%% can round the result
print(round(data.describe(),2))

#%% include('all') to see if there are non-numeric variables
print(data.describe(include='all'))

#%% can see that city is not numerical, so get unique values and their counts for this variable
print(data['city'].unique())
print(data['city'].value_counts())

#%% from the summary we could not see missing data (for the "price" variable)
# use the info() method (function) instead
# float is decimal number, int is integer, object is string (text)
print(data.info())

#%% clean the data by removing rows with missing data
data = data.dropna()

#%% now plot all variables in a matrix to see if there is a relationship between them
pd.plotting.scatter_matrix(data,figsize=(20,15))

#%% can also calculate the metrics manually
# minimum value
print(data['price'].min())
# maximum value
print(data['price'].max())
# average
print(data['price'].mean())
# variance
print(data['price'].var())
# standard deviation
print(data['price'].std())
# skewness
print(data['price'].skew())
# kurtosis
print(data['price'].kurt())

#%% subset data
# subset on column names
# to select multiple columns, add square brackets [] around them
data[['price','city']]

#%% subset on row numbers
data[0:10]

#%% subset rows from one column based on values in a different column
data['price'][data['city']=='trondheim']

#%% subset rows on values in a specific column 
data[data['square_meters']>50]

#%% subset rows and columns
data[['price','square_meters']][data['square_meters']>50]

#%% subset rows and columns based on on several conditions
# now we have to add parenthesis around the conditions
data[['price','square_meters','parking']][(data['square_meters']>50) & (data['parking']==1)]

#%% use the pipe operator "|" for "or"
data[['price','square_meters','parking']][(data['square_meters']>50) | (data['parking']==1)]
#%% plot data
# plot one variable
fig, ax = plt.subplots()
ax.plot(data['price'],'o')
plt.show()

#%% can change the colour
fig, ax = plt.subplots()
ax.plot(data['square_meters'],'^',c='darkred')
plt.show()

#%% more informative to plot two variables to see if there is a relationship we can use for explanation or prediction
fig, ax = plt.subplots()
ax.scatter(data['square_meters'],data['price'])
plt.show()

#%% make the plot more laborate, test different values for pch and colour
fig, ax = plt.subplots()
ax.scatter('square_meters','price',c='red',data=data)
ax.set_xlabel('Square meters')
ax.set_ylabel('Price')
ax.set_title('Price vs. square meters')
plt.show()

#%% can also use hexadecimal colour codes
# google 'hexadecimal color picker' to find the correct colour for you
fig, ax = plt.subplots()
ax.scatter('square_meters','price',c='#1f7d24',data=data)
ax.set_xlabel('Square meters')
ax.set_ylabel('Price')
ax.set_title('Price vs. square meters')
plt.show()

#%% histogram
# histogram of price, check for how the distribution looks and if there are gaps
fig, ax = plt.subplots()
ax.hist(data['price'])
plt.show()

#%% can have more bins to put values into
fig, ax = plt.subplots()
ax.hist(data['price'], color='#1f7d24',bins=20)


#%% several plots in one, define rows and columns
fig, ax = plt.subplots(nrows=2,figsize=(10,10))
ax[0].hist(data['price'][data['city']=='oslo'], 
           color='darkblue',
           bins=20,
           range=[0,10000000])
ax[0].set_title('Oslo')
ax[1].hist(data['price'][data['city']=='trondheim'], 
           color='darkred',
           bins=20,
           range=[0,10000000])
ax[1].set_title('Trondheim')

#%% boxplot to look for outliers 
fig, ax = plt.subplots()
ax.boxplot(data['price'])
plt.show()

#%% more elaborate boxplot
fig, ax = plt.subplots()
ax.boxplot(data['price'])
ax.set_title('Price')
plt.show()

#%% multiple boxplots to compare the distribution of different groups
fig, ax = plt.subplots(ncols=2,sharey=True,figsize=(10,10))
ax[0].boxplot(data['price'][data['city']=='oslo'])
ax[0].set_title('Oslo')
ax[1].boxplot(data['price'][data['city']=='trondheim'])
ax[1].set_title('Trondheim')
plt.show()

#%% barplot
# make table, parking count
parking_count = data['parking'].value_counts()
# make categories
parking_categories = ['0','1']
fig,ax = plt.subplots()
ax.bar(parking_categories,parking_count)
plt.show()

#%% more readable barplot
# make table, parking count
parking_count = data['parking'].value_counts()
# make categories
parking_categories = ['No parking','Parking']
fig,ax = plt.subplots()
ax.bar(parking_categories,parking_count)
plt.show()

#%% make table, city count (also works with strings)
city_count = data['city'].value_counts()
city_categories = data['city'].unique()

fig, ax = plt.subplots()
ax.bar(city_categories,city_count)
plt.show()

#%% change colours

fig, ax = plt.subplots()
ax.bar(city_categories,city_count,color=['#6744ad','#9f44ad'])
plt.show()

#%% statistical tests (difference of mean price for oslo and mean price for trondheim)
# null hypothesis is that of no difference
# if the p-value is less than 0.05 then there is a significant difference in means
from scipy import stats
prices_oslo = data['price'][data['city']=='oslo']
prices_trondheim = data['price'][data['city']=='trondheim']
t_statistic, p_value = stats.ttest_ind(prices_oslo, prices_trondheim)

# this is also how you can print some informative text to screen
# use print(f'') and put variables in curly brackets {} and text outside the curly brackets.
print(f't-stat: {t_statistic}')
print(f'p-value: {p_value}')

#%% correlation 
# can use the .corr() method for dataframes
# must drop the string variable first with the .drop() method
print(round(data.drop(columns='city').corr(),2))

#%% correlation of a subset
print(data[['price','square_meters','bedrooms']].corr())

#%% only keep 2 decimals for easier reading
print(round(data[['price','square_meters','bedrooms']].corr(),2))

#%% make cross tables to count combinations of groups
# works with variables which has categories, not continuous numbers
pd.crosstab(data['city'],data['parking'])

#%% add bedrooms to the crosstable
pd.crosstab([data['city'], data['bedrooms']], data['parking'])

#%% simple regression
import statsmodels.api as sm
# in Python we have to:
# 1) select the variables we would like to work with
# 2) add a constant term to the data
# we can do both in one operation like so:
x = sm.add_constant(data['square_meters'])
y = data['price']

# now fit the model
reg_sim = sm.OLS(y, x).fit()

# and print the results
print(reg_sim.summary())

#%% get residuals
reg_sim_residuals = reg_sim.resid

#%% plot residuals
fig, ax = plt.subplots()
ax.plot(reg_sim_residuals,'o')
plt.show()

#%% residuals vs the x variable
# check if there is some pattern (in that case there is unused information and a transformation is necessary)
fig, ax = plt.subplots()
ax.scatter(reg_sim_residuals, data['square_meters'])
plt.show()

#%% transform the variables to account for non-linearity
# take logarithm of both variables
# we have to make a new x and y dataset
# the math module only works with individual numbers
# must import numpy, as it is made to work with series of numbers

x = np.log(data['square_meters'])
x = sm.add_constant(x)
y = np.log(data['price'])

reg_sim_log = sm.OLS(y,x).fit()

print(reg_sim_log.summary())

#%% add a square of square meters
x = np.square(data['square_meters'])
x = sm.add_constant(x)
y = data['price']

reg_sim_square = sm.OLS(y,x).fit()

print(reg_sim_square.summary())

#%% multiple regression
# the last column is the same as the penultimate column (perfect multicolinearity) and is not estimated
x = data.drop(columns=['price','city'])
x = sm.add_constant(x)
y = data['price']

reg_mul = sm.OLS(y,x).fit()

print(reg_mul.summary())
#%% only keep the significant variables to get a more robust model
x = data[['square_meters','bathrooms','oslo']]
x = sm.add_constant(x)
y = data['price']

reg_mul = sm.OLS(y,x).fit()

print(reg_mul.summary())

#%% add estimated values to datafame
data['reg_mul_price'] = reg_mul.fittedvalues


# %% let us make a prediction
# the appartment we are looking at has 50 square meters
# it has one bathroom and is not in oslo
# now we can use the coefficients from the model to make the prediction


app_sqm = 50
app_bath = 1
app_oslo = 0

app_price = 2395000 + 60590 * app_sqm + -2465000 * 1 + 1872000 * 0

print(app_price)

