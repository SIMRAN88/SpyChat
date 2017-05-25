print "Hello"

# How to use escape sequences
print "Let\'s get started!"

# Let's start by greeting the spy.
print "Hello, Mr Spy!"
# Ask for the name of the spy.
spy_name = raw_input("Welcome to spy chat,please tell your name: ")

# initialize variable to find the length of the name
spy_name_length = len(spy_name)

# check if name is entered or not
if spy_name_length > 0:
    # greet again with the spy_name by string concatenation
    print "Hello, " + spy_name

    # Ask for spy salutation
    spy_salutation = raw_input("Should I call You Mr or Miss?: ")
    # variable is updated
    # String concatenation(salutation + name)
    spy_name = spy_salutation + " " + spy_name
    print "Alright, " + spy_name + " We need some more information."

else:
    print("Please enter your name and run the program again.")



