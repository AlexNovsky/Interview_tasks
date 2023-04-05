from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://jqueryui.com/droppable/')
'''switching to frame with action items'''
frame = driver.find_element(By.XPATH, '//*[@class="demo-frame"]')
driver.switch_to.frame(frame)
'''drag and drop action'''
source = driver.find_element(By.XPATH, '//*[@id="draggable"]')
target = driver.find_element(By.XPATH, '//*[@id="droppable"]')

action = ActionChains(driver)
'''first variant'''
# action.drag_and_drop(source, target).perform() #one drag-and-drop action
'''second variant'''
action.click_and_hold(source).move_to_element(target).release().perform()
'''switching to original page from the frame'''
driver.switch_to.default_content()
