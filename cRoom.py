import time, random
from cTrap import cTrap
"""
Manage room information via a class that mirrors the json contents. 
"""

class cRoom(object):
	def __init__(self, room_id="0", traps = [], building_id ="0", district_id="0"):
		if room_id == "0":
			self.room_id = self.gen_room_id()
		else:
			self.room_id = room_id
		self.traps = traps #build out the list of traps for this floor *function*
		self.building_id = building_id
		self.district_id = district_id

	def gen_room_id(self):
		#generate an epoch timestamp and return the millisecond value for the id. 
		#this might have to be more complex. 
		i = str(time.time())
		j = i.split('.')
		k = str(random.random())
		l = k.split('.')
		return j[1].center(8,"0") + "-" + l[1].center(20,"0")

	def gen_room_json(self):
		return {'room_id':self.room_id, 'traps':self.traps, 'building_id':self.building_id, 'district_id':self.district_id}

	def return_json_filename(self):
		return str(self.room_id) + ".json"

	def gen_trap_list(self): #based on the roomID get all of the trap IDs to populate this list.
		pass