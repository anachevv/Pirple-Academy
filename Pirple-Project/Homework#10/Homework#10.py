"""
BUILT-IN FUNCTIONS:
"""

"""
Function abs(x)

The function returns the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.
"""

#If we have a ball and a player whose positions are:
ballPosition = -8
playerPosition = 28
#How could we calculate the distance between them?
#By using the abs(x) function!
distance = abs(ballPosition) + abs(playerPosition)
print(distance)

"""
Function all(iterable)

The function returns True if all elements of the iterable are true(or if the iterable is empty)
"""

#In case we want to check if all the elements are the same:
x = [True, True, True]
y = [True, True, False]
z= [False, False, False]

print(all(x))
#All the element are True
print(all(y))
#One of the elements is not True
print(all(z))
#None of the elements is True

"""
Function any()

The function returns True if any element of the iterable is true. If the iterable is empty, returns False.
"""

#In case we want to check if any element of the iterable is true:
#We use the above case
print(any(x))
print(any(y))
print(any(z))

"""
Function ascii(object)

As repr(), returns a string containing a printable representation of an object, but espace the non-ASCII characters in the string returned by repr() using x, u or U escapes. This generates a string similar to that returned by repr() in Python 2.
"""

#How does ascii(object) function work:
ascii("béné")
print(ascii("béné"))

"""
Function bin(x)

Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer. Some examples:
"""

#Example
bin(3)
print(bin(3))

"""
If prefix "Ob" is desired or not, we can use either of the following ways.
"""

#Normal way
format(14, "#b"), format(14, "b")
print(format(14, "#b"), format(14, "b"))

#Short way
f'{14:#b}', f'{14:b}'
print(f'{14:#b}', f'{14:b}')

"""
Function breakpoint(*args,**kws)

This function drops you into the debugger at the call site.
"""

#Example
""" for i in range(10):
    print("i= ", i)
    if i ==5:
        #import pdb
        breakpoint()
print(i) """
#We can continue the counting by typing c(or continue) in the terminal
#Before we continue working with the next function, we have to press c(continue) so the last function get done.

"""
Functions: 1) bytes, 2) bytearray

1) Returns a new "bytes" object, which is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.
2) Returns a new array of bytes. The bytearray class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences
"""

#Example
bytes([1,2,3])
print(bytes([1,2,3]))
bytearray([1,2,3])
print(bytearray([1,2,3]))


"""
Function callable()

Returns True if the object argument appears callable, and False if not.
Functions are callables, classes are callables, methods are callables, instances of classes can even be turned into callables.
"""

#Example
callable("Hey")
print(callable("Hey"))
#It returns False because there is not a "type" into the parentheses.
#Example#2
callable(type("Hey"))
print(callable(type("Hey")))
#Now it returns True

"""
Functions: 1) chr(), 2) ord()

1) Returns the string representing a character whose Unicode code point is the integer i.
The valid range for the argument is from 0 through 1,114,111.
2) Given a string representing one Unicode character, returns an integer representing the Unicode code point of that character.
"""

#chr() example:
chr(0)
print(chr(0))
#it must returns '\x00'
#Now, ord() example:
ord('\x00')
print(ord('\x00'))

"""
Function @classmethod

Transform a method into a class method.
A class method receives the class as implicit first argument, just like an instance method receives the instance.
"""

#Example
class Car:
    def __init__(self, Features):
        self.Features = Features

    def __repr(self):
        return f"Car (Car{self.Features})"

    @classmethod
    def truck(cls):
        return cls(["4x4", "Big Tires"])

newCar = Car.truck()
print("newCar", newCar.__dict__)
#If there is missing ".__dict__", it will returns 0x0000020B18AB7B50. So let we add ".__dict__" and see what will happen.


"""
Function compile()

Compile the source into a code or AST object. When compiling a string with multi-line code in "single" or "eval" mode, input must be terminated by at least one newline character. THis is to facilitate detection of incomplete and complete statements in the code module.
"""

#String example
""" x = "5"
code = compile(x == "5", "", "eval")
print(type(code))
result = eval(code)
print(result)

#Bytes example
x = 5
bytes_str = bytes("x = 5", "utf-8")
print(type(bytes_str))
code = compile(bytes_str, "", "eval")
result = eval(code)
print(result) """


"""
Function class complex()

Returns a complex number with the vale real + imag*1j or convert a string or a number to complex number.
"""

#Example
complex(1)
print(complex(1))
complex(1, 2)
print(complex(1, 2))
#etc.


"""
Function delattr(object, name)

