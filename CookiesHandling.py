'''
Write a code that will show how you can manage cookies during your tests with Selenium
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.reddit.com/')

cookies = driver.get_cookies()

'''print all cookies on the page variant 1'''
for cook in cookies:
    print(cookies)

'''print all cookies on the page variant 2'''
print(cookies)

'''print amount of cookies on the page'''
print(len(cookies))
'''adding (sending) cookies to the webpage. Cookies could be sent as a dictionary'''
driver.add_cookie({"domain":"reddit.com","name":"alexpython","value":"python"})

driver.quit()
