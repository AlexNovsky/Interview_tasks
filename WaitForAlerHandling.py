'''
How would you avoid usage of sleep function?
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')


wait = WebDriverWait(driver, 9)

sign_in_btn = driver.find_element(By.NAME, 'proceed')
sign_in_btn.click()
alert = wait.until(expected_conditions.alert_is_present())
alert.accept()

driver.quit()