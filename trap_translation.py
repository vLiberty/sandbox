import json, os 
"""
Communicates with the source (Raw JSON files -or- eventually HTTP Endpoints) 
- To list, read and write the contents of the trap JSON files. 
- Builds lists for looping purposes. (Setting up the proof of concept)

#"""
def get_cwd_trap():
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	return (fileDir + '/trap_json')

#Reading/Writing to a JSON file
def write_json_file(json_str, filename):
	data = json.dumps(json_str)
	path = get_cwd_trap() + '/' + filename
	with open(path, 'w') as f:
		json.dump(data, f)

# Reading data back
def read_json_file(filename):
	path = get_cwd_trap() + '/' + filename
	with open(path, 'r') as f:
		return json.load(f)

def list_json_files():
	return os.listdir(get_cwd_trap())

def delete_json_file(filename):
	path = get_cwd_trap() + '/' + filename
	os.remove(path)

def create_dictionary(): #This is used to create a selection for the json files for the menu.
	j = 0
	newDictionary = {}
	for i in list_json_files():
		j += 1
		newDictionary[str(j)] = i
	return newDictionary

def create_num_trap(trapList): #This is a passed list of narrowed down entries that need to build a selection list for menues. 
	j = 0
	newDictionary = {}
	for i in trapList:
		j += 1
		newDictionary[str(j)] = i['id']
	return newDictionary

def read_json_file_s(filename):
	path = get_cwd_trap() + '/' + filename
	with open(path, 'r') as f:
		return json.load(f)	

def create_dictionary_empty_traps():
	returnList = []
	for key, value in create_dictionary().items():
		temp = json.loads(read_json_file(value)) #If throwing an error on this line, look for .DS_STORE file 
		#temp = read_json_file(value)
		#print ("Key: {} Value: {}".format(key,value))
		if temp["leftpeerid"] == "0" and temp["rightpeerid"] == "0":
			returnList.append(temp)
	#print (returnList[1])
	return returnList

