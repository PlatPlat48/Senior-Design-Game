#Here's an example of an array!
#(A collection of Values.)
#To get a value or instance in an array,
#use array[indexInArray-1].
#So to call 12 in array = [0,91,12,53,40,25],
#You would call array[3-1] or array[2].
#You can get the length of an array easily
#with len(array).
#Now... See if you can solve this puzzle!
from Solid import*
class Array_Puzzle(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "Array_Puzzle"
		self.image = pygame.image.load("Game/Sprites/AsymetricStoneBlock.png")
		self.codingStartVisible = [0,18,]
		self.codingEndVisible = [9,19,]
	def checkSolid(self,instance):
		a = len(instance)
		return(instance)
