'''
Write a function that will mark/check provided option in the dropdown list.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_values_from_dropdown(dropDownOptionsList, value):
    for ele in dropDownOptionsList:
        if ele.text == value:
            ele.click()
            break

industry_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
select_values_from_dropdown(industry_options, 'Education')
select_values_from_dropdown(industry_options, 'Travel')

country_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country]/options')
select_values_from_dropdown(country_options, 'Uganda')
