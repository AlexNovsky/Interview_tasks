from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


'''defining options for the webdriver manager'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')
'''assigning Chromedriver via Webdriver manager'''
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
'''assigning Chromedriver via selenuim webdriver'''
driver = webdriver.Chrome(options=options)

driver.get('https://www.amazon.com')
print(driver.title)

driver.quit()