from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 9)
signup_link = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))
signup_link.click()
first_name = wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'FIRST_NAME')))
first_name.send_keys('Alex')

driver.quit()