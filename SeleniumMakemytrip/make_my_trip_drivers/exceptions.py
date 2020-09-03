from enum import Enum


class MakeMyTripException(Exception):
	class ExceptionType(Enum):
		INTERNET_FAILURE = 'Check Internet Connection'
		NO_FLIGHTS_FOUND = 'No flights can be found in given route'

	def __init__(self, exception_type):
		self.exception_type = exception_type
