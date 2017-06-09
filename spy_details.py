from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None



class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#objects of class chatMessage



#existing user details
spy = Spy('bond', 'Mr.', 24, 4.7)

# objects of class Spy
friend_one = Spy('rohan', 'Mr.', 3.4, 20)
friend_two = Spy('sonal', 'Ms.', 3.4, 22)
friend_three = Spy('Dhruv', 'Mr.', 2.3, 31)

#friends list stores objects of class Spy
friends = [friend_one, friend_two, friend_three]