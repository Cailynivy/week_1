##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
'''
year1 = input("Year 1:")
year2 = input("Year 2:")
dif = year2 - year1
print ("Difference: {dif}")
'''
#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
'''
farenheit = int(input("Farenheit:"))
celsius = (farenheit - 32) * 5 / 9
print("Celsius:" , celsius)
'''

#
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''

usd = int(input("USD:"))
er = 0.97      
eu = usd * er 
print ("EU:" , eu)

##### ASSIGNMENT ENDS HERE #####