The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it.
"""

#Example
class Jeep:
    hp = 500
    model = "G-class"

print("Jeep", Jeep.__dict__)
delattr(Jeep, "hp")
print("Jeep after", Jeep.__dict__)



"""
Function dict()
Create a new dictionary. The dict object is the dictionary class.
"""

#Example
dict(a=1, b=2)
print(dict(a=1, b=2))


"""
Function dir([object])

Without arguments, returns the list of names in the current local scope. With an argument, attempts to return a list of valid attributes for that object. The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

    If the object is a module object, the list contains the names of the module’s attributes.

    If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.

    Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.
"""


#Example
class Jeep:
    hp = 500
    model = "G-class"

print(dir(Jeep))


"""
Function divmod(a,b)

Takes two (non complex) numbers as arguments and returns a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply.
"""

#Example
divmod(10,2)
print(divmod(10,2))
divmod(10,13)
print(divmod(10,13))
divmod(2,3)
print(divmod(2,3))
divmod(3,1)
print(divmod(3,1))


"""
Function enumerate

Returns an enumerate object. Iterable must be a sequence, an iterator, or some other object which supports iteration.
"""

#Example
countries = ["Bulgaria", "France", "Switzerland", "Austria"]
list(enumerate(countries))
print(countries)

#Enumerate in loops
for i, j in enumerate(["Bulgaria", "France", "Switzerland", "Austria"], 1):
    print(i, j)


"""
Function eval
The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.
"""

#Example
eval("-1")
print(eval("-1"))
eval("5 * -6")
print(eval("5 * -6"))


"""
Function exec(object[,globals[,locals]])

This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section “File input” in the Reference Manual).
"""

#Example
exec("print(1)")
exec("print(max(10,1))")
exec("print(min(10,1))")


"""
Function filter(function,iterable)

Constructs an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
"""

#Example
ages = [0,5,17,18,24]
def myFunc(x):
    return x>= 18

print(list(filter(myFunc, ages)))

#If we change this return with "text", e.g, we return "Hey":
ages = [0,5,17,18,24]
def myFunc(x):
    return "Hey"

print(list(filter(myFunc, ages)))


"""
Function float([x])

Returns a floating point number constructed from a number or string x.

If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More precisely, the input must conform to the following grammar after leading and trailing whitespace characters are removed.
"""

#Example
float("1")
print(float("1"))
float(333)
print(float(333))


"""
Function format(value[format_spec])

Converts a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.
"""

#Example
format(5, )
print(format(5, ))
format(5, "%")
print(format(5, "%"))
format(5, ".1%")
print(format(5, ".1%"))


"""
Function frozenset([iterable])

Returns a new frozenset object, optionally with elements taken from iterable.
"""

#Example
a = frozenset()
print(a)
a = frozenset([1,2,3])
print(a)
a = frozenset("HELLO")
print(a)

"""
Function getattr(object, name[,default])

Returns the value of the named attribute of object. Name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute.
"""

#Example
class Jeep:
    hp = 500
    model = "G-class"

print(getattr(Jeep, "hp"))
print(getattr(Jeep, "model"))


"""
Function globals()

Returns a dictionary representing the current global symbol table. Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).
"""


#Example
globals()
print(globals())


"""
Function hasattr(object, name)

The arguments are an object and a string. The result is True if the string is the name of one of the object's attributes, and False if not.
"""

#Example
class Jeep:
    hp = 500
    model = "G-class"

print(hasattr(Jeep, "hp"))
print(hasattr(Jeep, "engine"))


"""
Function hash()

Returns the hash value of the object(if it has one). Hash values are integers.  They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
"""

#Example
hash(6)
print(hash(6))
hash("6")
print(hash("6"))
hash(6.0)
print(hash(6.0))


"""
Function help([object])

Invokes the built-in help system. Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.
"""

#Example
""" help()
help("math")
print(help("math"))
 """

"""
Function hex()

Converts an integer number to a lowercase hexadecimal string prefixed with "0x". If x is not a Python int object, it has to define an __index__() method that returns an integer.
"""

#Example
hex(1)
print(hex(1))
hex(10)
print(hex(10))
hex(15)
print(hex(15))
hex(20)
print(hex(20))
float.hex(1.0)
print(float.hex(1.0))

"""
Function id(object)

Returns the "identify" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
"""

#Example
id(1)
print(id(1))
a = 6
b = 6
a == b
print(id(a), id(b))


"""
Function input([prompt])

