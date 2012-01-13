#!/usr/apps/bin/python
import random

HEADTOTAL=25
DECKTOTAL=100
COLORS=['red','blue','purple','grey','green']

class Head:
    def __init__(self,num):
		self.color=COLORS[num%4]
		self.value=num/4+1
		self.name=self.color+" "+str(self.value)
		if self.color=='red' and self.value==5:
			self.spy=True
		else:
			self.spy=False
		if self.color=='grey':
			self.value=-self.value
		
class Card:
	def __init__(self,num):
		self.name="Back"
		self.special=-1
		
class Player:
	def __init__(self,name):
		self.name=name
		self.hand=[]
		self.heads=[]
	def showhand(self):
		for i in range(len(self.hand)):
			print str(i+1)+". "+self.hand[i].name

class Deck:
	def __init__(self):
		self.cards=[]
		self.discard=[]
		for i in range(DECKTOTAL):
			self.cards.append(Card(i))
		random.shuffle(self.cards)
	def draw(self):
		if len(self.cards)== 0:
			self.cards = self.discard
			random.shuffle(self.cards)
			self.discard=[]
		return self.cards.pop()
	def toss(self,Card):
		self.discard.append(Card)
		

deck = Deck()
heads=[]
for i in range(HEADTOTAL):
	heads.append(Head(i))
random.shuffle(heads)

line=[]

	
playnum = int(raw_input("Number of players? "))
players=[]
for i in range(playnum):
	players.append(Player(raw_input("Player "+str(i)+"? ")))
	for j in range(5):
		players[i].hand.append(deck.draw())
	

for x in range(1):
	for i in range(10):
		line.append(heads.pop())
	print "Day "+str(x+1)+" begins..."
	while len(line)>0:
		for i in range(playnum):
			players[i].hand.append(deck.draw())
			print players[i].name+"  This is your hand:"
			players[i].showhand()
			hold=True
			while hold:
				plcard = int(raw_input("Select Card (0 to skip, 9 to see line): "))
				if plcard == 0:
					print "No card played"
					hold=False
				elif plcard > 0 and plcard < 9:
					print "You played "+players[i].hand[i-1].name
					deck.toss(players[i].hand.pop(i-1))
					hold=False
				elif plcard == 9:
					print "Execution line (top dies first):"
					for j in range(len(line)):
						print str(j+1)+". "+line[j].name
					hold=True
			#Slice!
			print line[-1].name+"'s execution has come. "+players[i].name+" collects the head for "+str(line[-1].value)+" points"
			players[i].heads.append(line.pop())

totals=[]
for i in range(playnum):
	totals.append(0)
	for j in range(len(players[i].heads)):
		totals[i]+=players[i].heads[j].value
	print str(totals[i])+" points for "+players[i].name

