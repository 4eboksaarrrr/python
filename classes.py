#-----------------------обычное сощздание________________________
# class User:
#     user_name = 'nikita'
#     password = 'qwerty'
#     is_banned = False
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'lox'
# print(user_1.user_name,user_2.user_name)
# User.user_name = 'леша тоже'
# print(user_1.user_name,user_2.user_name)

#----------------------self----------------------
# class User:
#     user_name = 'nikita'
#     password = 'gay'
#     krytoy = False
#     friends = []
#
#     def print_info(self):
#         print(' name: {}\n Password: {}\n krytoy?: {}\n'.format(
#             self.user_name, self.password, self.krytoy)
#         )
#
#     def add_friend(self, friend):
#        self.friends.append(friend)
#
#
#
# user_1 = User()
# user_1.print_info()
# user_1.add_friend('lesha')
# print(user_1.friends)


#-----------------------__init__----------------------
from cU import User
# from cU import *           - калл лучше не юзать
# import cU                  - user_1= cU.User('nikita', 100)


user_1 = User('nikita', 100)
user_1.print_info()

user_2 = User('lesha', 1000)
user_2.print_info()

#--------------------------------------