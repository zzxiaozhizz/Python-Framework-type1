from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# driver = webdriver.Chrome('../SeleniumDriver/chromedriver')
# driver.get('Http://www.baidu.com')
# driver.implicitly_wait(10)
# # driver.close()

# searchmsg = (By.ID, "kw")
# searbox = driver.find_element(*searchmsg)
# searbox.send_keys()

# search_btn = driver.find_element(By.ID,"su")
# search_btn.click()
# driver.close()

a = (By.ID, 'asdw')
print((*a))

# driver = webdriver.Chrome('../SeleniumDriver/chromedriver')
# driver.find_element()