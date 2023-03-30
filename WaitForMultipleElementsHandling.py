from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.freshworks.com/')

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_all_elements_located(By.CSS_SELECTOR, 'your_selector'))
