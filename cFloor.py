from cTrap import cTrap
from cRoom import cRoom

class cFloor(cRoom):
	def __init__(self, floor_id=0, rooms = [], building_id =0, district_id=0):
		self.floor_id = floor_id
		self.rooms = rooms #function to retrieve the list of rooms
		self.building_id = building_id
		self.district_id = district_id

		 