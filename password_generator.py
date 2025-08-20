# SECURE PASSWORD GENERATOR

# This proyect aims to generate Secure Password (with Python)
# The user chooses the password length

# Import necessary libraries for password generation
import random
import string

# The user is asked for the length of the password 
length = int(input("Enter the desired password length: "))

# Librarie String is used to get all the characters that can be used in the password: uppercase, lowercase + punctuation + numbers
characters = string.ascii_letters + string.punctuation + string.digits

# Opcional: print to check what characters can be used in the password
print("Characters available for password generation:", characters)

# Library Random is used to generate the password using the specified length (for) and randomly chosen characters (method choice)
password = ''.join(random.choice(characters) for i in range(length))   

# Print the new password
print("The generated password is:", password) 
