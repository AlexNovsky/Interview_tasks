from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

choose_file_btn = driver.find_element(By.XPATH, '//input[@type="file"]')
choose_file_btn.send_keys('/Users/DeBeers/Desktop/test')
upload_btn = driver.find_element(By.XPATH, '//input[@type="submit"]')
driver.quit()
