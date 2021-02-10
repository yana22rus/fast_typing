from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


profile=webdriver.FirefoxProfile('/home/qwe/.mozilla/firefox/2fvzizeq.default-esr')

browser = webdriver.Firefox(firefox_profile=profile)
browser.implicitly_wait(5)
browser.maximize_window()


browser.get("https://10fastfingers.com/typing-test/english")

def st(s):
	"""Surprise your friends with your fast typing"""

	for i in range(s):
		text = browser.find_element_by_css_selector('.highlight').text
		
		browser.find_element_by_id("inputfield").send_keys(text)

		ActionChains(browser).send_keys(Keys.SPACE).perform()
		

st(int(input("Speed test ")))#max speed - 600


