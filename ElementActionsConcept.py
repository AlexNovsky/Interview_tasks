from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://classic.crmpro.com/')

username_field = driver.find_element(By.NAME, 'username')
password_field = driver.find_element(By.NAME, 'password')
login_btn = driver.find_element(By.XPATH, '//input[@type="submit"]')

act_chains = ActionChains(driver)
sleep(3)
act_chains.send_keys_to_element(username_field, 'pythonminutes')
act_chains.send_keys_to_element(password_field, 'pythonminutes@1')
act_chains.click(login_btn).perform()
driver.quit()
