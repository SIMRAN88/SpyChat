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

    # declare new variables
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    # Ask for the age of the spy
    spy_age = raw_input("please enter your age: ")
    # raw input always gives a string to typecast age to int
    spy_age = int(spy_age)

    # Age cannot be less than 12 and greater than 50
    # nested if
    if 12 <= spy_age < 50:
        print("Welcome to Spy community")

        # Ask for spy_rating
        spy_rating = float(raw_input("Please enter your spy rating: "))

        if spy_rating > 4.5:
            print "Great Ace!"
        elif 3.5 <= spy_rating <=4.5:
            print "You are one of the good ones!"
        elif 2.5 <= spy_rating <=3.5:
            print "You can always do better."
        else:
            print "We will get someone to help you."

        # Make the spy come online
        spy_is_online = True

        # Authentication Complete
        print "Authentication Complete.Welcome %s,age: %d,rating : %.2f.Proud to have you on board." %(spy_name,spy_age,spy_rating)

    else:
        print("You are not of the proper age to enter the spy community!")

else:
    print("Please enter your name and run the program again.")



