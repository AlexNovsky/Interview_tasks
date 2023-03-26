from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


'''Handling javascript alerts on the web-pages'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

sign_in_btn = driver.find_element(By.XPATH, '//input[@type="submit"]')
sign_in_btn.click()

alert = driver.switch_to.alert #switching to pop-up alert
alert.accept()  #accept or click Ok button
# alert.dismiss()  #cancelling the popup
# alert.send_keys('simple text that should be entered in the textbox of pop-up')  #sending text to the popup
driver.switch_to.default_content()

driver.quit()

