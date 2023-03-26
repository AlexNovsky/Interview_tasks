from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.com/')

best_sellers_link = driver.find_element(By.LINK_TEXT, 'Best Sellers')
best_sellers_link.click()
driver.back() #going to the previous page
driver.forward() #going to the second visited page
driver.refresh() #refreshing the current page
driver.quit()