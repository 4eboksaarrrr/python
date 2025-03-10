#-------------------- 1 доюавление в список(метод append, extend) ---------------------
#
# list_number = [1, 2, 3, 4, 5]
# for i in range(5):
#     new_num = int(input("введите числа"))
#     list_number.append(new_num)
# print(list_number)
#
# list1 = ['lo', 'ko', 'qwe','ko','ko','ko',]
# list2 = ['ko','ko','ko','2vo', 'xcvo', 'xcvwe',]
#
# list1.extend(list2)
# print(list1)


#----------------------метод  count-----------------------

# list1 = ['lo', 'ko', 'qwe','ko','ko','ko',]
# list2 = ['ko','ko','ko','2vo', 'xcvo', 'xcvwe',]
# print(list1.count('ko'))

#----------------------индексы-----------------------
#
# scores = [8, 5, 10, 7, 6]
# scores[1] *= 3
# x = scores[0]

# print(x)
# print(scores)

#-----------------------------------------------------

# slovo = "kakaska"
# zamena = 'L'
# list1 = list(slovo)
#
#
# list1[2] = zamena
# print(list1)

#---------- --------------------метод insert-------------------------
# list_1 = ['popa ', 'kaka', 'kal']
# list_1.insert(2,'govno')
# print(list_1)

#------------------------метод index--------------------------------------


# list_1 = ['popa ', 'kaka', 'kal']
# i_list_1= list_1.index('kal')
# print(i_list_1)
#

#------------------------вложенные списки--------------------------------------

# numb = int(input(""))
# numbers = list(range(1, numb+1))
# print(numbers)
#

#--------------------------------------------------------------------

# N = int(input(""))
# members = []
# num = 1
# for _ in range(N // 3):
#     members.append(list(range(num, num+3)))
#     num += 3
#
# print(members)
#

#--------------------------------------------------------------------
#
# list1 = [['lol','kek'],['kak','puk']]
# list1[0][1] = 'nasral'
# print(list1)

#----------------------list comprehetion-------------------
# list1 = []
# for x in range(10000000):
#     list1.append(x*x)
# print(list1)
# # калл и медленно





# list1 = [x**2 for x in range(10000000)]
# print(list1)
# #крутяк и супербыстро

#-----------------------------------------

# a = [1,2,3,4]
# print(*a)

#-----------------------------------