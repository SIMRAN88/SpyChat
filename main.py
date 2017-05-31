from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

# Let's start by greeting.
print "Hello!"

# How to use escape sequences
print "Let\'s get started!"

# Ask the spy whether he wants to continue with the default spy or create a new user
question = "Do you want to continue as" + spy_salutation + " " + spy_name + "Y/N ?"
existing = raw_input(question)

# add a status message
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred',"Live and Let Die","Diamonds are forever"]

# list to store the name of friends
friends_name = []
# list to store the age of friends
friends_age = []
# list to store the rating of friends
friends_rating = []
# list to store whether the friend is online or not
friends_is_online = []


def add_status(current_status_message):
    updated_status_message = None

    # check if current status message is set or not
    if current_status_message is not None:
        print 'Your current status message is %s \n' % current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    # Asking if the user wants to select a default status or a custom one
    default = raw_input("Do you want to select from the older status (y/n)? ")

    # .upper() converts from any case to upper case
    if default.upper() == "N":

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above status"))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You did not update your status message'

    return updated_status_message


# function to add a friend to this chat
def add_friend():
    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")
    new_age = int(new_age)

    new_rating = raw_input("Spy rating?")
    new_rating = float(new_rating)

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None

    # updated variable
    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
            spy_rating) + " Proud to have you onboard"

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                else:
                    show_menu = False
    else:
        print("you are not of the correct age to be a spy")

# if the user chooses the default spy
if existing.upper() == "Y":
    # start the chat function is called
    start_chat(spy_name, spy_age, spy_rating)
# the user wants to add a new user
elif existing.upper() == "N":
    # declare variables
    spy_name = " "
    spy_salutation = " "
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    # Ask for the name
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # Check if the name is entered or not
    if len(spy_name) > 0:
        # ask for the salutation
        spy_salutation = raw_input("What should we call you Mr or Miss?")

        # Ask for the age of the spy
        spy_age = raw_input("please enter your age: ")
        # raw input always gives a string to typecast age to int.
        spy_age = int(spy_age)
        # Age cannot be less than 12 and greater than 50
        # nested if
        if 12 <= spy_age < 50:
            print("Welcome to Spy community")

            # Ask for spy_rating
            spy_rating = raw_input("Please enter your spy rating: ")
            # raw input always gives a string to typecast rating to float.
            spy_rating = float(spy_rating)

            # conditions to pass comments according to the spy_rating.
            if spy_rating > 4.5:
                print "Great Ace!"
            elif 3.5 <= spy_rating <= 4.5:
                print "You are one of the good ones!"
            elif 2.5 <= spy_rating <= 3.5:
                print "You can always do better."
            else:
                print "We will get someone to help you."

            # Make the spy come online
            spy_is_online = True

            # after the variable shave been updated authenticate the user.
            # Authentication Complete
            # print "Authentication Complete.Welcome %s,age: %d,rating : %.2f.Proud to have you on board." % (
            # spy_name, spy_age, spy_rating)

            # Call the start_chat function to start(the function will authenticate the user)
            start_chat(spy_name, spy_age, spy_rating)

        # age is less than 12
        elif spy_age < 12:
            print("Sorry , you are too young to become a spy!")
        # age is greater than equal to 50
        elif spy_age >= 50:
            print("Sorry , you are too old to be a spy!")


    else:
        print("Please enter a valid name")
