import pytest
from object_repository import constants
from page_objects.news_page import NewsPage


@pytest.mark.usefixtures('get_driver_object')
class TestNewsReading:

	@pytest.fixture(autouse=True)
	def open_website(self, get_driver_object):
		global driver
		driver = get_driver_object
		driver.get(constants.NEWS_SITE_URL)

	def test_read_and_print_all_news_in_current_page(self):
		news_page = NewsPage(driver)
		current_page_news = news_page.read_current_page_news()
		for news in current_page_news:
			print(news)
		print('Total news count in current page ', len(current_page_news))

	def test_read_all_news_along_with_its_score_in_current_page(self):
		news_page = NewsPage(driver)
		news_with_score = news_page.read_current_page_with_score()
		NewsPage.print_news(news_with_score)

	def test_read_news_up_to_required_page_count(self):
		expected_news_entries_count = 120
		news_page = NewsPage(driver)
		news_with_points = news_page.read_news_up_to_page(4)
		NewsPage.print_news(news_with_points)
		NewsPage.print_heading_with_highest_points(news_with_points)
		NewsPage.print_most_occurring_word_in_news(news_with_points)
		assert len(news_with_points) == expected_news_entries_count
