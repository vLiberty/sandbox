from cTrap import cTrap
from cRoom import cRoom
from room_translation import *
from trap_translation import *

"""
This links new traps and associates them to a room. 
1) View Rooms - Presents a list of the json files in room_json/ directory (this is where new rooms jsons are held)
2) Adding new traps links traps from left to right from the available traps in trap_json
3) Adding traps to an existing room (not created yet.)
4) Removing rooms and updating the traps that are affected by this change (not created yet.)
"""

ans = True
while ans:
	print ("\n1) View rooms.\n2) Create new room.\n3) Add trap to room")
	ans = input("Selection: ") 
	if ans == "1":
		print ("\nPlease select a room to view")
		viewTrap = True
		while viewTrap:
			fileList = create_room_dictionary()
			for i in sorted(fileList):
				print ('{0}) {1}'.format(i, fileList[i]))
			viewTrap = input("\n# Selection: ")
			if viewTrap not in fileList:
				print ("doesnt exist") 
			else:
				print (read_json_room(fileList[viewTrap]))
	elif ans == "2":
		#Present a list of traps and say select the closest trap to the door and prepare to add traps in a clockwise fashion.  
		"""
		New room *Create new room class instace
		- List traps not in a room left & right = 0 *Done*
		- Begin loop
			- Select LEFT trap (input) *create class instance of left trap *Done*
			- update room.trap [] = append(LEFT.trapID) *done*
			- update (LEFT).room_id trap -- Where does this belong? 
			- [ New Loop ] List the traps not in a room 
			- Select next trap (input) (RIGHT) *create class instance of right trap
			- update (RIGHT).room_id trap
			- update (LEFT).rightPeerID 
			- update (RIGHT).leftPeerID
			- update room.trap [] = append(RIGHT.trapID)
			- Write JSON's for traps (jsonstr, filename)
			- Write JSON's for Room
			- if the loop will continue then (right becomes left for adding the next trap)
				- set a temp variable with the new LEFT trap_id. 
		"""
		newRoom = cRoom("0",[],"0","0") #create a new room 
		viewTrap = True
		print ("Select the first (most left) trap in the room: ")
		tempLeft = 0
		while viewTrap:
			trapList = create_dictionary_empty_traps()
			numTrap = create_num_trap(trapList)
			for i in sorted(numTrap):
					print ("{}) {}.json".format(i, numTrap[i]))
			viewTrap = input("Select the first trap for the room: ")
			if viewTrap not in numTrap:
				print("Not in the list")
			else:
				firstSelection = numTrap[viewTrap] #hold the ID of the first trap so it cannot select the same one twice. Build out the list for comparison. 
				outerData= json.loads(read_json_file(numTrap[viewTrap] + '.json')) #Open the JSON file that holds the left trap
				outerTrap = cTrap(outerData['id'],outerData['leftpeerid'],outerData['rightpeerid'],newRoom.room_id) #create a class with that data

				newRoom.traps.append(numTrap[viewTrap]) #append the trap list to the room. 
				
				OIleftId = outerData['id'] #this variable gets updated on the inside as the loop iterates. 

				secLoop = True
				updatePreRight = False #this populates n+1 additions to link left and right peer ids

				while secLoop:
					trapList = create_dictionary_empty_traps() #Make the list smaller every time the loop iterates. 
					numTrap = create_num_trap(trapList)		
					if len(numTrap) == 0:
						break
					for i in sorted(numTrap):
						print ("{}) {}.json".format(i, numTrap[i]))
					secLoop = input("\n Select the next trap for the room placed to the right: ")
					if viewTrap not in numTrap:
						print ("Not in the list")
					else:
						if firstSelection in numTrap[secLoop]: 
							print ("Duplicate traps")
						else:
							firstSelection = numTrap[secLoop] #update the selection for next loop iteration.
							if updatePreRight == False: # Update the outter trap only on the first iteration.
								outerTrap.rightpeerid = numTrap[secLoop]
								write_json_file(outerTrap.return_trap_json(), outerTrap.return_json_filename()) #write the left trap DO not use LEFTTrap again in 2nd loop
								OIleftId = outerTrap.id
							elif updatePreRight == True:
								#Open the previous right trap JSON and update the right peer information of the newly added trap	
								rightData2 = json.loads(read_json_file(preRight + '.json')) #Remember this is now the LEFT trap. 
								updateRight = cTrap(rightData2['id'],OIleftId, numTrap[secLoop],rightData2['roomid'])
				
								OIleftId = rightData2['id'] #This gets updated for when we loop again. 

								write_json_file(updateRight.return_trap_json(),updateRight.return_json_filename())

							rightData1= json.loads(read_json_file(numTrap[secLoop] + '.json')) #Open the JSON file that holds the RIGHT trap
							rightTrap = cTrap(rightData1['id'],OIleftId,rightData1['rightpeerid'],newRoom.room_id) #create a class with that data

							if updatePreRight == True:
								OIleftId = rightData1['id'] # This is updated after we enter and after we've gone through the loop once. 

							newRoom.traps.append(numTrap[secLoop]) #add the trap list to the room.
							
							write_json_file(rightTrap.return_trap_json(),rightTrap.return_json_filename()) #write the right trap

							updatePreRight = True #if multiple traps are added, this will ensure the previous one is updated. 
							preRight = rightTrap.id #Load the current right trap id so that it will be updated if another trap is added

							write_json_room(newRoom.gen_room_json(),newRoom.return_json_filename()) #Create/Update the room. 
	elif ans == "3":
		print ("\nPlease select a room to add traps too")
		viewTrap = True
		while viewTrap:
			fileList = create_room_dictionary()
			for i in sorted(fileList):
				print ('{0}) {1}'.format(i, fileList[i]))
			viewTrap = input("\n# Selection: ")
			if viewTrap not in fileList:
				print ("doesnt exist") 
			else:
	else:
		print ("\nPlease enter a valid selection")
   