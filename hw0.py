#  BASIC DATA TYPES

## BASICS

### P1.PY
"""

"""
Placeholders
"""

# You're writing a program, and you don't know what your starting value for your 'initial' variable is yet. The program won't run if you leave it blank, but you don't want to forget you need it! Make a workaround.


# This temp variable is just until you figure out what you are doing! Replace it with the apprpriate label ASAP!

temp = something


"""

### P2.PY


"""

"""
Basic Variables
"""

# Create a variable that represents your favorite number, and add a note to remind yourself what this variable represents. Now print it out without re-typing the number.


# Your favorite number is 6, remember? What food is traditionally eaten in the month you celebrate the number 6?
six = 6
turkey = six
print(turkey)


# Create another variable that represents your favorite color, and do the same steps as above.


# The color that all comic sans should be displayed in.
color = "cyan"
comic_sans = color
print(comic_sans)


"""

### P3.PY


"""

"""
String Formatting
"""

# Create a variable that contains the first 4 lines of your favorite song. Add a comment that includes the song title and artist **each on their own line**! Now print out this variable.

# Song name: Part XI  
# Artist: Prequell, Fyfe
part_xi = "If I could be with my life\nI wouldn′t waste anymore time in the nightland\nI've run careless as you find me dancin\nI found my body"
print(part_xi)



"""

## TYPECASTING

### P1.PY


"""

"""
Typcasting w. Integers & Floats
"""

# Convert these numbers into floats and back. Print out each result as well as its data type.

five = 5
zero = 0
neg_8 = -8
neg_22 = -22


# This should convert the variables in lines 84, 85, 86, 87 into floats:
float_five = float(five)
float_zero = float(zero)
float_neg_8 = float(neg_8)
float_neg_22 = float(neg_22)

print(float_five,type(float_five))
print(float_zero,type(float_zero))
print(float_neg_8,type(float_neg_8))
print(float_neg_22,type(float_neg_22))

# This will convert the variables in lines 91, 92, 93, 94 into integers:
int_five = int(float_five)
int_zero = int(float_zero)
int_neg_8 = int(float_neg_8)
int_neg_22 = int(float_neg_22)

print(int_five,type(int_five))
print(int_zero,type(int_zero))
print(int_neg_8,type(int_neg_8))
print(int_neg_22,type(int_neg_22))


"""

### P2.PY


"""

"""
Typcasting w. Strings
"""

# Convert these variables into strings and then back to their original data types. Print out each result as well as its data type. What do you notice about the last one?

five = 5
zero = 0
neg_8 = -8
T = True
F = False


# This step is to check the original types of the variables:
print("")
print("Here are the original variable types:")
print(five,type(five))
print(zero,type(zero))
print(neg_8,type(neg_8))
print(T,type(T))
print(F,type(F))

# This will convert the variables in lines 126, 127, 128, 129, 130 into strings:
string_five = str(five)
string_zero = str(zero)
string_neg_8 = str(neg_8)
string_T = str(T)
string_F = str(F)

print("")
print("Here are the original variables converted into strings:")
print(string_five,type(string_five))
print(string_zero,type(string_zero))
print(string_neg_8,type(string_neg_8))
print(string_T,type(string_T))
print(string_F,type(string_F))

# This will convert the variables in lines 141, 142, 143, 144, 145 into their original type:
int_five = int(string_five)
int_zero = int(string_zero)
int_neg_8 = int(neg_8)
bool_T = bool(string_T)
bool_F = bool(string_F)

# This will inproperly print bool_F as 'True' but I dont know why:
print("")
print("Here are the converted variables reconverted back to their original type, but with an issue with the False boolean:")
print(int_five,type(int_five))
print(int_zero,type(int_zero))
print(int_neg_8,type(int_neg_8))
print(bool_T,type(bool_T))
print(bool_F,type(bool_F))

# This will correct the bool_F error:
bool_F = False

# This will properly print bool_F as 'False':
print("")
print("Here are the converted variables reconverted back to their orignal type with corrected False boolean:")
print(int_five,type(int_five))
print(int_zero,type(int_zero))
print(int_neg_8,type(int_neg_8))
print(bool_T,type(bool_T))
print(bool_F,type(bool_F))

# Is there a better way to make blank lines between these blocks?

"""

