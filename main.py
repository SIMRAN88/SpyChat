from spy_details import spy

# Let's start by greeting.
print"Hello!"

# How to use escape sequences
print "Let\'s get started!"

# Ask the spy whether he wants to continue with the default spy or create a new user
question = "Do you want to continue as" + spy['salutation'] + " " + spy['name'] + "Y/N ?"
existing = raw_input(question)

# add a status message
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred', "Live and Let Die", "Diamonds are forever"]

# friend list to store name,age,rating an is_online
friends = []

#
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
        new_status_message =  raw_input("What status message do you want to see?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above status"))

        # Check if the position exists and then only set it
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if current_status_message:
        print 'Your updated status message is: %s' % current_status_message
    else:
        print 'You did not update your status message'

    return updated_status_message


# function to add a friend to this chat
def add_friend():
    # using a dictionary to add a friend details
    new_friend = {
        'name': ' ',
        'salutation': ' ',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['name'] + " " + new_friend['salutation']

    new_friend['age'] = raw_input("Age?")
    new_friend['age'] = int(new_friend['age'])

    new_friend['rating'] = raw_input("Spy rating?")
    new_friend['rating'] = float(new_friend['rating'])

    # Add a friend of correct age and equal or higher rating
    if len(new_friend['name']) > 0 and 12 < new_friend['age'] < 50 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        # age is less than 12
        if new_friend['age'] < 12:
            print("Sorry , the friend is too young to become a spy!")
        # age is greater than equal to 50
        elif new_friend['age'] >= 50:
            print("Sorry , the friend is too old to be a spy!")



    return len(friends)

def select_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' %(item_number +1,friend['name'],friend['age'],friend['rating'])

        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def start_chat(spy):
    current_status_message = None

    # updated variable
    spy['name'] = spy['salutation'] + " " + spy['name']
    # Age cannot be less than 12 or greater than 50
    if 12 < spy['age'] < 50:

        # Authentication complete
        # Show a message with all te spy details
        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(
            spy['rating']) + " Proud to have you on board"

        # Can be done in this way also print "Authentication complete. Welcome %s, age: %d and rating of: %.2f.Proud
        # to have you on board" % (spy_name, spy_age, spy_rating)

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                # set a status
                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                # add a friend
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                # select from a friend to chat with
                elif menu_choice == 3:
                    index = select_friend()
                    print index
                else:
                    show_menu = False

    else:
        # age is less than 12
        if spy['age'] < 12:
            print("Sorry , you are too young to become a spy!")
        # age is greater than equal to 50
        elif spy['age'] >= 50:
            print("Sorry , you are too old to be a spy!")


# if the user chooses the default spy
if existing.upper() == "Y":
    # start the chat function is called
    start_chat(spy)
# the user wants to add a new user
elif existing.upper() == "N":
    # declare variables using a dictionary
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    # Ask for the name
    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # Check if the name is entered or not
    if len(spy['name']) > 0:
        # ask for the salutation
        spy['salutation'] = raw_input("What should we call you Mr or Miss?")

        # Ask for the age of the spy
        spy['age'] = raw_input("please enter your age: ")
        # raw input always gives a string to typecast age to int.
        spy['age'] = int(spy['age'])
        # Age cannot be less than 12 and greater than 50
        # nested if
        if 12 <= spy['age'] < 50:
            print("Welcome to Spy community")

            # Ask for spy_rating
            spy['rating'] = raw_input("Please enter your spy rating: ")
            # raw input always gives a string to typecast rating to float.
            spy['rating'] = float(spy['rating'])

            # conditions to pass comments according to the spy_rating.
            if spy['rating'] > 4.5:
                print "Great Ace!"
            elif 3.5 <= spy['rating'] <= 4.5:
                print "You are one of the good ones!"
            elif 2.5 <= spy['rating'] <= 3.5:
                print "You can always do better."
            else:
                print "We will get someone to help you."

            # Make the spy come online
            spy['is_online'] = True

            # Call the start_chat function to start(the function will authenticate the user)
            start_chat(spy)
    else:
        print("Please enter a valid name")
