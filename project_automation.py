from selenium import webdriver

chrome_browser = webdriver.Chrome('./automation_testing/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Heyyyy I Am Dhruuuvvv..')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

chrome_browser.quit()
