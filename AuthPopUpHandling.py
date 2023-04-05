'''
Write a code that will provide username and password directly into authentication pop-up window(alert)
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://admn:admin@the-internet.herokuapp.com/basic_auth') #Providing username and password admin:admin
driver.quit()
