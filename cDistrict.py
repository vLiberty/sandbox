from cTrap import cTrap
from cRoom import cRoom
from cFloor import cFloor
from cBuilding import cBuilding

class cDistrict(cBuilding):
	def __init__(self, district_id=0, buildings = []):
		self.district_id = district_id
		self.buildings = buildings # 
