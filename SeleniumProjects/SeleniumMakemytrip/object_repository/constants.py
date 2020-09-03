#for test cases
CHROME_PATH = r"C:\\Users\\VIGNESH\\Drivers\\chromedriver_win32\\chromedriver.exe"
FROM_LOCATION_REQUIRED = 'Mumbai'
REQUIRED_TO_LOCATION = 'Bengaluru'

#for MakeMyTrip Home Page
HOME_URL = 'https://www.makemytrip.com'
FLIGHT_OPTION_XPATH = '//*[@id="SW"]/div[1]/div[2]/div/div/nav/ul/li[1]'
ROUND_TRIP_OPTION_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[1]/ul/li[2]'
FROM_OPTION_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/label'
FROM_LOCATION_INPUT_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input'
SUGGESTED_FROM_CITIES_XPATH = '//*[@id="react-autowhatever-1"]/div[1]/ul/li'
TO_LOCATION_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]'
TO_LOCATION_INPUT_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/input'
SUGGESTED_TO_CITIES_XPATH = '//*[@id="react-autowhatever-1"]/div[1]/ul/li'
DEPARTURE_OPTION_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[4]/label'
DEPARTURE_DATES_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div'
SEARCH_OPTION_XPATH = '//*[@id="root"]/div/div[2]/div/div/div[2]/p/a'
SEARCH_PAGE_TITLE = 'Makemytrip'

#for search results page
SEARCH_RESULTS_AVAILABILITY = '//*[@id="section--wrapper"]/div[1]/div[3]/div/div[1]/div/span[2]'
DEPARTURE_FLIGHTS_LIST_XPATH = '//*[@id="ow-domrt-jrny"]/div/div'
RETURN_FLIGHTS_LIST_XPATH = '//*[@id="rt-domrt-jrny"]/div/div'
ONE_STOP_XPATH = '//*[@id="section--wrapper"]/div[1]/div[3]/div/div[1]/div/span[2]'
NON_STOP_XPATH = '//*[@id="section--wrapper"]/div[1]/div[3]/div/div[1]/div/span[1]'
REFLECTED_DEPARTURE_FLIGHT_PRICE = '//*[@id="left-side--wrapper"]/div/div/div[4]/div/div[1]/div/div/div[1]/div/div[2]/div/div[3]/p'
REFLECTED_RETURN_FLIGHT_PRICE = '//*[@id="left-side--wrapper"]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[2]/div/div[3]/p'
REFLECTED_TOTAL_VALUE = '//*[@id="left-side--wrapper"]/div/div/div[4]/div/div[1]/div/div/div[3]/div[1]/p/span'
