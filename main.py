from datetime import  datetime
from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from colorama import init, Fore, Back, Style


#default status list
STATUS_MESSAGES=["hello","I am at gym"," I am driving car."]

# add status
def add_status(current_status_message):
    updated_status_message = None

    if(current_status_message != None):
        print"your current status message is:"+current_status_message
    else:
        print "you dont have any status"
#user wants an default status Y/N
    default=raw_input("Do you want to select from older satus Y/N:")
#if user enters N
    if default.upper()=='N':
        new_status_message=raw_input("Enter your Status:")
        if len(new_status_message)>0:
            updated_status_message=new_status_message
            STATUS_MESSAGES.append(new_status_message)
            print updated_status_message
            print"Your Status is "+updated_status_message
#if user enters Y
    elif default.upper()=='Y' :
        item_position=1
        for message in STATUS_MESSAGES :
            print'%d.%s'%(item_position,message)
            item_position=item_position+1
        message_selection=int(raw_input("Select A status from list:"))
        if len (STATUS_MESSAGES)>=message_selection:
            updated_status_message=STATUS_MESSAGES[message_selection-1]
            print updated_status_message
    else:
        print "The option you chose is not valid! Press either y or n"
    return updated_status_message

# add friend function
def add_friend():


    new_friend = Spy('', '', 0, 0.0)
    new_friend.salutation = raw_input("Are you Mr. OR Ms.:")
    new_friend.name= raw_input("please add your friends name:")
    new_friend.rating=float(raw_input("Enter your friendz  rating:"))
    new_friend.age=int(raw_input("Enter your age please:"))
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 1.0:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print "Invalid entry!!!!!! .you canot add spy with above details"
    return len(friends)

#select a friend
def select_friend ():
    item_number=0
    for friend in friends:
        #print '%s aged %d with rating %.2f is online' %(friend['name'], friend['age'], friend['rating'])
        print '%d. %s %s' % (item_number + 1, friend.salutation,friend.name)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends:")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

#send a message
def send_message():
    friend_choice= select_friend()
    original_image=raw_input("what is name of your image:")
    output_path="output.jpg"
    text=raw_input("what do you want to say:")
    Steganography.encode(original_image,output_path,text)
    new_chat = ChatMessage(text, True)
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"

#read a message
def read_message():
    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"
    if secret_text == "":
        print"SORRY !!!! sender did not send any secret message to you"
    elif secret_text.upper()=="SM":
        print"save me ."
    elif secret_text.upper()=="ALERT":
        print"please be alerted ."
    elif secret_text.upper()=="SOS":
        print"This is a special  message.clear the path ASAP"
    else:
        print secret_text
        text_length= len(secret_text)- secret_text.count(' ')
        print str("Message has ")+str(text_length)+str("  words")


#reads chats history
def read_chat_history():
    read_for = select_friend()
    init()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            a = chat.time.strftime("%d %B %Y")
            b= 'You said:'
            c= chat.message
            print(Fore.RED + str(a))
            print(Fore.BLUE + str(b))
            print(Fore.BLACK + str(c))

        else:
            d=chat.time.strftime("%d %B %Y")
            e=friends[read_for].name+str(" said")
            f=chat.message
            print(Fore.RED + str(d))
            print(Fore.BLUE + str(e))
            print(Fore.BLACK + str(f))

        # start chat function for existing and new user
def start_chat(spy):
    current_status_message=None
    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and sy.age < 50:
        print "AUTHENTICATION COMPLETE. Welcome " + spy.name + " your  age  is " + str(spy.age) + " and rating " + str(
            spy.rating) +" out of 5"+ " we are Proud to have you. "
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n1. Add a status update \n2) Add a friend \n3) select a friend \n4) Send a secret message \n5) Read a secret message \n6) Read chats from a user \n7) Close application\n "
        menu_choice = int(raw_input(menu_choices))

#choice 1 will update the message
        if menu_choice == 1:
            print 'You chose to update the status'
            current_status_message = add_status(current_status_message)

#choice 2 will add a friend
        elif menu_choice == 2:
            print"You choose to add a friend"
            friends = add_friend()
            print 'You have %d friends' % (friends)

#choice 3 will select a friend
        elif menu_choice == 3:
            friend_choice_position =select_friend()
            print friend_choice_position

#choice 4 will send a message
        elif menu_choice == 4:
            send_message()

#choice 5 will read a message
        elif menu_choice == 5:
            read_message()
#choice 6 will read chat history
        elif menu_choice== 6:
            read_chat_history()
#chouce 7 will exit the application
        elif menu_choice==7:
            exit()
# this will be printed if wrong entry is done
        else:
            show_menu=False
            print "please enter any option from 1-6"
#proceed as existing or a new user
spy_input = raw_input("YOU WANT TO BE A default USER   Y/N:")

#existing usery
if(spy_input.upper()=='Y' ):
    start_chat(spy)

#proceed as a new user
elif(spy_input.upper()=='N'):
    spy = Spy('', '', 0, 0.0)

    spy['name'] = raw_input("Welcome to SPY CHAT APPLICATION , you must tell me your spy name first: ")
    spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")
    spy['age'] = int(raw_input("What is your age?"))
    spy['rating'] = float(raw_input("What is your spy rating?"))

    start_chat(spy)
else:
    print"Please enter either Y/N"

