import enum


class BooksWagonException(Exception):
	class ExceptionType(enum.Enum):
		NO_BOOK_FOUND = 'Required book can not be found'

	def __init__(self, exception_type):
		self.exception_type = exception_type
