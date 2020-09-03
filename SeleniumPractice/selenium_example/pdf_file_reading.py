import pytest
from selenium import webdriver
from .utilities.pdf_handler import PdfHandler


class TestPdfReading:
	test_pdf_file_path = "C:\\Users\\VIGNESH\\PycharmProjects\\SeleniumExample\\resource\\sample.pdf"
	@pytest.fixture
	def get_driver_object(self):
		global driver
		driver = webdriver.Chrome(
			executable_path=r"C:\\Users\\VIGNESH\\Drivers\\chromedriver_win32\\chromedriver.exe")
		driver.maximize_window()
		yield driver
		driver.close()
		driver.quit()

	def test_verify_pdf_in_the_url(self, get_driver_object):
		url = "http://www.africau.edu/images/default/sample.pdf"
		driver.get(url)
		assert driver.current_url.__contains__('pdf')

	def test_verify_the_content_in_the_pdf_file(self, get_driver_object):
		pdf_content = PdfHandler.read_pdf_file(self.test_pdf_file_path)
		assert pdf_content.__contains__('Virtual Mechanics')

	def test_verify_no_of_pages_in_the_pdf_file(self, get_driver_object):
		expected_pages = 2
		pdf_pages_count = PdfHandler.get_pdf_file_page_count(self.test_pdf_file_path)
		assert pdf_pages_count == expected_pages

