from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.disney.com/')

banner_iframe = 'iframe[aria-label="Advertisement"]'
banner_close_button = '//*[@id="overlay"]//*[@class="sprite close"]'

frame = driver.find_element(By.CSS_SELECTOR, banner_iframe)
driver.switch_to.frame(frame) #switching to the targeted frame to perform actions

close_banner = driver.find_element(By.XPATH, banner_close_button)
close_banner.click() #performing action

driver.switch_to.parent_frame() #switch to the parent frame if target frame inside another frame
driver.switch_to.default_content() #switch to original webpage