# # Library project

# library = []
# wishlist = []

# owned_book = input("Enter the name of a book you own: ")
# if (owned_book):
# 	library.append(owned_book)

# another_owned_book = input("Enter the name of another book you own (or press Enter to skip): ")
# if (another_owned_book):
# 	library.append(another_owned_book )

# print('\n')
# print (f'Your Library: {library}')
# print('\n')

# wish_to_have = input("Enter the name of a book you wish to have in the future: ")
# if (wish_to_have):
# 	wishlist.append(wish_to_have)

# another_wish_to_have = input("Enter the name of another book you wish to have in the future (or press Enter to skip): ")
# if (another_wish_to_have):
# 	wishlist.append(another_wish_to_have)

# print(f"library: {library}") 
# print(f"wishlist: {wishlist}" ) 


# print('\n')
# print (f'Your Wishlist: {wishlist}')
# print('\n')

# acquired_from_wish = input("Enter the name of a book from your wishlist that you've aquired (or press Enter to skip): ")
# library.append(acquired_from_wish)
# wishlist.remove(acquired_from_wish)

# print(f"library: {library}") 
# print(f"wishlist: {wishlist}") 

# if (acquired_from_wish):
# 	wishlist.remove(acquired_from_wish)
# 	library.append(acquired_from_wish)

# print('\n')
# print(f'Updated Library: {library} \nUpdated Wishlist: {wishlist}')
# print('\n')

# wish_to_donate = input("Enter the name of a book from your library that you wish to donate (or press Enter to skip): ")

# if (wish_to_donate):
# 	library.remove(wish_to_donate)

# print('\n')
# print(f'Final Library after Donations: {library}')

# #_______________________________________________________

# # methods on lists proj 1

# colors = []
# first_color = input("Add the first color you like: ")
# colors.append(first_color)

# more_colors = input("Do you like to add more colors? Yes, or No? ")
# active = True

# while (active):

# 	if (more_colors.lower() == "no"):
# 		print(f"The color you like is : \n {colors}")
# 		active = False
# 	elif (more_colors.lower() == "yes"):
# 		second_color = input("Add another color to the list: ")
# 		colors.append(second_color)
# 		print(f"The colors you like are : \n {colors}")
# 		active = False
# 	else:
# 		print("Enter a valid, yes or no")
# 		more_colors = input("Do you like to add more colors? Yes, or No? ")

# #______________________________________________

# # methods on lists proj 2

# class_a = ['ahmed', 'muhammad']
# class_b = ['dyab', 'roni']
# class_all = class_a + class_b

# print(f'class a are: \n \t {class_a} \nAnd class b are: \n \t {class_b}\nwhile calss a and b are: \n \t {class_all}')
# class_all.append('fuck me')
# print(class_all)

# #______________________________________________
