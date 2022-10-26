from selenium.webdriver.common.action_chains import ActionChains
driver.maximize_window()

# Одно действие - движение к елементу

actions = ActionChains(driver)
actions.move_to_element('element').perform()
time.sleep(3)