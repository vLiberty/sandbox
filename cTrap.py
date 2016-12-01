import time, random

class cTrap (object):
	#Constructor class. #sell is required, and variables that it will need within itself is defined. (SELF.y)
	def __init__(self, trapid = "0", leftpeerid = "0", rightpeerid ="0", roomid="0", floorid="0", buildingid="0", districtid="0", triggered = "0"):
		if trapid == "0":
			self.id = self.gen_trap_id() #random number generation or passed value for class instanciation
		else:
			self.id = trapid
		self.leftpeerid = leftpeerid
		self.rightpeerid = rightpeerid
		self.roomid = roomid
		self.floorid = floorid
		self.buildingid = buildingid
		self.districtid = districtid
		self.triggered = triggered #triggered, triggered count, 

	def gen_trap_id(self):
		#generate an epoch timestamp and return the millisecond value for the id. 
		#this might have to be more complex. 
		i = str(time.time())
		j = i.split('.')
		k = str(random.random())
		l = k.split('.')
		return j[1].center(8,"0") + "-" + l[1].center(20,"0")

	def return_trap_json(self): #returns all of the object variables as a json structure {dictionary}
		return {'id':self.id, 'leftpeerid':self.leftpeerid, 
				'rightpeerid':self.rightpeerid, 'roomid':self.roomid,
				'buildingid':self.buildingid, 'districtid':self.districtid,
				'triggered':self.triggered}

	def return_json_filename(self):
		return str(self.id) + ".json"

	def get_trap_id(self):
		return self.id

	def get_trap_left(self):
		return self.leftpeerid

	def get_trap_right(self):
		return self.rightpeerid

	def trap_trigger(self):
		self.triggered += 1 #update its trigger by one. THIS might be separated into a different area. 

	def trap_notification(self): 
		pass #create a json record entry of the notification for communication
