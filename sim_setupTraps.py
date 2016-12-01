from cTrap import cTrap
from trap_translation import *

#x = cTrap()
#write_json_file(x.return_trap_json(),x.return_json_filename())

ans = True
while ans: 
	print ("\n\n1) View Current traps.\n2) Add a new trap.\n3) Remove a trap")
	ans = input("Selection: ")
	if ans == "1": 
		print ("\nViewing collection\n")
		#call the function to list all of the available traps and their creation dates. 
		print ("\nPlease Select a Trap to view")
		viewTrap = True
		while viewTrap:
			fileList = create_dictionary()
			#print ("Filetype is {}: ".format(type(fileList)))
			for i in sorted(fileList):
				print ('{0}) {1}'.format(i, fileList[i]))
			viewTrap = input("\n# Selection: ")
			if viewTrap not in fileList:
				print ("doesnt exist") 
			else:
				print("print the contents of the json file")
				print (read_json_file(fileList[viewTrap]))
	elif ans == "2": 
		print("\nAdd Trap\n")
		x = cTrap() #create an empty file
		write_json_file(x.return_trap_json(), x.return_json_filename())
		#write_json_file("str","9213922.json")


		# Call the function to list all of the available traps and to select a number with the trap id beside it
		# how does this work for a large list? Format a table to display? 
		# The first trap is your right trap then the 2nd choice is your left. 
		# if you insert a new trap between two paired traps, ask if they want to insert and redraw the association
	elif ans == "3":		# Call the function to list all of the available traps and select the number to delete 
		viewTrap = True
		while viewTrap: #First loop to select a trap. 
			fileList = create_dictionary()
			for i in sorted(fileList):
				print ('{0}) {1}'.format(i, fileList[i]))
			viewTrap = input("\n# Select trap to delete: ")
			if viewTrap not in fileList:
				print ("Please chose a trap from the list to delete.") 
			else:
				delSelction = True
				while delSelction: #Provide the ARE YOU SURE you want to delete. 
					delSelction = input("Type \'yes\' to delete this file {} or press \'<enter>\' to go back\n:".format(fileList[viewTrap]))
					if delSelction == "yes":
						print ("\nDeleting trap {}\n".format(fileList[viewTrap]))
						#More logic needs to present for removing a trap...... Removing 
						delete_json_file(fileList[viewTrap])
						break						
		"""if ans != "yes":
			print ("\nPress enter to return and not delete the file.")	
		else:
			print ("Deleting file: {}".format(filename))"""
	else:
		print ("\n\n\nPlease choose 1 - 4\n\n\n")

# Once the viewing is available you then.....
# Define a floor and assign a trap to a floor.
# Define a building and assign a trap to a building. 
# District should be in a separate area for larger deployments. floor and building should be apart of
#   the new trap creation routine. 
# Define a new trap creation screen
"""

y = cTrap()
z = cTrap()

print (x.return_trap_json())
print (y.return_trap_json())
print (z.return_trap_json())

write_json_file(x.return_trap_json(), x.return_json_filename())
write_json_file(y.return_trap_json(), y.return_json_filename())
write_json_file(z.return_trap_json(), z.return_json_filename())
"""
#[complete] Setup a trap (entry and put it in a json file) -> create a python package that communicates between the sources 
# | Trap Source | <-> | Translation (creates communication) | <-> |  Get Fetch Request to Translation |
# Create a menu driven page to add, edit, remove a trap.
# when a right peer ID is set, then set the left peer ID
# when a left peer ID is set, then set the right peer ID

#Edit a trap and update the json
#Read the list of traps from the json. 

#display current room configuration. 
#dislplay the current floor configuration. 
#display the current ... configuration. 

#simulate a trap trigger for a given room. 
#simulate a trap trigger for a given floor. 
#simulate a trap trigger from ...

#display trap triggers by District, region, building, floor, room. Start broad 