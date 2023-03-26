from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

btn_to_click = driver.find_element(By.XPATH, '//*[@class="context-menu-one btn btn-neutral"]')
right_click_menu = driver.find_elements(By.XPATH, '//ul[@class="context-menu-list context-menu-root"]')

'''right/context click'''
act_chain = ActionChains(driver)
act_chain.context_click(btn_to_click).perform()
'''clicking on Copy context menu item'''
for ele in right_click_menu:
    if ele.text == 'Copy':
        ele.click()
        break