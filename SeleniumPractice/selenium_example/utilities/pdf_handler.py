import PyPDF4


class PdfHandler:
	@classmethod
	def read_pdf_file(cls, pdf_file_path):
		pdf_file = cls.get_pdf_file(pdf_file_path)
		pdf_page = pdf_file.getPage(0)
		return pdf_page.extractText()

	@classmethod
	def get_pdf_file_page_count(cls, file_path):
		pdf_file = cls.get_pdf_file(file_path)
		return pdf_file.getNumPages()

	@classmethod
	def get_pdf_file(cls, pdf_file_path):
		pdf_file = open(pdf_file_path, 'rb')
		return PyPDF4.PdfFileReader(pdf_file)

