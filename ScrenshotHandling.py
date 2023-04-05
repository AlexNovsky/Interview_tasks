from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


'''making a screenshot of visible part of webpage'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.suse.com')
driver.get_screenshot_as_file('suse.png')

'''making screenshot of full webpage
*** could be taken only in headless mode***'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.suse.com')
#executing javascript scenario to scroll entire webpage
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('SuSe_full_screenshot.png')

driver.quit()
