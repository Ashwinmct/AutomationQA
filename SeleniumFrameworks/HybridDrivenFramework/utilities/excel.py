import xlrd, openpyxl


class Excel(object):
	zero_index = 0

	def get_sheet_by_name(self, path, sheet_name):
		work_book = xlrd.open_workbook(path)
		return work_book.sheet_by_name(sheet_name)

	def get_number_of_rows(self, path, sheet):
		return (self.get_sheet_by_name(path, sheet)).nrows

	def read_data_from_sheet(self, path, sheet_name, row, column):
		return (self.get_sheet_by_name(path, sheet_name)).cell_value(row, column)

