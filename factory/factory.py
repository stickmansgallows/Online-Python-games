import database

class Part:
	def __init__(self, partType, level):
		self.partType = partType
		self.level = level
		self.used = false
		self.maxLevel
		for i in attribList:
			self.attrib[i] = a[partType][i][level]
		
	def buy(self,player):
		self.owner = player

class Player:
    def __init__(self, number):
        self.player = number
        self.slots = 8
        self.money = 20
        self.stats = []
        for attrib in attribList:
            self.stats[attrib] = 0
        self.equipment = []
        self.equipment.append(Part('machine',0))
        self.equipment.append(Part('machine',0))
        self.equipment.append(Part('prodRob',0))
        self.equipment.append(Part('prodRob',0))
        self.updateState()

    def updateState(self)
        for attrib in attribList:
            self.stats[attrib] = 0
            for parts in self.equipment:
                self.power += parts[attrib]
                
if __name__ == '__main__':
	players = 5
	for i in partList:
		for j in range(len(a[i]['cost']):
			for k in range(b[i][j][players]):	       
			       parts.append(Part(i,j))
	

