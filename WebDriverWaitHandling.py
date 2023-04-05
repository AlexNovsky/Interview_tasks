from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 9)

# wait.until(expected_conditions.title_is('HubSpot Login'))
wait.until(expected_conditions.title_contains('HubSpot'))

email_id = wait.until(expected_conditions.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('abrakadabra.com')

driver.find_element(By.ID, 'password')