If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.
"""

#Example
""" s = input("---> ")
print(s)
 """

"""
Function isinstance(object, classinfo)

Returns True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples), returns True if object is an instance of any of the types.
"""

#Example
isinstance("hey", str)
print(isinstance("hey", str))
isinstance("hey", int)
print(isinstance("hey", int))


"""
Function issubclass(class, classinfo)

Returns True if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked.
"""

#Example
class Car:
    pass
class Toyota(Car):
    pass
class ToyotaSupra(Toyota):
    pass

print(issubclass(Toyota, (Car, int, str)))
#if "Car" is missing above, it will return False
print(issubclass(Toyota, (int, str)))


"""
Function iter(object[,sentinel])

Returns an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0).
"""

#Example
a = iter(["hey", "car", "python", 100])
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


"""
Function locals()
Updates and returns a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary.
"""

#Example
print(globals())
print(locals())
print(globals() is locals())

print(globals() is locals())

def printNames():
    name = "Annie"
    print("Name: ", name)

printNames()


"""
Function map(function, iterable, ...)

Returns an iterator that applies function to every item of iterable, yielding the results.  If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted.
"""

#Example
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x**2

sq_nums = map(square, numbers)
print(type(sq_nums))
for num in sq_nums:
    print(num)


"""
Function max(iterable, *[,key, default])
max(arg1, arg2, *args[,key])

Returns the largest item in an iterable or the largest of two or more arguments.If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned. There are two optional keyword-only arguments. The key argument specifies a one-argument ordering function like that used for list.sort(). The default argument specifies an object to return if the provided iterable is empty.
"""

#Example
a = max([1,2,3,4,5,6,7,8,9,10])
print(a)
b = max([], default = 100)
print(b)
c = max("apple", "dog")
print(c)
d = max("human", "alien")
print(d)
#I knew it :D


"""
Function memoryview(object)

    Returns a “memory view” object created from the given argument. See Memory Views for more information.
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
Returns the smallest item in an iterable or the smallest of two or more arguments.
"""

#Example
a = b"Hey"
print(type(a))
print(memoryview(a))
print(type(memoryview(a)))
a = bytearray(b"hey")
print(a)
b = memoryview(a)
print(b.obj)


"""
Function min(iterable, *[,key, default])
min(ar1, agr2, args*[,key])
Returns the smallest item in an iterable or the smallest of two or more arguments.
"""

#Example
a = min([1,2,3,4,5,6,7,8,9,10])
print(a)
b = min([100,200,300,400,500,600,700,800,900,1000])
print(b)
c = min("hey", "hola", "bonjour", "здравей", "привет")
print(c)


"""
Function next(iterator[,default])

Retrieves the next item from the iterator by calling its __next__() method. f default is given, it is returned if the iterator is exhausted.
"""

#Example
a = iter(["Bonjour", "comment", "ça ", "va", "?"])
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


"""
Function object()

Returns a new featureless object. Object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.
"""

#Example
o = object()
print(o)
print(type(o))
print(dir(o))
a = object()
print(a)
b = object()
print(b)
print(a == b)
print(a is b)


"""
Function oct(x)

Converts an integer number to an octal string prefixed with "0o". The result is a valid Python expression.
"""

#Example
print(oct(1))
print(oct(2))
print(oct(8))
print(oct(9))


"""
Function open(file,mode="r", buffering = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None)

Opens file and returns a corresponding file object. 
Modes:
"r" - open for reading(default)
"w" - open for writing, truncating the file first
"x" - open for exclusive creation, failing if the file already exists
"a" - open for writing, appending to the end of the file if it exists
"b" - binary mode
"t" - text mode(default)
"+" - open for updating(reading and writing)
"""

#Example
""" file = open("idk.txt", mode="r", buffering = -1, encoding = None, errors = None, newline = None, closefd = True, opener = None)

print("writing 'bro'...")
file.write("bro")
 """

"""
Function pow(base, exp[,mod])

Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.
"""

#Example
print(5 ** 1)
print(5 ** 2)
print(pow(5,2))
print(pow(100,2))
print((5 ** 2)% 12)
print(pow(5,2,12))


"""
Function property(fget = None, fset = None, fdel = None, doc = None)

Return a property attribute.

fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.
"""

#Example
class Car:
    def __init__(self, name):
        self.name = name

@property
def name(self):
    print("in the getter")
    return self._name

@name.setter
def name(self, name):
    print("in the setter")
    if len(name) > 6:
        self.name = name

@name.deleter
def name(self, name):
    print("in the deleter")
    del self.name

my_car = Car("Toyota")
print("my_car.name", my_car.name)
""" my_car.name = "idk" """
#"my_car.name = "idk"
print("my_car.name", my_car.name)
#Let's see what happens if "my_car.name" has more than 6 letters:
my_car.name = "idkbruh"


"""
Function repr(object)

Return a string containing a printable represention of an object.  For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object.
"""

#Example
print(str(3) == str("3"))
print(repr(3) == repr("3"))
from decimal import Decimal
a = Decimal(1.25)
print(a)
print(str(a))
print(repr(a))


"""
Function reversed(seq)

Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
"""

#Example
my_list = [1,2,3,4,5]
for i in reversed(my_list):
    print(i)


"""
Function round(number[,ndigits])

Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
"""

#Example
print(round(1.25))
print(round(2.5))
print(round(3.6))


"""
Function set([iterable])

    Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types — set, frozenset for documentation about this class.

    For other containers see the built-in frozenset, list, tuple, and dict classes, as well as the collections module.
"""

#Example
a = [1,2,3,4,4,4,4,4,5,5,5,5,5]
print(set(a))
print(list(set(a)))
a = {1,2,3,4,5,6,7,8,9}
a.add(10)
print(a)
a.remove(2)
print(a)


"""
Function setattr(object,name,value)

This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
"""

#Example
class Jeep:
    hp = 500
    model = "G-class"

setattr(Jeep, "wheels", "Winter tires")
print(getattr(Jeep, "wheels"))


"""
Function slice(stop)
slice(start,stop[,step])

Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). 
"""

#Example
list = (a,b)
b = slice(2)
print(b)
print(type(b))
""" print(a[b]) """


"""
Function sorted(iterable, *,key=None, reverse=False)

Return a new sorted list from the items in iterable.

Has two optional arguments which must be specified as keyword arguments.

key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
"""

#Example
a = ["c","a","b"]
print(sorted(a))
b = [1,3,2,5,4,7,6,9,8,11,10,13,12]
print(sorted(b))
c = [-1,2,-3,4,-5]
print(sorted(c))


"""
Function @staticmethod

Transform a method into a static method.

A static method does not receive an implicit first argument. 
"""

#Example
class Car:
    def my_instance_method(self):
        return "my_instance_method!!!", self

    @classmethod
    def my_class_method(cls):
        return "my_class_method!!!",cls

    @staticmethod
    def my_static_method():
        return "my_static_method!!!"


"""
Function sum(iterable/,start=0)

Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.
"""

#Example
a = (1,2,3)
b = (1,2,3,4,5,6)
c = (1,2,3,4,5,6,7,8,9)
print(sum(a))
print(sum(b))
print(sum(c))
print(sum([5,5,5]))
print(sum([3,3,3], 100))


"""
Function super([type[,object-or-type]])

Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

The object-or-type determines the method resolution order to be searched. The search starts from the class right after the type.
"""

#Example
class Parent:
    def __init__(self, txt):
        self.message = txt
        self.new = True

    def printmessage(self):
        print(self.message)

class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)

x = Child("Welcome!")
x.printmessage()


"""
Function tuple([iterable])

Rather than being a function, tuple is actually an immutable sequence type.
"""

#Example
print(tuple())
a = tuple()
print(a)
print(type(a))
print(tuple([1,2,3,4,5,6,7,8,9,10]))
print(tuple({1,2}))


"""
Function vars([object])

Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
"""

#Example
print(vars())
class Car:
    speed = 100

print(Car)
print(vars(Car))


"""
Function zip(*iterables)

Make an iterator that aggregates elements from each of the iterables.
"""

#Example
list_1 = ["a", "b", "c", "d"]
list_2 = ["aa", "bb", "cc", "dd"]
list_3 = ["aaa", "bbb", "ccc", "ddd"]
print( dict(zip(list_1, list_2)) )


"""
Function __import__(name,globals=None,locals=None,fromlist=(),leve=0)

This function is invoked by the import statement. It can be replaced (by importing the builtins module and assigning to builtins.__import__) in order to change semantics of the import statement, but doing so is strongly discouraged as it is usually simpler to use import hooks (see PEP 302) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use.
"""

#Example
import os
print(os)
os1 = __import__("os")
print(os1)
m = __import__("math")
print(m)
print(m.fabs(-10))


"""
This is my sample code.
"""