
#   numbers separated with commas will create a tuple
tuple = 122, 789, 893
print(tuple)

#   numbers with _ in sequence will be ignored and considered as digit separators
num = 1_234_567
print(num)

#   all mathematical operations on integers
#   Remember that when operating an integer and a float it will return a float
1 + 2   #   Addition
2 - 1   #   Subtraction
2 * 3   #   Multiplication
9 / 2   #   Floating-point division
9 // 2  #   Floor Division
9 % 2   #   Modulo / Remainder
2**2    #   Exponentiation

#   ! Remember that Python follows the PEMDAS rule and will sometimes be altered by
#   Bitwise and Logical values

#   Converting variables to float and integer by using float() and int() functions vice-versa

#   Boolean variables
#   you can get the equivalent bool value by using the bool() function and treats non-zero
#   numbers as True and zero numbers as False.
print(bool(1))
print(bool(0.0))


#   Strings
#   You can use either single or double quotes and three single quotes for multi-line strings
quote = "'I am Woodrow Fajardo'"
print(quote)

quote = '"My name is Woodrow Fajardo"'
print(quote)

#   Multi-line string
quote = '''I am Thanos the destroyer of worlds
they called me a madman. I will wipe half the universe.
And I call it mercy.'''
print(quote)

#   Escape and Whitespace Characters in strings
#   \n - new line
#   \r - carriage return
#   \t - tab
#   \' - single quote
#   \\ - backslash
print("I am Woodrow\n19 years of age\nFrom the Philippines")


#   Concatenation and Multiplication
quote = 'We won ' + 'together!'
print(quote)

quote = 'Ha' + ('ha' * 5)
print(quote)

#   Offset and Slice
#   Getting a particular char or a sequence of char from a string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   Offset (remember that index starts at 0)
print(alphabet[2])

#   Slice (getting a sequence of char using [:])
#   varname[:]  - gets entire sequence
#   varname[2:] - gets all characters from start until end
#   varname[:2] - gets all character until chosen endpoint
#   varname[2:10] - Start to end
#   varname[2:20:3] - start until endpoint skipping characters set by step [start:end:step]

print(alphabet[2:])
print(alphabet[:2])
print(alphabet[2:10])
print(alphabet[2:20:3])


#   Length len() function (the equivalent to strlen from C)
#   len() function can also be used for tuples, list, sets, arrays and dictionaries
print(len('123456789'))

#   Strip (strips whitespaces or specified characters from the string)
#   strip() - strips characters from both sides (left and right)
#   lstrip() - strips characters from the left
#   rstrip() - strips characters from the right
word = '     Hola&*?'
print(word.strip())
print(word.rstrip('&*?'))
print(word.lstrip())
word = word.strip('&*?')
word = word.lstrip()
print(word)

#   Split and Join function (equivalent to strtok func in C)

#   Split function will separate a string literal into a list
#   If no separator indicated, python will try to use whitespaces to separate values
months = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec'
print(months.split(','))

#   another example using escape sequences
word = '\lorem\nipsum\tdolor\nsit amet'
print(word.split())

#   Join function join() will bring together the list items to form a string value.
groc = ['bread', 'eggs', 'sugar', 'salt']
print('Grocery List:', ', '.join(groc)) # join the list using comma (', ')

#   Replace function replace()
#   takes on 3 arguments (string to be replaced, string to replace, number of times the replacement occur (optional))
dessert = 'chocolate ice cream with chocolate coating'
print(dessert.replace('chocolate', 'vanilla', 1))  # if optional parameter it will change all instances it can find, for this we have 2.

#   Case string
#   capitalize() - capitalize the first word of the string
#   title()      - capitalizes the first letter of each word
#   upper()      - capitalizes all the letters in the string
#   lower()      - converts the letter to lowercase
#   swapcase()   - changes the case from upper to lowercase and vice versa
title = 'noli me tangere'
print(title.capitalize())
print(title.title())
print(title.upper())
print(title.lower())
print(title.swapcase())






