from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from object_repository import constants


class NewsPage:
	FIRST_PAGE = 0

	def __init__(self, driver):
		self.driver = driver

	def read_current_page_news(self):
		return self.__read_page_content(constants.NEWS_XPATH)

	def read_current_page_with_score(self):
		current_page_news = self.read_current_page_news()
		current_page_scores = self.read_current_page_points()
		return self.__combine_news_and_score(current_page_news, current_page_scores)

	def read_current_page_points(self):
		points_list = self.__read_page_content(constants.SCORE_PATH)
		return [self.filter_numbers(points) for points in points_list]

	def __read_page_content(self, item_path):
		content_list = self.driver.find_elements(By.XPATH, item_path)
		return [content.text for content in content_list]

	@staticmethod
	def __combine_news_and_score(news_list, score_list):
		return dict(zip(news_list, score_list))

	def read_news_up_to_page(self, pages):
		news_dict = {}
		for page in range(pages):
			current_page_news = self.read_current_page_with_score()
			news_dict = current_page_news if page == self.FIRST_PAGE else self.__merge(current_page_news, news_dict)
			self.click_more_button()
		return news_dict

	def click_more_button(self):
		more_button = self.driver.find_element(By.XPATH, constants.MORE_BUTTON_XPATH)
		ActionChains(self.driver).move_to_element(to_element=more_button).click(on_element=more_button).perform()

	@staticmethod
	def __merge(dictionary1, dictionary2):
		merged_dictionary = {**dictionary1, **dictionary2}
		return merged_dictionary

	@staticmethod
	def filter_numbers(points):
		return int((points.split(' '))[0])

	@staticmethod
	def print_news(news_dictionary):
		print('news : points')
		[print(news, point) for news, point in news_dictionary.items()]
		print('Total entries of news ', len(news_dictionary))

	@staticmethod
	def print_heading_with_highest_points(news_with_points_dictionary):
		# find the key with highest value and print
		news_heading_with_highest_point = max(news_with_points_dictionary, key=news_with_points_dictionary.get)
		print('\nNews heading with highest point :', news_heading_with_highest_point, '\nHighest Points: ',
		      news_with_points_dictionary[news_heading_with_highest_point])

	@staticmethod
	def print_most_occurring_word_in_news(news_and_points_dictionary):
		# get all the news headings -> split each heading into list of words -> combine into single flatten list
		# ->find most occurring word and print
		news = news_and_points_dictionary.keys()
		news_heading_words_lists = [heading.split(' ') for heading in news]
		words_list = [word for heading in news_heading_words_lists for word in heading]
		print('\n Most occurring word :', max(set(words_list), key=words_list.count))
