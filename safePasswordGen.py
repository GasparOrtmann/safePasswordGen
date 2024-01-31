import string
import random

#Password length
length = int(input("Insert password length: "))

#Uppercases + digits + punctuation marks
characters = string.ascii_letters + string.digits + string.punctuation

#Generate password with random characters with previous length password set
password = "".join(random.choice(characters) for i in range(length))

print("Password: " + password)