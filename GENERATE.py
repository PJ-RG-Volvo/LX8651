import string
import random # define the random module
S = 681  # number of characters in the string
#call random.choices() string module to find the string in Uppercase + numeric data.
ran = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = S))
print("Generated text is : " + str(ran)) # print the random data
