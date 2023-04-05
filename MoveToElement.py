'''
Could you write the code, that will navigate to the element and perform the action?
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.spicejet.com/')
login_ele = driver.find_element(By.XPATH, '//*[@id="ctl00_HyperLinkLogin"]')
act_chains = ActionChains(driver)
act_chains.scroll_to_element(login_ele).perform()

spice_club_members_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_chains.scroll_to_element(spice_club_members_ele).perform() #scrolling the webpage to the element

member_login_ele = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login_ele.click() #performing the action with the targeted element
driver.quit()
