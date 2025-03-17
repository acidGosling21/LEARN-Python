
#   In programming, one of the common analogies about how computers handles 
#   data is with the idea of a shelf and a bunch of objects. Think a computer's
#   memory as one big shelf and data as objects stored on and retrieved from this
#   shelf. Python follows this "data as objects" analogy and treats data accordingly.
#   Remember, Python is a dynamically-typed programming language.

x = 'Jose'
y = 5

#   id() function will return a memory address of the object.
print(id(x))
print(id(y))

#   data types 
#   ! Use type() function to check an object's data type.
#   Non-mutable object data types:
int = 13 
print(type(float))

float = 0.1
print(type(float))

str = 'Hello World'
print(type(str))

bool = True
print(type(bool))

list = ['Seth', 'Precious', 'Garcia']   # mutable object data type (sequence of objects)
print(type(list))

tuple = (3, 6, 9)       # non-mutable object data type (sequence of objects)
print(type(tuple))

set = set(['saba', 'chico', 'atis'])    # mutable object data type (unordered set of objects)
print(type(set))

frozenset = frozenset(['Maria', 'Fatima', 'Fajardo'])   # non-mutable object data type (unordered set of objects)
print(type(frozenset))

dict = {'martial art':'kali',
        'hero':'rizazl',
        'city':'Cebu'}          # mutable object data type
print(type(dict))

#   Mutability?



