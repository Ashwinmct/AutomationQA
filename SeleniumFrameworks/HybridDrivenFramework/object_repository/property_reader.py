from jproperties import Properties


class ReadProperties:
	file_path = 'C:\\Users\\VIGNESH\\PycharmProjects\\HDF\\object_repository\\object.properties'
	def __init__(self):
		self.configs = Properties()
		self.properties_dictionary = self.__load_property_dictionary()

	def __load_property_dictionary(self):
		properties = self.__load_properties()
		properties_dictionary = {}
		for property in properties:
			properties_dictionary[property[0]] = property[1].data
		return properties_dictionary

	def __load_properties(self):
		with open(self.file_path, 'rb') as config_file:
			self.configs.load(config_file)
		return self.configs.items()

	def get(self, property):
		return self.properties_dictionary.get(property)
