import pyfiglet

name = input("Enter your name")
font = pyfiglet.figlet_format(name)
print(font)