import string
import random

source1 = string.ascii_lowercase
source2 = "!#$%&*+_?@^"
source3 = string.ascii_uppercase

# ask user for a specific length of password
pwd_length = input("\nEnter Password Length (# between 8 and 16):")

pwd_length = int(pwd_length)

# Transform `source1`, `source2` and `source3` into lists
src1,src2,src3 = list(source1), list(source2), list(source3)

# randomize and create password
random.shuffle(src1)
random.shuffle(src2)
random.shuffle(src3)

lowercase = src1[:int(round(0.4*pwd_length))]
symbols = src2[:int(round(0.4*pwd_length))]
uppercase = src3[:int(round(0.4*pwd_length))] 
password = lowercase + symbols + uppercase
random.shuffle(password)

# truncate to specified length
password = "".join(password[:pwd_length])

print("\n")
print("-"*30)
print("password = {}".format(password))

# error checking
print("Assumption checks")
print(".. correct length:", pwd_length == len(password))
print("... has lowercase:", password.upper() != password)
print("... has uppercase:", password.lower() != password)
print("...... has symbol:", not password.isalpha())


