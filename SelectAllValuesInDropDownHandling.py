'''
Write a function that will check list of the options, that should be marked/checked in the dropdown list and mark them.
Add an additional verification if user wants to mark All options
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def select_all_values(options_list, value):
    if not value[0].lower() == 'all':
        for ele in drop_list:
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

driver.find_element(By.ID, 'justAnInputBox').click()

drop_list = driver.find_element(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
values_list = ['all']
# values_list = ['choice 2', 'choice 3', 'choice 6 2 1']

select_all_values(drop_list, values_list)
