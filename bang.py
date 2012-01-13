#!/usr/apps/bin/python
import random

class Character:
    def __init__(self, num):
		self.name = names[num]
		self.description
		self.effect
		self.life

class Player:
	def __init__(self, name, position, role, charnum):
		self.name=name
		self.pos=position
		self.role=role
		self.character = Character(charnum)
		self.hand=[]
		self.table=[]
		self.gun=1
		self.life=4
		if role='sheriff':
			self.life+=1
		if charnum == blacklist:
			self.life-=1
		self.lifemax=self.life
	def draw(self, card):
		self.hand.append(card)
	def playhand(self, card):
		if card.color == green or card.color == blue:
			self.table.append(card)
			self.hand.remove(card)
	def playtable(self, card):
		self.table.remove(card)
	def showhand(self):
		print "Hand: "
		for i in range(len(hand)):
			self.hand[i].disp
	def showtable(self):
		print "In play: "
		for i in range(len(table)):
			self.table[i].disp		

class Card:
	def __init__(self, num):
		self.name
		self.descrip
		self.color #None, blue, green
		self.effect #Bang, steal, discard, draw, health, miss, indian, genstore
		self.targets #Reachable, 1, all, any, self, deck
		self.face #Face card value
	def disp(self):
		print self.name+" "self.descrip
		
class Deck:
	def __init__(self):
		self.cards = []
		self.discard = []
		for i in 100: 
			self.cards.append(Card(i))
		random.shuffle(self.cards)
	def draw(self):
		if len(self.cards = 0):
			self.cards = self.discard
			random.shuffle(self.cards)
			self.discard=[]
		return self.cards.pop()
	def toss(self,Card):
		self.discard.append(Card)

#Character Deck
CHARNUM=30
chars=[]
for i in range(CHARNUM):
	chars.append(Character(i))
random.shuffle(chars)

#Playing card deck
deck = Deck()

#Enter in players one at a time
playernum = raw_input("Number of players? ")
playernames=[]
for i in range(playernum):
	playernames.append(raw_input("Player "+str(i+1)+"?"))
random.shuffle(playernames)

#Make role deck
#Sheriff is always 0
deputy = [0,0,0,0,1,1,1,2,2]
outlaw = [0,0,0,1,1,2,2,2,3]
renegade=[0,0,1,1,1,1,2,2,2]
sheriff= [0,1,1,1,1,1,1,1,1]
roles=[]
d=deputy[playernum]
ren=renegade[playernum]
o=outlaw[playernum]
for i in range(playernum-1):
	if d > 0:
		r='deputy'
		d-=1
	elif ren > 0:
		r='renegade'
		ren-=1
	elif o > 0:
		r='outlaw'
		o-=1
	else:
		break
	roles.append(r)
random.shuffle(roles)
roles.append('sheriff')
roles.reverse()

print "Character deck has been shuffled and roles assigned"
if deputy[playernum] == 0:
	print "There are no deputies"
elif deputy[playernum] == 1:
	print "There is one deputy"
else:
	print "There are "+str(deputy[playernum])+" deputies"
if outlaw[playernum] == 1:
	print "one outlaw"
else:
	print str(outlaw[playernum])+" outlaws"
if renegade[playernum] == 1:
	print "and one renegade"
else:
	print "and "+str(renegade[playernum])+" renegades"

print "Say hi to Sheriff "+playernames[0]
print "Going clockwise from the sheriff, these are the positions of the players:"
for i in range(playernum):
	print str(i+1)+": "+playername[i]
	
players=[]
for i in range(playernum):
	print playername[i]+"'s turn. Choose a character"
	guy=[chars.pop(),chars.pop()]
	print "Your role is "+roles[i]
	print guy[0].name
	print guy[0].description
	print guy[1].name
	print guy[1].description
	choice = raw_input("1 or 2? ")
	players.append(Player(playername[i]),i,roles[i],guy[choice-1])
	for j in range(players[i].life):
		players[i].draw(deck.draw())

roundn=0
while 1:
	roundn+=1
	print "Round "+str(roundn)+"...FIGHT!"
	for i in range(playernum):
		print players[i].name+": "+players[i].role
		players[i].draw(deck.draw())
		players[i].draw(deck.draw())
		players[i].showhand
		players[i].showtable
		print "Health: "+str(players[i].life)
		
		

