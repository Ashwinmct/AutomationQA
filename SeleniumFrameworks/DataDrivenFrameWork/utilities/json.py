import json

class JSONreader():
	@classmethod
	def load_file(cls, path):
		with open(path, "r+") as json_file:
			data = json.load(json_file)
		return data
