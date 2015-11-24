#Ex 15: Reading Files
#imports the argv module from the system
from sys import argv

# # assigns new arguments from the command line
# # argv[0] is the script 'ex15.py' pathname, 
# # argv[1] is the 'ex15_sample.txt' input file
# script, filename = argv

filename = raw_input("Enter filename: ")
#assigns the argv[1] object to the variable txt
txt = open(filename)

#prints the filename of argv[1]
print "Here's your file %r:" % filename
#prints the contents of txt with the function read
print txt.read()
txt.close()

# #print statement
# print "Type the filename again:"
# #prompt for another filename to assign to file_again
# file_again = raw_input("> ")

# #assigns the (raw_input)file_again object 
# #to the variable txt_again
# txt_again = open(file_again)

# #prints the txt_again object via read function
# print txt_again.read()
# txt_again.close()