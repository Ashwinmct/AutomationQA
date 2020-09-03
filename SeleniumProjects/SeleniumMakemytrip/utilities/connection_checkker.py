import requests


class Internet(object):
	DEFAULT_CHECKING_URL = 'https://www.google.com'
	DEFAULT_TIME_OUT = 10

	@classmethod
	def check_connection_status(cls, url=DEFAULT_CHECKING_URL, time_out=DEFAULT_TIME_OUT):
		try:
			requests.get(url, time_out)
			return True
		except (requests.ConnectionError, requests.Timeout) as excp:
			print('No internet connection\n')
			print(excp)
			return False
