from lib2to3.pgen2 import driver
from selenium import webdriver
import time

url = "https://www.vk.ru/"
driver = webdriver.Chrome(executable_path='/home/roman/python_course/Selenium_Python/Chrome_ driver/chromedriver')

try:

    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
        print(ex)

finally:
    driver.close()
    driver. quit()