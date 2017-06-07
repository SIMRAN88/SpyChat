from spy_details import spy, Spy, friends, ChatMessage
from steganography.steganography import Steganography
from colorama import init
from termcolor import colored

# to initialize the colorama
init()

# adding default status messages
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred', "Live and Let Die", "Diamonds are forever"]

# Let's start by greeting.
print"Hello!"

# How to use escape sequences
print "Let\'s get started!"

# Ask the spy whether he wants to continue with the default spy or create a new user
question = "Do you want to continue as" + spy.salutation + " " + spy.name + "Y/N ?"
existing = raw_input(question)

# Adding a status
def add_status():

    # in the beginning no status message
    updated_status_message = None

    # check if current status message is set or not
    if spy.current_status_message is not None:
        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    # Asking if the user wants to select a default status or a status which is already present
    default = raw_input("Do you want to select from the older status (y/n)? ")

    # A spy wants to add another status
    # .upper() converts from any case to upper case
    if default.upper() == "N":
        # ask the user to enter a new status
        new_status_message =  raw_input("What status message do you want to see?")

        # if valid status message is entered
        if len(new_status_message) > 0:
            # in the existing status list add the new status
            STATUS_MESSAGES.append(new_status_message)
            # variable update
            updated_status_message = new_status_message

    # A spy wants to choose from the existing status
    elif default.upper() == 'Y':

        # to give an index number to the statuses
        item_position = 1

        # to show all the default statuses so that the user can select
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        # ask the user which index of the list he wants to choose.
        message_selection = int(raw_input("\nChoose from the above status"))

        # Check if the position exists and then only set it
        if len(STATUS_MESSAGES) >= message_selection:
            # variabale update
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    # when the user chooses neither yes nor no
    else:
        print 'The option you chose is not valid! Press either y or n.'

    # when the status message is updated
    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    # when it is not updated
    else:
        print 'You did not update your status message'

    # the updated message will be read
    return updated_status_message


