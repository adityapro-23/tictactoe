def PrintBoard(m):
	print("+---+---+---+")
	print("| %s | %s | %s |" % (m[0][0], m[0][1], m[0][2]))
	print("+---+---+---+")
	print("| %s | %s | %s |" % (m[1][0], m[1][1], m[1][2]))
	print("+---+---+---+")
	print("| %s | %s | %s |" % (m[2][0], m[2][1], m[2][2]))
	print("+---+---+---+")

map = [
	[' ', ' ', ' '],
	[' ', ' ', ' '],
	[' ', ' ', ' ']
]

PrintBoard(map)

def checkBoard():
	if map[0][0] == map[1][0] and map[1][0] == map[2][0]:
		return map[0][0]
	if map[0][0] == map[0][1] and map[0][1] == map[0][2]:
		return map[0][0]
	if map[0][0] == map[1][1] and map[1][1] == map[2][2]:
		return map[0][0]
	if map[2][0] == map[1][1] and map[1][1] == map[0][2]:
		return map[2][0]
	if map[2][0] == map[2][1] and map[2][1] == map[2][2]:
		return map[2][0]
	if map[2][2] == map[1][2] and map[1][2] == map[0][2]:
		return map[2][2]
	if map[0][1] == map[1][1] and map[1][1] == map[2][1]:
		return map[0][1]
	if map[1][0] == map[1][1] and map[1][1] == map[1][2]:
		return map[1][0]
	
	return ' '

def loop():
	turn = 0
	current = 'o'

	while True:
		if current == 'o':
			current = 'x'
		else:
			current = 'o'

		turn += 1

		while True:
			inp = input("What will be your move %s? " % current)
			x = int(inp.split('-')[0]) - 1
			y = int(inp.split('-')[1]) - 1

			if map[y][x] != ' ':
				print("This place is already taken! Try again %s" % current)
				continue
			
			map[y][x] = current

			PrintBoard(map)

			break

		win = checkBoard()
		if win != ' ':
			print("The winner is: %s!" % win)
			break
		elif turn == 9:
			print("Draw!")
			break
				

loop()