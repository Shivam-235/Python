name = "shivam"
print(name[0])
print(name[1])
print("Lets use a for loop\n")
Project = "Trying to be friend with python"
for character in Project:
    print(character)
print(name[0:6])
print(len(name))
fruit = "banana"
print(fruit[:-3])#Python Interprets len(fruit)-3 i.e[0:2]
print(fruit[:])#Python Interprets len(fruit) i.e[0:6]
#for loops
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabets: #i is a variable
    print(i)
#Strings are immutable
guy = "!!!Shivam!!!!!!!!! is smart"
print(guy.replace("S","s"))
print(guy.upper())      #upper makes the string uppercase
print(guy.lower())      #lower makes the string lowercase
print(guy.rstrip("!"))  #rstrip removes the right side spaces
print(guy.lstrip("!"))  #lstrip removes the left side spaces
print(guy.split(" "))   #split removes the spaces
print(guy.find("Shivam"))#finds the index of the string
quantumphysics = "the future of quantum physics is Bright"
print(quantumphysics.capitalize())#capitalizes the first letter
print(quantumphysics.title())#capitalizes the first letter of every word
print(quantumphysics.swapcase())#swaps the case of the string
print(quantumphysics.count("t"))#counts the number of times the string is repeated
print(quantumphysics.startswith("t"))#checks if the string starts with the given string
print(quantumphysics.endswith("t"))#checks if the string ends with the given string
print(quantumphysics.isalnum())#checks if the string is alphanumeric
print(quantumphysics.isalpha())#checks if the string is alphabetic
print(quantumphysics.isdigit())#checks if the string is a digit
print(quantumphysics.islower())#checks if the string is lowercase
print(quantumphysics.isupper())#checks if the string is uppercase
print(quantumphysics.isspace())#checks if the string is a space
print(len(quantumphysics)) #prints the length of the string
print(len(quantumphysics.center(100)))#centers the string
print(quantumphysics.endswith("of",4, 13))#checks if the string ends with the given string
great = "shivam is great"
print(great.find("is"))#finds the index of the string
print(great.index("is"))#finds the index of the string
print(great.isprintable())#checks if the string is printable
str1 = "  "
print(str1.isspace())#checks if the string is a space
print(great.join("shivam"))#joins the string
print(great.partition("is"))#partitions the string
print(great.istitle())#checks if the string is title