# function to add a friend to this chat
def add_friend():
    # using the class spy
    new_friend = Spy(" ", " ", 0, 0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.name + " " + new_friend.salutation

    # ask for the age of the friend
    new_friend.age = raw_input("Age?")
    # Type casting to integer
    new_friend.age = int(new_friend.age)

    # Ask for the rating of the friend
    new_friend.rating = raw_input("Spy rating?")
    # Type casting to float
    new_friend.rating = float(new_friend.rating)

    # Add a friend of correct age and equal or higher rating
    # valid name of strings must be entered
    if len(new_friend.name) > 0 and new_friend.name.isdigit()== False and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating:
        # after the conditions are satisfied the friend will be added
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print("Sorry , the friend cannot be a spy!")

    # The no of friends the spy has will be returned.
    return len(friends)

# Function to select a friend from the friends list
def select_friend():
    # indexing the position of a friend
    item_number = 0

    # To select a friend with the indexing
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' %(item_number + 1, friend.name, friend.age, friend.rating)

        item_number = item_number + 1

    # Ask the user which friend he want to have a chat with
    friend_choice = raw_input("Choose from your friends")
    # The friend will be selected
    friend_choice_position = int(friend_choice) - 1

    # returns the selected friend to perform the options
    return friend_choice_position

# Function to send a secret message
def send_message():

    # select a friend to whom you want to send a message
    friend_choice = select_friend()

    # Select the image in which you want to write a secret message
    original_image = raw_input("What is the name of the image?")
    # the output path of the image where the message is stored
    output_path = "output.jpg"
    # write the secret message
    text = raw_input("What do you want to say? ")
    # The library steganography that helps to encode the message
    Steganography.encode(original_image, output_path, text)

    # The text message wil be stored in chat messages
    new_chat = ChatMessage(text,True)

    # Along with the name we add the message
    friends[friend_choice].chats.append(new_chat)

    # After the encoding is done the message is ready.
    print "Your secret message image is ready!"


# Function to send a message of help in case of an emergency
def send_message_help():
    # Select the friend who had sent the emergency message
    friend_choice = select_friend()
    # Send the helping message text to the friend in emergency
    text = "I am coming to save you. Do not worry "
    # The message will be added in the chat
    new_chat = ChatMessage(text,True)
    # Add the message to the one who said.
    friends[friend_choice].chats.append(new_chat)


# Read the secret message sent by a friend.
def read_message():

    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    # error handling if a secret message is present or not
    try:
        secret_text = Steganography.decode(output_path)
        print "The secret message you read is",
        print (colored(secret_text,'red'))
        words = secret_text.split()
        if "SOS" in words or "Save" in words or "Help" in words:
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow'))
            print (colored("The friend that sent this message needs an emergency.", 'green'))
            print (colored("PLease help your friend by sending a helping message.", 'green'))
            print (colored("Select that friend to send him a helping message.", 'red'))
            send_message_help()
            print(colored("You have sent a message to help your friend.",'magenta'))
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
        else:
            new_chat = ChatMessage(secret_text, False)
            friends[sender].chats.append(new_chat)
            print "Your secret message has been saved!"
    # TypeError handling
    except TypeError:
        print "Nothing to decode from the message"



def start_chat(spy):

    # updated variable
    spy.name = spy.salutation + " " + spy.name
    # Age cannot be less than 12 or greater than 50
    if 12 < spy.age < 50:

        # Authentication complete
        # Show a message with all te spy details
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you on board"

        # Can be done in this way also print "Authentication complete. Welcome %s, age: %d and rating of: %.2f.Proud
        # to have you on board" % (spy.name, spy.age, spy.rating)

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    # set the status calling the
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends
                elif menu_choice == 3:
                    send_message()
                else:
                    show_menu = False

    else:
        # age is less than 12
        if spy.age <= 12:
            print("Sorry , you are too young to become a spy!")
        # age is greater than equal to 50
        elif spy.age >= 50:
            print("Sorry , you are too old to be a spy!")


# if the user chooses the default spy
if existing.upper() == "Y":
    # start the chat function is called
    start_chat(spy)
# the user wants to add a new user
elif existing.upper() == "N":
    # declare variables using a class
    spy = Spy(" ", " ", 0, 0.0)

    # Ask for the name
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # Check if the name is entered or not
    if len(spy.name) > 0 and spy.name.isdigit() == False:
        # ask for the salutation
        spy.salutation = raw_input("What should we call you Mr or Miss?")
        # check if salutation is entered or not
        if len(spy.salutation) > 0:

            # Ask for the age of the spy
            spy.age = raw_input("please enter your age: ")

            if len(spy.age) > 0:
                # raw input always gives a string to typecast age to int.
                spy.age = int(spy.age)
                # Age cannot be less than 12 and greater than 50
                # nested if
                if 12 <= spy.age < 50:
                    print("Welcome to Spy community")

                    # Ask for spy_rating
                    spy.rating = raw_input("Please enter your spy rating: ")
                    if len(spy.rating) > 0:
                        # raw input always gives a string to typecast rating to float.
                        spy.rating = float(spy.rating)

                        # conditions to pass comments according to the spy_rating.
                        if spy.rating > 4.5:
                            print "Great Ace!"
                        elif 3.5 <= spy.rating <= 4.5:
                            print "You are one of the good ones!"
                        elif 2.5 <= spy.rating <= 3.5:
                            print "You can always do better."
                        else:
                            print "We will get someone to help you."

                        # Make the spy come online
                        spy.is_online = True

                        # Call the start_chat function to start(the function will authenticate the user)
                        start_chat(spy)

                    # If spy rating is not entered
                    else:
                        print "Enter a valid spy rating"

                # valid age is not entered
                else:
                    # age is less than 12
                    if spy.age <= 12:
                        print("Sorry , you are too young to become a spy!")
                    # age is greater than equal to 50
                    elif spy.age >= 50:
                        print("Sorry , you are too old to be a spy!")
                    else:
                        print("Please enter a valid age")

            # if age is not entered
            else:
                print("Please enter your age")

        # the salutation is not entered
        else:
            print("Please enter a valid salutation")

    # the name is not entered
    else:
        print("Please enter a valid name")