### P3.PY


"""

"""
Booleans I - Typecasting w. Numbers
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result.

one = 1
zero = 0


bool_one = bool(one)
bool_zero = bool(zero)

print("")
print("Section A:")
print(bool_one,type(bool_one))
print(bool_zero,type(bool_zero))


# B) Use typecasting to turn the resultant variables from part A into floats. Print the result and the datatype of the result.


float_one = float(bool_one)
float_zero = float(bool_zero)

print("")
print("Section B:")
print(float_one,type(float_one))
print(float_zero,type(float_zero))


# C) Use typecasting to turn the resultant variables from part B back into booleans. Print the result and the datatype of the result.


bool2_one = bool(float_one)
bool2_zero = bool(float_zero)

print("")
print("Section C:")
print(bool2_one,type(bool2_one))
print(bool2_zero,type(bool2_zero))


# C) Use typecasting to turn the resultant variables from part C into integers. Print the result and the datatype of the result.


int_one = int(bool2_one)
int_zero = int(bool2_zero)

print("")
print("Section D:")
print(int_one, type(int_one))
print(int_zero, type(int_zero))


# E) Use typecasting to turn the variable below into a boolean value. Print the result and the datatype of the result.

ten = 10


bool_ten = bool(ten)

print("")
print("Section E:")
print(bool_ten, type(bool_ten))

"""

### P4.PY


"""

"""
Booleans II - Typecasting w. Strings
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result.

one = 1
zero = 0
bool_true = True
bool_false = False


bool_one = bool(one)
bool_zero = bool(zero)

print("")
print("Section A:")
print(bool_one,type(bool_one))
print(bool_zero,type(bool_zero))
print(bool_true,type(bool_true))
print(bool_false,type(bool_false))


# B) Use typecasting to turn the latest values for variables 'one' and 'zero' back into integers. Print the result and the datatype of the result.


int_one = int(bool_one)
int_zero = int(bool_zero)

print("")
print("Section B:")
print(int_one,type(int_one))
print(int_zero,type(int_zero))



# C) Use typecasting to turn the latest values for variables 'bool_true' and 'bool_false' back into boolean values. Print the result and the datatype of the result.


bool2_true = bool(bool2_one)
bool2_false = bool(bool2_zero)

print("")
print("Section C:")
print(bool2_true,type(bool2_true))
print(bool2_false,type(bool2_false))



"""

## OPERATORS

### P1.PY


"""

"""
Integer & Float Operators
"""

# Complete the specified math operations. Do the next operation on the result from the previous operation.

orig_var = 100


print("")
print("Original Variable =",orig_var)


# Add 50

print("")
print("Add 50")
orig_var += 50
print(orig_var)


# Subtract 90


print("")
print("Subtract 90")
orig_var -= 90
print(orig_var)


# Multiply 10


print("")
print("Multiply 10")
orig_var *= 10
print(orig_var)


# Divide 150


# Note type changes from integer to float here.
print("")
print("Divide 150")
orig_var /= 150
print(orig_var)


# Modulus 3


# I think this is saying 4/3=1.333333, and 1/3 of 3 is 1, so 1. 
print("")
print("Modulus 3")
orig_var %= 3
print(orig_var)


"""

### P2.PY


"""

"""
String Operators
"""

# Create two variables, each of which is half of a compound sentence. Do NOT add any punctuation up front. Add the two variables together, and print the result.
## Example compound sentence: "I'll go to the beach today, and I'll go snorkeling."

"""

### P3.PY


"""

"""
Addition I - Numbers & Strings
"""

# Add the below sets of variables together.

# A)
a = 0
b = 2



# B)
c = '0'
d = '2'



# C)
e = "0"
f = 2

"""

### P4.PY


"""

"""
Addition II - Booleans
"""

# Add the below sets of variables together.

# A)
a = True
b = True



# B)
c = False
d = False



# C)
e = True
f = False
