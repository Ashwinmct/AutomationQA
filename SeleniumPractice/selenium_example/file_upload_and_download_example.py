import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSeleniumFileUploadAndDownload:
	@pytest.fixture
	def get_driver_object(self):
		global driver
		driver = webdriver.Chrome(executable_path=r"C:\\Users\\VIGNESH\\Drivers\\chromedriver_win32\\chromedriver.exe")
		driver.maximize_window()
		yield driver
		driver.close()
		driver.quit()

	def test_file_upload_in_selenium(self, get_driver_object):
		file_path = 'C:\\Users\\VIGNESH\\PycharmProjects\\SeleniumExample\\resource\\demo.txt'
		driver.get('http://demo.guru99.com/test/upload')
		driver.find_element(By.ID, 'uploadfile_0').send_keys(file_path)
		driver.find_element(By.ID, 'terms').click()
		driver.find_element(By.ID, 'submitbutton').click()

	def test_file_download_in_selenium(self, get_driver_object):
		url = "http://demo.automationtesting.in/FileDownload.html"
		driver.get(url)
		driver.find_element_by_id("textbox").send_keys("Testing the file downloading operation")
		time.sleep(5)
		driver.find_element_by_id("createTxt").click()
		time.sleep(5)
		driver.find_element_by_id("link-to-download").click()
