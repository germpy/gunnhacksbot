import discord
from discord.ext import commands

'''
TODO

Check for checkmates
Castling
Pawn moving forward twice on first move
Swap pawn out for piece of player's choice, once it reaches the end of the board

'''
import copy

class Chess():

	# these will be the same for every game
	tiles =   [":black_large_square:", ":white_large_square:",

			   "<:wpawn:810246630715818030>", "<:wknight:810246630573604874>", 
			   "<:wbishop:810246630556434432>", "<:wrook:810246630707822732>",
			   "<:wqueen:810246630653689917>", "<:wking:810246630283935765>",

			   "<:bpawn:810246630556958750>", "<:bknight:810246630279610389>",
			   "<:bbishop:810246630191923301>", "<:brook:810246630338985996>",
			   "<:bqueen:810246630511083560>", "<:bking:810246630636257294>"]

	# the setup: rook, knight, bishop, queen, king, etc.
	backtiles = [3, 1, 2, 4, 5, 2, 1, 3]

	BLACK = 0
	WHITE = 1

	bPawnStart = 1 # the row where black pawns start
	wPawnStart = 6 # the row where white pawns start

	bPawnEnd = 7
	wPawnEnd = 0

	def __init__(self):

		self.board = []

		# fills in the board with empty tiles
		for i in range(8):
			self.board.append([])
			for j in range(8):
				self.board[i].append(self.color(i,j))

		# adds in the chess pieces
		for i in range(8):

			# pawns
			self.board[Chess.wPawnStart][i] = 2
			self.board[Chess.bPawnStart][i] = 8

			# other pieces
			self.board[0][i] = 8 + Chess.backtiles[i]
			self.board[7][i] = 2 + Chess.backtiles[i]

	# what color should the empty tile here be?
	def color(self, r, c):
		if (r % 2 == 0):
			if (c % 2 == 0):
				return Chess.BLACK
			return Chess.WHITE
		if (c % 2 == 0):
			return Chess.WHITE
		return Chess.BLACK

	# are the given coordinates in bounds?
	def inbounds(self, coords):

		return (0 <= coords[0] < 8 and 0 <= coords[1] < 8)

	# number -> row letter -> column
	def toCoord(self, given):

		if type(given) == list:
			return given

		if len(given) != 2:
			return -1
		if given[1] not in "12345678":
			return -1
		if given[0].upper() not in "ABCDEFGH":
			return -1

		return [int(given[1])-1, "ABCDEFGH".find(given[0].upper())]

	# is this square empty, white, or black?
	def getcolor(self, piece):
		piece = self.board[piece[0]][piece[1]]
		if piece <= 1:
			return -1
		if 2 <= piece < 8:
			return Chess.WHITE
		return Chess.BLACK

	# is this square empty, a pawn, a knight, etc.
	def type(self, piece):
		piece = self.board[piece[0]][piece[1]]
		if piece >= 8:
			piece -= 6
		if 2 <= piece <= 7:
			return piece - 2
		return -1

	# WHITE -> BLACK, vice versa
	def opp(self, v):
		if v == 0:
			return 1
		return 0

	# printing to the console
	def debugOutput(self):
		v = "⬛⬜"
		for i in range(8):
			s = str(i+1) + "|"
			for j in range(8):
				if self.board[i][j] <= 1:
					s += v[self.board[i][j]]
				else:
					s += Chess.tiles[self.board[i][j]][2:4]
				s += "|"
			print(s)

	# finds the places a piece can move to
	def legalmove(self, c1, playerColor):

		possmoves = []

		piecemoving = self.type(c1)

		if piecemoving == 0: # pawn

			dr = 0 # will the player move up a row, or down a row?
			if playerColor == Chess.BLACK:
				dr = 1
			else:
				dr = -1

			cr = c1[0]
			cc = c1[1] # current position

			# moving diagonally
			if self.inbounds([cr+dr, cc-1]) and self.getcolor([cr + dr, cc - 1]) == self.opp(playerColor):
				possmoves.append([cr+dr, cc-1])
			if self.inbounds([cr+dr, cc+1]) and self.getcolor([cr + dr, cc + 1]) == self.opp(playerColor):
				possmoves.append([cr+dr, cc+1])

			# moving straight forward
			if self.inbounds([cr + dr, cc]) and self.getcolor([cr + dr, cc]) == -1:
				possmoves.append([cr+dr, cc])

		if piecemoving == 1: # knight
			v = [-2, -1, 1, 2]
			for i in v:
				for j in v:
					if abs(i) == abs(j):
						continue

					newc = [c1[0] + i, c1[1] + j]
					if self.inbounds(newc):
						possmoves.append(newc)

		if piecemoving == 2 or piecemoving == 4: # bishop and queen (queen can move diagonally)
			
			# moving up and left
			for i in range(-1, -99, -1):
				thisc = [c[0] + i, c1[1] + i]
				if not self.inbounds(thisc):
					break
				possmoves.append(thisc)
				if self.type(thisc) != -1:
					break

			# moving down and right
			for i in range(1, 99):
				thisc = [c[0] + i, c1[1] + i]
				if not self.inbounds(thisc):
					break
				possmoves.append(thisc)
				if self.type(thisc) != -1:
					break

			# moving down and left
			for i in range(-1, -99, -1):
				thisc = [c[0] - i, c1[1] + i]
				if not self.inbounds(thisc):
					break
				possmoves.append(thisc)
				if self.type(thisc) != -1:
					break

			# moving up and right
			for i in range(1, 99):
				thisc = [c[0] - i, c1[1] + i]
				if not self.inbounds(thisc):
					break
				possmoves.append(thisc)
				if self.type(thisc) != -1:
					break

		if piecemoving == 3 or piecemoving == 4: # rook and queen
			# moving vertically
			for i in range(c1[0] - 1, -1, -1):
				possmoves.append([i, c1[1]])
				if self.type([i,c1[1]]) != -1:
					break
			for i in range(c1[0] + 1, 8):
				possmoves.append([i, c1[1]])
				if self.type([i,c1[1]]) != -1:
					break

			# moving horizontally
			for i in range(c1[1] - 1, -1, -1):
				possmoves.append([c1[0], i])
				if self.type([c1[0], i]) != -1:
					break
			for i in range(c1[1] + 1, 8):
				possmoves.append([i, c1[1]])
				if self.type([i,c1[1]]) != -1:
					break

		if piecemoving == 5: # king
			for i in range(-1,2):
				for j in range(-1,2):
					if i == j == 0:
						continue
					possmoves.append([c1[0]+i, c1[0]+j])

		return possmoves

	# is moving the piece in T1 to T2 legal?
	def legal(self, t1, t2, playerColor, checkForCheck = True):

		# handles input
		c1 = self.toCoord(t1)
		c2 = self.toCoord(t2)
		if (c1) == -1 or (c2) == -1:
			return False, "invalid input"


		# basic issues w/ moving
		if self.getcolor(c1) == -1:
			return False, "no piece there"
		if self.getcolor(c1) != playerColor:
			return False, "not your piece"
		if self.getcolor(c2) == playerColor:
			return False, "cannot move onto another one of your pieces"
		if self.type(c2) == 5:
			return False, "cannot move onto a king"

		# can the piece legally move there?

		possmoves = self.legalmove(c1, playerColor)
		if c2 not in possmoves:
			return False, "that piece cannot move there"

		temp = copy.deepcopy(self.board)
		self.board[c2[0]][c2[1]] = self.board[c1[0]][c1[1]]
		self.board[c1[0]][c1[1]] = self.color(c1[0], c1[1])

		# will the player's king be in check?

		# find where the player's king is
		kingc = []
		for i in range(8):
			for j in range(8):
				if self.type([i,j]) == 5 and self.getcolor([i,j]) == playerColor:
					kingc = [i,j]


		
		if checkForCheck == True:

			illegalMove = False

			# check each tile on the chessboard
			for i in range(8):
				for j in range(8):
					thiscolor = self.getcolor([i,j])
					if thiscolor != self.opp(playerColor):
						pass # this square cannot "capture" the king

					# will the opponent's piece be able to reach the king from here?
					res, e = self.legal([i,j], kingc, self.opp(playerColor), checkForCheck = False)
					# if yes, illegalMove should be set to True
					illegalMove = (illegalMove or res)


			if illegalMove == True:
				self.board = temp
				return False, "this would put your king in check"

		# the move is legal
		return True, ""

c = Chess()
c.debugOutput()


print(c.legal("H7", "H6", Chess.WHITE))
c.debugOutput()



class GameCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="donothing")
	async def donothing(self):
		return

def setup(bot):
	bot.add_cog(GameCog(bot))