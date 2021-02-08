from time import sleep

from selenium import webdriver

#chrome.exe --remote-debugging-port=9222
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

# driver=webdriver.Chrome()
driver.implicitly_wait(3)
url='https://detail.tmall.com/item.htm?id=634443792690&spm=608.7065813.botbar.addcart.70aa7787RNRklj'
driver.get(url)
driver.find_element_by_link_text('点此进入').click()
sleep(1)
locator = (By.LINK_TEXT, '马上抢')
WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable(locator))
ele = driver.find_element(*locator)
while True:
    print(ele.text)
    webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
    # ele.click()
    if '确定' in driver.page_source:
        break
    sleep(0.2)
locator = (By.LINK_TEXT, '确定')
print(driver.page_source)
WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable(locator))
while True:
    ele = driver.find_element(*locator)
    print(ele.text)
    ele.click()
    sleep(0.2)
# sleep(5)
# driver.close()