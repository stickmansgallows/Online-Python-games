
attribList 	= "cost", "workers", "box", "pallet", "power"
partList	= "machine", "prodRob", "workRob", "pallets", "power", "opt"

#part attributes
a["machine"]["cost"] 	= [1,3,6,8,9,11,14,19]
a["machine"]["box"]		= [1,1,2,1,3,2,3,3]
a["machine"]["workers"]	= [-2,-2,-3,-1,-3,-2,-2,-2]
a["machine"]["power"]	= [-2,-1,-1,-1,-2,-1,-2,-1]
a["machine"]["pallet"]	= [0,0,0,0,0,0,0,0]

a["prodRob"]["cost"] 	= [4,7,9,10,13,15,20]
a["prodRob"]["box"]		= [1,1,2,3,2,3,3]
a["prodRob"]["workers"]	= [0,0,0,0,0,0,0]
a["prodRob"]["power"]	= [-2,-1,-2,-3,-1,-2,-1]
a["prodRob"]["pallet"]	= [0,0,0,0,0,0,0]

a["workRob"]["cost"] 	= [6,10,13,17,22]
a["workRob"]["box"]		= [0,0,0,0,0]
a["workRob"]["workers"]	= [1,2,3,4,5]
a["workRob"]["power"]	= [-1,-1,-1,-1,-1]
a["workRob"]["pallet"]	= [0,0,0,0,0]

a["pallets"]["cost"] 	= [6,10,14,18,22,26]
a["pallets"]["box"]		= [0,0,0,0,0,0]
a["pallets"]["workers"]	= [0,0,0,0,0,0]
a["pallets"]["power"]	= [0,0,0,0,0,0]
a["pallets"]["pallet"]	= [1,2,3,4,5,6]

a["power"]["cost"] 		= [12,17,21,25,29,33]
a["power"]["box"]		= [0,0,0,0,0,0]
a["power"]["workers"]	= [1,1,1,1,1,1]
a["power"]["power"]		= [1,2,3,4,5,6]
a["power"]["pallet"]	= [0,0,0,0,0,0]

a["opt"]["cost"] 		= [17,22,30,31,39]
a["opt"]["box"]			= [1,1,2,1,2]
a["opt"]["workers"]		= [0,0,0,1,1]
a["opt"]["power"]		= [1,1,2,3,3]
a["opt"]["pallet"]		= [0,0,0,0,0]

#part quantity by player
b["machine"] = 	[0,0,0,0],
				[1,2,2,3],
				[1,2,2,3],
				[1,1,2,2],
				[1,1,1,2],
				[1,2,3,3],
				[1,1,2,2],
				[1,1,1,1]
				
b["probRob"] =	[0,0,0,0],
				[1,2,3,4],
				[2,3,4,4],
				[1,1,1,1],
				[1,2,3,4],
				[1,1,1,2],
				[1,1,2,2]
				
b["workRob"] =	[0,0,0,0],
				[1,1,2,2],
				[1,2,2,2],
				[1,2,2,2],
				[1,1,1,2]
				
b["pallets"] =	[1,2,3,4],
				[1,2,3,4],
				[1,2,3,4],
				[0,0,0,1],
				[2,4,5,5],
				[1,1,1,1]
				
b["power"] =	[0,0,0,0],
				[1,1,2,2],
				[1,2,2,2],
				[1,1,1,2],
				[1,1,1,1],
				[1,1,1,1]
				
b["opt"] =		[1,1,1,1],
				[1,1,1,1],
				[1,1,1,2],
				[0,1,1,1],
				[1,1,2,2]
