CHROME_DRIVER_PATH = r"C:\\Users\\VIGNESH\\Drivers\\chromedriver_win32\\chromedriver.exe"
#Home page details
HOME_PAGE_BUTTON = '//*[@id="ctl00_imglogo"]'
BOOKS_WAGON_URL = 'https://www.bookswagon.com'
HOME_PAGE_LOGIN_BUTTON = '//*[@id="ctl00_divLogin"]/ul/li[1]'
HOME_PAGE_USER_ACCOUNT_BUTTON = '//*[@id="ctl00_lblUser"]'
LOG_OUT_OPTION = '//*[@id="ctl00_lnkbtnLogout"]'
SEARCH_BOX_XPATH = '//*[@id="ctl00_TopSearch1_txtSearch"]'
BEST_SELLERS = '//*[@id="ctl00_libestseller"]/a'
WISH_LIST_OPTION = '//*[@id="ctl00_divLogged"]/ul/li/div/div/div[1]/ul/li[4]/a'
#Login Page
LOGIN_PAGE_URL = 'https://www.bookswagon.com/login'
LOGIN_EMAIL_ID_XPATH = '//*[@id="ctl00_phBody_SignIn_txtEmail"]'
LOGIN_PASSWORD_XPATH = '//*[@id="ctl00_phBody_SignIn_txtPassword"]'
LOGIN_PAGE_LOG_IN_BUTTON = '//*[@id="ctl00_phBody_SignIn_btnLogin"]'
#user account page
USER_ACCOUNT_PAGE_URL = 'https://www.bookswagon.com/myaccount.aspx'
HOME_BUTTON_XPATH = '//*[@id="ctl00_lihome"]/a'
##wish list
BUY_WISH_LIST_BOOKS_XPATH = '//*[@id="ctl00_phBody_WishList_lvWishList_ctrl0_divAddtoCart"]/a/input'
SELECT_ALL_BOOKS = '//*[@id="ctl00_phBody_WishList_lvWishList_chkAll"]'
BUY_SELECTED_BOOKS = '//*[@id="ctl00_phBody_WishList_lvWishList_chkAll"]'
EMPTY_WISH_LIST = '//*[@id="book"]/div[2]'
REMOVE_ALL_BUTTON = '//*[@id="ctl00_phBody_WishList_lvWishList_imgDelete"]'
BOOK_IN_WISH_LIST = '//*[@id="book"]/div[2]/div[1]/div[3]/div[1]/a'
#books page
BUY_NOW_BUTTON_XPATH = '//*[@id="ctl00_phBody_ProductDetail_divAddtoCart"]/a/input'
#best sellers page
BEST_SELLING_BOOKS_XPATH = '//*[@id="listSearchResult"]/div/div[4]/div[5]/a[2]/input'
BELOW_100_RS = '//*[@id="site-wrapper"]/div[3]/div[2]/div[2]/div[2]/ul[1]/li[2]/a'
CHEAPEST_BOOK_IN_BEST_SELLER_PAGE_NAME_XPATH = '//*[@id="listSearchResult"]/div/div[3]/div[1]/a'
# cart
CART_ICON_XPATH = '//*[@id="topright-menu"]/div[2]/div[1]/a'
REMOVE_LIST_CLASS = 'remove'
CART_FRAME_XPATH = '//*[@id="cboxLoadedContent"]/iframe'
CART_CLOSER_XPATH = '//*[@id="cboxClose"]'
QUANTITY_BOX = '//*[@id="BookCart_lvCart_ctrl0_txtQty"]'
PLACE_ORDER = '//*[@id="BookCart_lvCart_ctrl0_imgUpdate"]'
CONTINUE_SHOPPING = '//*[@id="BookCart_uplnShopping"]/div[2]/a'
