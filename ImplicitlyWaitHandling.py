from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

'''Global function, applied only for the web elements with functions find_element, find_elements
not for non web elements such as title, url, alerts etc'''
driver.implicitly_wait(8)
# driver.implicitly_wait(0) #canceling previous setting
driver.get('https://app.hubspot.com/login')

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys('pizzaHut')

driver.quit()
