import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
if __name__=='__main__':

    pytest.main(["-vs","./testcase/TestBaidu.py", "--alluredir", "./report/allure-result"])

    '''
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    time.sleep(2)
    driver.find_element(By.ID,'s-top-loginbtn').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_25__closeBtn"]').click()
    '''
