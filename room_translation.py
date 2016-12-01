import json, os 
"""
Communicates with the source (Raw JSON files -or- eventually HTTP Endpoints) 
- To list, read and write the contents of the ROOM JSON files. 
- Builds lists for looping purposes. (Setting up the proof of concept)

"""
def get_cwd_room():
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	return (fileDir + '/room_json')

#Reading/Writing to a JSON file
def write_json_room(json_str, filename):
	data = json.dumps(json_str)
	path = get_cwd_room() + '/' + filename
	with open(path, 'w') as f:
		json.dump(data, f)

# Reading data back
def read_json_room(filename):
	path = get_cwd_room() + '/' + filename
	with open(path, 'r') as f:
		return json.load(f)

def list_json_room():
	return os.listdir(get_cwd_room())

def delete_json_room(filename): #More logic needs to be added for removing a room. The left/right peer IDs need to be updated on a removed room
	path = get_cwd_room() + '/' + filename
	os.remove(path)

def create_room_dictionary():
	j = 0
	newDictionary = {}
	for i in list_json_room():
		j += 1
		newDictionary[str(j)] = i
	return newDictionary