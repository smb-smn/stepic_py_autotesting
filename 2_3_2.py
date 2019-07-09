import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()

##browser.switch_to.window(browser.window_handles[1])#переход на новую вкладку
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.close()