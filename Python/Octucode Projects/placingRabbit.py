print("Welcome to: Place the Rabbit\n")

field = [
    ['🌿', '🌿', '🌿'], 
    ['🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿']
]

print(field[0])
print(field[1])
print(field[2], "\n")

print("Where should the rabbit go? 🐇")

picks = []


user_places = input("Please choose a row and a column: ")

row = int( user_places[0] ) 
col = int( user_places[1] )

while( ( row < 0 ) or ( col < 0 ) or ( row  > 3) or (col > 3)):
    user_places = input("Please choose a row and a column: ")
    row = int( user_places[0] ) 
    col = int( user_places[1] )


picks.append( row - 1 )
picks.append( col - 1)

print("\n Success ....")

field[picks[0]][picks[1]] = '🐇'

print(field[0])
print(field[1])
print(field[2], "\n")

